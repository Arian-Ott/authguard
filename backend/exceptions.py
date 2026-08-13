class UsernameFormatError(Exception):
    pass


class UserAlreadyExists(Exception):
    pass


class PasswordMissmatchError(Exception):
    pass


class InvalidPasswordStrength(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class ValidationError(Exception):
    pass


class DuplicateDataError(Exception):
    pass


class Forbidden(Exception):
    pass


class NotFound(Exception):
    pass
