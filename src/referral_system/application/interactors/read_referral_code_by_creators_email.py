from dataclasses import dataclass

from referral_system.application.errors import ReferralCodeDoesNotExists
from referral_system.application.interfaces.identity_provider import IdentityProvider
from referral_system.application.interfaces.referral_code_data_gateway import (
    ReferralCodeDataGateway,
)
from referral_system.application.interfaces.transaction_manager import (
    TransactionManager,
)
from referral_system.domain.entities.referral_code import ReferralCode, Title
from referral_system.domain.entities.user import Email


@dataclass
class ReadReferralCodeByCreatorsEmailRequest:
    email: Email


@dataclass
class ReadReferralCodeByCreatorsEmailResponse:
    title: Title


class ReadReferralCodeByCreatorsEmailInteractor:
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
        self, request_data: ReadReferralCodeByCreatorsEmailRequest
    ) -> ReadReferralCodeByCreatorsEmailResponse:
        referral_code: (
            ReferralCode | None
        ) = await self._referral_code_data_gateway.read_by_creator_email(
            email=request_data.email
        )

        if referral_code is None:
            raise ReferralCodeDoesNotExists(
                "There is no referral code created by a user with such an email."
            )

        return ReadReferralCodeByCreatorsEmailResponse(
            title=referral_code.title,
        )
