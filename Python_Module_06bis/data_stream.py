#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._stored_data: list[str] = []
        self._counter_rank: int = 0
        self.total_processed: int = 0

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
            self.total_processed += len(data)
        else:
            self._stored_data.append(str(data))
            self.total_processed += 1


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
            self.total_processed += len(data)
        else:
            self._stored_data.append(data)
            self.total_processed += 1


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
        self.total_processed += len(items)


class DataStream:
    """Gestiona y enruta con flujo heterogéneo datos mediante polimorfismo."""
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Enruta cada elemento al procesador adecuado que lo valide."""
        for element in stream:
            accepted: bool = False
            for proces in self._processors:
                if proces.validate(element):
                    proces.ingest(element)
                    accepted = True
                    break
            if not accepted:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        """Muestra estadísticas de procesamiento de cada procesador."""
        if not self._processors:
            print("No processor found, no data")
            return

        for proces in self._processors:
            proces_name = proces.__class__.__name__.replace(
                "Processor", " Processor"
            )
            print(
                f"{proces_name}: "
                f"total {proces.total_processed} items processed, "
                f"remaining {len(proces._stored_data)} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    stream = DataStream()

    print("Initialize Data Stream...")
    print("=== DataStream statistics ===")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    stream.register_processor(NumericProcessor())

    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        {
            "log_level": "WARNING",
            "log_message": "Telnet access! Use ssh instead"
        },
        {"log_level": "INFO", "log_message": "User wil is connected"},
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)

    print("=== DataStream statistics ===")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(first_batch)

    print("=== DataStream statistics ===")
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    # Extraemos algunos elementos
    numeric = stream._processors[0]
    text = stream._processors[1]
    log = stream._processors[2]

    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()

    print("=== DataStream statistics ===")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
