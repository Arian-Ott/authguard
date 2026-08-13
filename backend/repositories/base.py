from typing import Generic, TypeVar

from tortoise.exceptions import IntegrityError
from tortoise.models import Model

from backend.exceptions import DuplicateDataError

T = TypeVar("T", bound=Model)


class BaseRepository(Generic[T]):
    def __init__(self, model: type[T]):
        self.model = model

    async def get_by_id(self, obj_id: int) -> T | None:
        """Gets entry by id.

        :param obj_id: Primary key of the object
        :type obj_id: int
        :return: Returns object if found, otherwise none
        :rtype: T | None
        """

        return await self.model.get_or_none(id=obj_id)

    async def get_all(self, limit: int = 1000) -> list[T]:
        """Gets all entries from a database table.

        To prevent large table locks, a limit of 1000 entries
        is specified.

        :param limit: Amount of elements to be fetched, defaults to 1000
        :type limit: int, optional
        :return: List of all elements
        :rtype: list[T]
        """
        return await self.model.all().limit(limit)

    async def create(self, **kwargs) -> T:
        """Creates an entity in the database.

        :raises DuplicateDataError: Re-raises an integrity error to decouple from the ORM
        :return: Created object
        :rtype: T
        """
        try:
            return await self.model.create(**kwargs)
        except IntegrityError as e:
            raise DuplicateDataError(str(e)) from e

    async def update(self, obj_id: int, **kwargs) -> T | None:
        """Updates an object.

        :param obj_id: Primary key of the objext
        :type obj_id: int
        :return: Updated database entry
        :rtype: T | None
        """

        await self.model.filter(id=obj_id).update(**kwargs)
        return await self.get_by_id(obj_id)

    async def delete(self, obj_id: int) -> bool:
        """Deletes an object in the database.

        :param obj_id: Primary key of the object
        :type obj_id: int
        :return: Truthy if deleted, falsy otherwise
        :rtype: bool
        """
        deleted = await self.model.filter(id=obj_id).delete()
        return deleted > 0
