from ..models import UserModel
from .base import BaseRepository


class UserRepo(BaseRepository["UserModel"]):
    async def get_by_username(self, username: str) -> UserModel | None:
        """Gets a user by a username.

        :param username: Username of the user within the database.
        :type username:str
        :returns: Instance of a user, none if user was not found.
        """
        return await self.model.get_or_none(username=username)
