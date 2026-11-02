#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._stored_data: list[str] = []
        self._counter_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # Valida si el dato puede ser procesado.
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingiere el dato es valido; de lo contrario lanza una excepcion."""
        pass

    def output(self) -> tuple[int, str]:
        """Extrae y retorna (rango, dato) del elemento mas antiguo."""
        if not self._stored_data:
            raise ValueError("No data to extract")

        value: str = self._stored_data.pop(0)  # pop(0) Saca pimer elemento
        rank = self._counter_rank
        self._counter_rank += 1
        return rank, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._stored_data.append(str(item))
        else:
            self._stored_data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._stored_data.append(item)
        else:
            self._stored_data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                isinstance(data.get("log_level"), str)
                and isinstance(data.get("log_message"), str)
            )
        if isinstance(data, list):
            return all(self.validate(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item["log_level"]
            message = item["log_message"]
            self._stored_data.append(f"{level}: {message}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    # ---- Numeric Processor ----
    print("Testing Numeric Processor...")
    num_proces = NumericProcessor()

    print(f"Trying to validate input '42': {num_proces.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proces.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proces.ingest("foo")  # type: ignore[arg-type]
    except ValueError as error:
        print(f"Got exception: {error}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num_proces.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for i in range(3):
        rank, value = num_proces.output()
        print(f"Numeric value {rank}: {value}")

    # ---- Text Processor ----
    print("\nTesting Text Processor...")
    text_proces = TextProcessor()

    print(f"Trying to validate input '42': {text_proces.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_proces.ingest(['Hello', 'Nexus', 'World'])

    print("Extracting 1 value...")
    rank, value = text_proces.output()
    print(f"Text value {rank}: {value}")

    # ---- Log Processor ----
    print("\nTesting Log Processor...")
    log_proces = LogProcessor()

    print(f"Trying to validate input 'Hello': {log_proces.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    log_proces.ingest(logs)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proces.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
