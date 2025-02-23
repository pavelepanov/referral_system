from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from referral_system.domain.entities.referral_code import ReferralCodeId

UserId = NewType("UserId", UUID)
Email = NewType("Email", str)
PasswordHash = NewType("PasswordHash", str)

RawPassword = NewType("RawPassword", str)


@dataclass
class User:
    id: UserId
    email: Email
    password_hash: PasswordHash
    registered_by_referral_code_id: ReferralCodeId


def create_user(
    id: UserId,
    email: Email,
    password_hash: PasswordHash,
    registered_by_referral_code_id: ReferralCodeId,
) -> User:
    return User(
        id=id,
        email=email,
        password_hash=password_hash,
        registered_by_referral_code_id=registered_by_referral_code_id,
    )
