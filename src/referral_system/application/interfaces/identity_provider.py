from abc import abstractmethod
from typing import Protocol


class IdentityProvider(Protocol):
    @abstractmethod
    async def is_authenticated(self) -> bool: ...
