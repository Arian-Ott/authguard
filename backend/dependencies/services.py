from typing import Annotated

from fastapi import Depends

from ..services.user import UserService
from .repos import UserRepoDep


def get_user_service(user_repo_dep: UserRepoDep):
    return UserService(user_repo_dep)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
