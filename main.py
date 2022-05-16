from game import Game
from context import GameContext


class Context(GameContext):
    """Responsible for handling interaction with the game UI."""

    def __init__(self):
        self.game = Game(self)


def main():
    context = Context()
    context.game = Game(context)
    context.game.Start(context).start()
    context.game = None


if __name__ == "__main__":
    main()
