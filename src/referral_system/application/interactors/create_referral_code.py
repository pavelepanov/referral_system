from dataclasses import dataclass

from referral_system.application.errors import ReferralCodeAlreadyExists
from referral_system.application.interfaces.identity_provider import IdentityProvider
from referral_system.application.interfaces.referral_code_data_gateway import (
    ReferralCodeDataGateway,
)
from referral_system.application.interfaces.referral_code_id_generator import (
    ReferralCodeIdGenerator,
)
from referral_system.application.interfaces.referral_code_title_generator import (
    ReferralCodeTitleGenerator,
)
from referral_system.application.interfaces.transaction_manager import (
    TransactionManager,
)
from referral_system.domain.entities.referral_code import (
    Expiration,
    ReferralCode,
    Title,
    create_referral_code,
)
from referral_system.domain.entities.user import UserId


@dataclass
class CreateReferralCodeRequest:
    expiration_in_minutes: Expiration


@dataclass
class CreateReferralCodeResponse:
    title: Title


class CreateReferralCodeInteractor:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        referral_code_id_generator: ReferralCodeIdGenerator,
        referral_code_title_generator: ReferralCodeTitleGenerator,
        referral_code_data_gateway: ReferralCodeDataGateway,
        transaction_manager: TransactionManager,
    ):
        self._identity_provider = identity_provider
        self._referral_code_id_generator = referral_code_id_generator
        self._referral_code_title_generator = referral_code_title_generator
        self._referral_code_data_gateway = referral_code_data_gateway
        self._transaction_manager = transaction_manager

    async def __call__(
        self, request_data: CreateReferralCodeRequest
    ) -> CreateReferralCodeResponse:
        user_id: UserId = await self._identity_provider.get_current_user_id()
        referral_code_id = self._referral_code_id_generator()
        referral_code_title = self._referral_code_title_generator()

        referral_code: ReferralCode = create_referral_code(
            id=referral_code_id,
            title=referral_code_title,
            expiration=request_data.expiration_in_minutes,
            created_by_user_id=user_id,
        )

        referral_code_from_storage: (
            ReferralCode | None
        ) = await self._referral_code_data_gateway.read_by_creator_id(
            creator_id=user_id
        )

        if referral_code_from_storage is not None:
            raise ReferralCodeAlreadyExists("You can only have one referral code.")

        await self._referral_code_data_gateway.add(referral_code=referral_code)

        await self._transaction_manager.commit()

        return CreateReferralCodeResponse(title=referral_code.title)
