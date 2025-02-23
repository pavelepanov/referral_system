from dataclasses import dataclass
from typing import NewType
from uuid import UUID
from datetime import datetime

from referral_system.domain.entities.user import UserId

ReferralCodeId = NewType("ReferralCodeId", UUID)
Title = NewType("Title", str)
Expiration = NewType("Expiration", datetime)


@dataclass
class ReferralCode:
    id: ReferralCodeId
    title: Title
    expiration: Expiration
    created_by_user_id: UserId






def create_referral_code(id: ReferralCodeId,
    title: Title,
    expiration: Expiration,
    created_by_user_id: UserId,
) -> ReferralCode:
    return ReferralCode(
        id=id,
        title=title,
        expiration=expiration,
        created_by_user_id=created_by_user_id,
    )
