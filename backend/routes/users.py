from fastapi import APIRouter, HTTPException, status

from ..dependencies.services import UserServiceDep
from ..exceptions import UserAlreadyExists
from ..schemas.users import UserCreate, UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse)
async def post_user(user: UserCreate, user_service_dep: UserServiceDep):
    try:
        new_user = await user_service_dep.register(
            username=user.username,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        return new_user
    except UserAlreadyExists as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email is already registered.",
        ) from e
