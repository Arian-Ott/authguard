import logging
import secrets

from argon2 import PasswordHasher

from ..exceptions import DuplicateDataError, UserAlreadyExists
from ..models import UserModel
from ..repositories.user import UserRepo

logger = logging.getLogger(__name__)
_PH = PasswordHasher()
_FALSE_HASH = secrets.token_urlsafe(64)


class UserService:
    def __init__(self, user_repo: UserRepo):
        self._user_repo = user_repo

    async def register(
        self,
        username: str,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> UserModel | None:
        _hashed_pw = _PH.hash(password)

        try:
            new_user = await self._user_repo.create(
                username=username,
                email=email,
                password=_hashed_pw,
                first_name=first_name,
                last_name=last_name,
            )
            logger.info(
                f"User registered. id={new_user.id}",
            )
            return new_user
        except DuplicateDataError:
            logger.warning(
                "Could not create user. Email or username already registered."
            )
            raise UserAlreadyExists(
                "A user with this username or email already exists."
            )
