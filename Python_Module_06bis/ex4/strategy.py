#!/usr/bin/python3
from abc import ABC, abstractmethod
from ex3.creature import Creature
from ex3.capability import TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        """Devuelve True si la entidad puede usar esta estrategia."""
        pass

    @abstractmethod
    def act(self, entity: Creature) -> None:
        """Ejecuta la estrategia sobre la entidad."""
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return True  # válida para cualquier criatura

    def act(self, entity: Creature) -> None:
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        # Solo es válida si la entidad tiene la capacidad de transformarse
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if isinstance(entity, TransformCapability):
            # Secuencia: transformarse → atacar → volver a la normalidad
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())
        else:
            raise ValueError(
                f"Invalid creature '{entity.name}'"
                " for this aggressive strategy"
            )
