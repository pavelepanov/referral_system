from referral_system.domain.errors import Error


class ApplicationError(Error): ...


class ReferralCodeAlreadyExists(ApplicationError): ...
