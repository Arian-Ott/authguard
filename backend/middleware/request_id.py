import secrets
from contextvars import ContextVar

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

request_id_var: ContextVar[str] = ContextVar("request_id", default="-")
correlation_id_var: ContextVar[str] = ContextVar("correlation_id", default="-")


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Assigns a per-request ID and propagates a correlation ID.

    Request-ID: always generated fresh per service hop.
    Correlation-ID: adopted from `X-Correlation-ID` if provided, otherwise
    generated. Both are placed into the response headers so downstream
    components (or the user's browser inspector) can pick them up.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        """Adds a request id and correlation id to a request if needed.

        Keeps existing correlation IDs.

        :param request: Incoming request
        :type request: Request
        :param call_next: Next Request step
        :type call_next: _type_
        :return: Response with added IDs
        :rtype: Response
        """
        request_id = secrets.token_urlsafe(16)
        request_id_var.set(request_id)

        incoming = request.headers.get("x-correlation-id")
        correlation_id = incoming if incoming else secrets.token_urlsafe(16)
        correlation_id_var.set(correlation_id)

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Correlation-ID"] = correlation_id
        return response
