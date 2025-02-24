from dataclasses import dataclass

from referral_system.application.errors import UsersInfoNotFoundByReferralCode
from referral_system.application.interfaces.identity_provider import IdentityProvider
from referral_system.application.interfaces.referral_code_data_gateway import (
    ReferralCodeDataGateway,
)
from referral_system.application.interfaces.transaction_manager import (
    TransactionManager,
)
from referral_system.domain.entities.user import User, UserId


@dataclass
class ReadInfoAboutReferralsByCreatorIdRequest:
    creator_id: UserId


@dataclass
class ReadInfoAboutReferralsByCreatorIdResponse:
    users_info: list[User]


class ReadInfoAboutReferralsByCreatorIdInteractor:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        referral_code_data_gateway: ReferralCodeDataGateway,
        transaction_manager: TransactionManager,
    ):
        self._identity_provider = identity_provider
        self._referral_code_data_gateway = referral_code_data_gateway
        self._transaction_manager = transaction_manager

    async def __call__(
        self, request_data: ReadInfoAboutReferralsByCreatorIdRequest
    ) -> ReadInfoAboutReferralsByCreatorIdResponse:
        users_info: (
            list[User] | None
        ) = await self._referral_code_data_gateway.read_info_about_referrals(
            creator_id=request_data.creator_id
        )

        if users_info is None:
            raise UsersInfoNotFoundByReferralCode

        return ReadInfoAboutReferralsByCreatorIdResponse(
            users_info=users_info,
        )
