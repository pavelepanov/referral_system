from referral_system.application.errors import ReferralCodeDoesNotExists
from referral_system.application.interfaces.identity_provider import IdentityProvider
from referral_system.application.interfaces.referral_code_data_gateway import (
    ReferralCodeDataGateway,
)
from referral_system.application.interfaces.transaction_manager import (
    TransactionManager,
)
from referral_system.domain.entities.referral_code import ReferralCode
from referral_system.domain.entities.user import UserId


class DeleteReferralCodeInteractor:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        referral_code_data_gateway: ReferralCodeDataGateway,
        transaction_manager: TransactionManager,
    ):
        self._identity_provider = identity_provider
        self._referral_code_data_gateway = referral_code_data_gateway
        self._transaction_manager = transaction_manager

    async def __call__(self) -> None:
        user_id: UserId = await self._identity_provider.get_current_user_id()

        referral_code: (
            ReferralCode | None
        ) = await self._referral_code_data_gateway.read_by_creator_id(
            creator_id=user_id
        )

        if referral_code is None:
            raise ReferralCodeDoesNotExists("You don't have a referral code.")

        await self._referral_code_data_gateway.delete(referral_code_id=referral_code.id)

        await self._transaction_manager.commit()
