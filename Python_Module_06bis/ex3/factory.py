#!/usr/bin/python3
from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon
from .entities import Shiftling, Morphagon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Crea la entidad base de la familia."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Crea la entidad evolucionada de la familia."""
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
