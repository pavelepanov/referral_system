from typing import Protocol

from referral_system.domain.entities.referral_code import ReferralCodeId


class ReferralCodeIdGenerator(Protocol):
    def __call__(self) -> ReferralCodeId: ...
