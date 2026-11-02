#!/usr/bin/python3
from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transforma la criatura y devuelve un mensaje."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Vuelve a la forma normal y devuelve un mensaje."""
        pass

    def is_transformed(self) -> bool:
        return self._transformed
