from abc import ABC, abstractmethod
from ..models import AdapterResponse

class ConformanceAdapter(ABC):
    """Construction-neutral interface used by the harness."""
    @abstractmethod
    def describe_capabilities(self) -> set[str]: ...
    @abstractmethod
    def execute(self, operation: str, request: dict) -> AdapterResponse: ...
