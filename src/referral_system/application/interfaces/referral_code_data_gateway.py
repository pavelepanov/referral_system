from abc import abstractmethod
from typing import Protocol

from referral_system.domain.entities.referral_code import ReferralCode
from referral_system.domain.entities.user import UserId


class ReferralCodeDataGateway(Protocol):
    @abstractmethod
    async def add(self, referral_code: ReferralCode) -> None: ...

    @abstractmethod
    async def read_by_creator_id(self, creator_id: UserId) -> ReferralCode | None: ...
