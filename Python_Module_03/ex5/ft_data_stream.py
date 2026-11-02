#!/usr/bin/python3
import random
from typing import Generator


PLAYER: tuple[str, ...] = (
    "alice",
    "bob",
    "charlie",
    "dylan",
)


ACTIONS: tuple[str, ...] = (
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release",
)


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYER)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield (event)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    group = gen_event()

    for i in range(1000):
        player, action = next(group)
        print(f"Event {i}: Player {player} did action {action}")

    events_list: list[tuple[str, str]] = []
    for i in range(10):
        events_list.append(next(group))
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
