from typing import Annotated

from fastapi import Depends

from ..models import UserModel
from ..repositories.user import UserRepo


def get_user_repo() -> UserRepo:
    return UserRepo(UserModel)


UserRepoDep = Annotated[UserRepo, Depends(get_user_repo)]
