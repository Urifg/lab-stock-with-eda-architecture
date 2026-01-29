from abc import ABC, abstractmethod
from ..entities.batch import Batch


class BatchRepository(ABC):
    @abstractmethod
    async def get(self, reference: str) -> Batch | None: ...

    @abstractmethod
    async def add(self, batch: Batch) -> None: ...
