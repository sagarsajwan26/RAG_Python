from app.models.user import User
from app.repositories.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_all_users(self) -> list[User]:
        return await self.repository.get_all()
