import base64

from Game import Game

def parse_deck(deck_base64):
    # Decode the base64 string
    decoded_bytes = base64.b64decode(deck_base64)

    # Convert bytes to string (assuming it's UTF-8 encoded)
    decoded_string = decoded_bytes.decode('utf8')

    # Split the string into a list of cards
    cards = decoded_string.split('|')

    deck = []

    for card in cards[:-1]:
        name = card.split('$')[0]
        full_name = name.replace("_", " - ")

        count = card.split('$')[1]

        deck.append((full_name, int(count)))

    return deck

def get_decks():
    # Ask for player deck 1
    print("Please input deck 1")
    # input = input()
    # load input from file deck_input.txt
    with open('./src/deck_input.txt', 'r') as file:
        input = file.readline()
    deck1 = parse_deck(input)
    # print(deck1)

    # Ask for player deck 2
    print("Please input deck 2")
    # input = input()
    deck2 = parse_deck(input)
    # print(deck2)

    return deck1, deck2


def main():
    decks = get_decks()

    game = Game(decks[0], decks[1])

    winner = game.check_winner()

    while not winner:
        game.print_state()
        game.active_player.print_state()

        if game.active_player == game.player2:
            print("Using random AI")
            game.do_random_command()
        else:
            print("Input command:")
            command = input()
            game.do_command(int(command))

        winner = game.check_winner()

    print("Game over")
    print(winner.name + " wins!")

# Run the game
if __name__ == "__main__":
    main()