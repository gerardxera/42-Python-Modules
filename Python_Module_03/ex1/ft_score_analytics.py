#!/usr/bin/python3
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        scores: list[int] = []
        for arg in sys.argv[1:]:
            try:
                scores += [int(arg)]
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(scores) == 0:
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
            return
        print(f"Scores processed: {scores}")
        total_players = len(scores)
        print(f"Total players: {total_players}")
        total_score = sum(scores)
        print(f"Total score: {total_score}")
        average_score = total_score / total_players
        print(f"Average score: {average_score}")
        high_score = max(scores)
        print(f"High score: {high_score}")
        low_score = min(scores)
        print(f"Low score: {low_score}")
        score_range = high_score - low_score
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
