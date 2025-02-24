from abc import abstractmethod
from typing import Protocol

from referral_system.domain.entities.user import Email, UserId


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_current_user_id(self) -> UserId: ...

    @abstractmethod
    async def get_current_user_email(self) -> Email: ...
