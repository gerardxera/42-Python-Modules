#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    """Abstract base class for data processing."""

    def __init__(self) -> None:
        self._stored_data: list[str] = []
        self._counter_rank: int = 0
        self.total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validates whether the data can be processed."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingest the data if it is valid; otherwise, throw an exception."""
        pass

    def output(self) -> tuple[int, str]:
        """Extracts and returns (range, data) from the oldest element."""

        if not self._stored_data:
            raise ValueError("No data to extract")

        value: str = self._stored_data.pop(0)  # pop(0) Saca pimer elemento
        rank = self._counter_rank
        self._counter_rank += 1
        return rank, value


class NumericProcessor(DataProcessor):
    """Numeric data processor."""

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
    """Text processor."""

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
    """Log record processor."""

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


class ExportPlugin(Protocol):
    "Protocol that defines the contract for export plugins."

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Receives a list of tuples (rank, value) and exports them."""


class DataStream:
    """Manages and routes heterogeneous data flows using polymorphism."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """A new processor is registered in the stream."""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Route each element to the appropriate processor for validation."""
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
        """Displays processing statistics for each processor."""
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Drain up to 'nb' elements per processor and send them to the plugin.
        """
        for proces in self._processors:
            extracted: list[tuple[int, str]] = []

            # Sacar los nb elemenntos si hay
            for i in range(nb):
                try:
                    rank, value = proces.output()
                    extracted.append((rank, value))
                except ValueError:
                    # No quedan datos en este proceso y da error
                    break

            # Si hemos sacado algo, se lo pasamos eel pluguin
            if extracted:
                plugin.process_output(extracted)


class CSVExportPlugin:
    """Plugin to export data in CSV format."""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        csv_line = ",".join(values)
        print(f"CSV Output: {csv_line}")


class JSONExportPlugin:
    """Plugin to export data in JSON format."""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [f'"item_{rank}": "{value}"' for rank, value in data]
        json_line = "{" + ", ".join(items) + "}"
        print(f"JSON Output: {json_line}")


def main() -> None:
    """Main function for testing the data pipeline."""
    print("=== Code Nexus - Data Pipeline ===\n")
    stream = DataStream()

    print("Initialize Data Stream...\n")
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        {"log_level": "WARNING", "log_message":
         "Telnet access! Use ssh instead"},
        {"log_level": "INFO", "log_message": "User wil is connected"},
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)

    print("\n=== DataStream statistics ===")
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    print("\n=== DataStream statistics ===")
    stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        {"log_level": "ERROR", "log_message": "500 server crash"},
        {"log_level": "NOTICE", "log_message":
         "Certificate expires in 10 days"},
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {second_batch}")
    stream.process_stream(second_batch)

    print("\n=== DataStream statistics ===")
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)

    print("\n=== DataStream statistics ===")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
