from typing import Protocol

from referral_system.domain.entities.referral_code import Title


class ReferralCodeTitleGenerator(Protocol):
    def __call__(self) -> Title: ...
