from db.users import users
from models.user import User, UserIn
from .base import BaseRepository
from typing import List, Optional
import datetime
from core.security import hash_password, verify_password


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        quary = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(quary=quary)

    async def get_by_id(self, id: int) -> Optional[User]:
        quary = users.select().where(users.c.id==id).first()
        user = await self.database.fetch_one(quary)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        values = {**user.dict()}
        values.pop("id", None)
        quary = users.insert().values()
        user.id = await self.database.execute(quary)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        quary = users.update().where(users.c.id==id).values()
        user.id = await self.database.execute(quary)
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        quary = users.select().where(users.c.email == email).first()
        user = await self.database.fetch_one(quary)
        if user is None:
            return None
        return User.parse_obj(user)
