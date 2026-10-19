
import random
from collections import Counter

# Rock, Paper, Scissors
CHOICES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}

# Each move beats the move mapped to it.
WINNING_MOVES = {
    1: 3,  # Rock beats Scissors
    2: 1,  # Paper beats Rock
    3: 2,  # Scissors beats Paper
}

# Persistent statistics for the current program session.
SESSION_STATS = {
    "matches_played": 0,
    "matches_won": 0,
    "matches_lost": 0,
    "matches_drawn": 0,
    "rounds_won": 0,
    "rounds_lost": 0,
    "rounds_drawn": 0,
}


def get_number(prompt, valid_options):
    """Ask for a valid numeric menu option."""
    while True:
        answer = input(prompt).strip()

        if answer.isdigit() and int(answer) in valid_options:
            return int(answer)

        print("Invalid option. Please try again.")


def get_player_name(prompt):
    """Ask for a non-empty player name."""
    while True:
        name = input(prompt).strip()

        if name:
            return name

        print("Name cannot be empty. Please try again.")


def get_move(player_name):
    """Get a valid move, or None if the player quits."""
    while True:
        print("\nChoose your move:")
        for number, move in CHOICES.items():
            print(f"  {number}. {move}")
        print("  Q. Return to main menu")

        answer = input(f"{player_name}, your choice: ").strip().lower()

        if answer == "q":
            return None

        if answer in ("1", "2", "3"):
            return int(answer)

        print("Invalid input. Enter 1, 2, 3 or Q.")


def determine_winner(move1, move2):
    """Return 0 for a draw, 1 if player 1 wins, or 2 if player 2 wins."""
    if move1 == move2:
        return 0

    if WINNING_MOVES[move1] == move2:
        return 1

    return 2


def get_computer_move(player_history):
    """
    Choose a move based on the player's previous moves.

    The computer predicts the player's most common move and counters it.
    With limited history, it uses a random move.
    """
    if len(player_history) < 2:
        return random.choice(list(CHOICES.keys()))

    move_counts = Counter(player_history)
    most_common_count = max(move_counts.values())

    # Randomly choose among tied most-common moves.
    most_common_moves = [
        move
        for move, count in move_counts.items()
        if count == most_common_count
    ]
    predicted_player_move = random.choice(most_common_moves)

    # The move that beats the predicted player move.
    counter_move = next(
        move
        for move, beaten_move in WINNING_MOVES.items()
        if beaten_move == predicted_player_move
    )

    # Add some unpredictability instead of always following the prediction.
    if random.random() < 0.80:
        return counter_move

    return random.choice(list(CHOICES.keys()))


def display_score(player1, player2, score1, score2, draws):
    """Display the current match score."""
    print("\n" + "-" * 42)
    print("MATCH SCORE")
    print(f"{player1}: {score1}  |  {player2}: {score2}")
    print(f"Drawn rounds: {draws}")
    print("-" * 42)


def display_session_stats():
    """Display statistics accumulated during this program session."""
    print("\n" + "=" * 42)
    print("SESSION STATISTICS")
    print("=" * 42)
    print(f"Matches completed: {SESSION_STATS['matches_played']}")
    print(f"Matches won:       {SESSION_STATS['matches_won']}")
    print(f"Matches lost:      {SESSION_STATS['matches_lost']}")
    print(f"Matches drawn:     {SESSION_STATS['matches_drawn']}")
    print("-" * 42)
    print(f"Rounds won:        {SESSION_STATS['rounds_won']}")
    print(f"Rounds lost:       {SESSION_STATS['rounds_lost']}")
    print(f"Rounds drawn:      {SESSION_STATS['rounds_drawn']}")
    print("=" * 42)


def record_match_result(result):
    """Record a completed match in the session statistics."""
    SESSION_STATS["matches_played"] += 1

    if result == "won":
        SESSION_STATS["matches_won"] += 1
    elif result == "lost":
        SESSION_STATS["matches_lost"] += 1
    else:
        SESSION_STATS["matches_drawn"] += 1


def play_round(
    player1,
    player2,
    vs_computer,
    player_history,
    score,
    round_draws,
):
    """
    Play one round.

    Return updated scores and True if the round was completed.
    Return None as the first result if the player quits.
    """
    move1 = get_move(player1)

    if move1 is None:
        return None, score, round_draws

    if vs_computer:
        move2 = get_computer_move(player_history)
        print(f"\n{player2} chose: {CHOICES[move2]}")
    else:
        print(f"\nIt's {player2}'s turn.")
        move2 = get_move(player2)

        if move2 is None:
            return None, score, round_draws

    # Store the human player's move for future computer predictions.
    player_history.append(move1)

    print("\n" + "=" * 42)
    print(f"{player1}: {CHOICES[move1]}")
    print(f"{player2}: {CHOICES[move2]}")

    winner = determine_winner(move1, move2)

    if winner == 0:
        print("Round result: Draw!")
        round_draws += 1
        SESSION_STATS["rounds_drawn"] += 1

    elif winner == 1:
        print(f"Round winner: {player1}!")
        score[0] += 1
        SESSION_STATS["rounds_won"] += 1

    else:
        print(f"Round winner: {player2}!")
        score[1] += 1
        SESSION_STATS["rounds_lost"] += 1

    print("=" * 42)
    display_score(player1, player2, score[0], score[1], round_draws)

    return True, score, round_draws


def play_match(vs_computer, best_of):
    """Play a Best of 3 or Best of 5 match."""
    print("\n" + "=" * 42)
    print("ROCK, PAPER, SCISSORS")
    print(f"BEST OF {best_of}")
    print("=" * 42)

    player1 = get_player_name("Enter your name: ")

    if vs_computer:
        player2 = "Computer"
        print("\nThe computer will learn from your previous moves.")
    else:
        player2 = get_player_name("Enter player 2's name: ")

    target_wins = best_of // 2 + 1
    score = [0, 0]
    round_draws = 0
    player_history = []

    while score[0] < target_wins and score[1] < target_wins:
        completed, score, round_draws = play_round(
            player1,
            player2,
            vs_computer,
            player_history,
            score,
            round_draws,
        )

        if completed is None:
            print("\nMatch cancelled. Returning to the main menu.")
            return

    print("\n" + "=" * 42)
    print("MATCH RESULTS")
    print("=" * 42)
    print(f"Rounds played: {sum(score) + round_draws}")
    print(f"{player1}: {score[0]} round wins")
    print(f"{player2}: {score[1]} round wins")
    print(f"Draws: {round_draws}")

    if score[0] > score[1]:
        print(f"\nMatch winner: {player1}!")
        result = "won"
    elif score[1] > score[0]:
        print(f"\nMatch winner: {player2}!")
        result = "lost"
    else:
        # Normally unreachable in Best of 3/5, but safe to handle.
        print("\nThe match ended in a draw!")
        result = "drawn"

    record_match_result(result)
    print("=" * 42)


def main():
    """Run the main menu."""
    while True:
        print("\n" + "=" * 42)
        print("ROCK, PAPER, SCISSORS")
        print("=" * 42)
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. View session statistics")
        print("4. Exit")

        choice = get_number("Select an option: ", {1, 2, 3, 4})

        if choice in (1, 2):
            print("\nChoose match format:")
            print("1. Best of 3 (first to 2 wins)")
            print("2. Best of 5 (first to 3 wins)")

            format_choice = get_number("Select a format: ", {1, 2})
            best_of = 3 if format_choice == 1 else 5

            play_match(
                vs_computer=(choice == 2),
                best_of=best_of,
            )

        elif choice == 3:
            display_session_stats()

        elif choice == 4:
            display_session_stats()
            print("\nThanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
