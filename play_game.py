from src.Dealer import Dealer
from src.Deck import Deck
from src.Errors import NegativeMoneyError, NotEnoughMoneyError
from src.HumanPlayer import HumanPlayer

__author__ = 'Darryl'


def game(player):
    # Instantiating objects
    dealer = Dealer()
    deck = Deck()

    player_lost = False
    player_wins = False
    print("You have $%d" % player.check_money())
    # placing bets
    bet = 0
    while bet == 0:
        try:
            bet = player.place_bet()
        except (NegativeMoneyError, NotEnoughMoneyError) as e:
            print(e)
        except ValueError:
            print("Please place a valid bet!")

    # dealing cards
    print("Cards are being dealt NOW!")
    dealer.receive_card(deck.take_card())
    dealer.receive_hidden(deck.take_card())
    for i in range(2):
        player.receive_card(deck.take_card())

    stay = False
    player_has_blackjack = False

    # checking for blackjack
    if player.get_hand_value() == 21:
        print("You have Blackjack!")
        player_has_blackjack = True
        stay = True

    if (dealer.get_hand_value() + dealer.get_hidden().get_value()) == 21:
        print("Dealer has Blackjack!")
        dealer.reveal_hidden()
        stay = True

    # In case win/lose conditions are not met
    while not player_wins and not player_lost:
        # checking for win or lose conditions
        if stay and player.get_hand_value() <= 21:
            while dealer.get_hand_value() < 17:
                dealer.receive_card(deck.take_card())
            print("Dealer has a total of %d" % dealer.get_hand_value())
            if dealer.get_hand_value() <= 21:
                if player.get_hand_value() > dealer.get_hand_value():
                    player_wins = True
                elif player.get_hand_value() == dealer.get_hand_value():
                    player_lost = True
                    player_wins = True
                elif player.get_hand_value() < dealer.get_hand_value():
                    player_lost = True
            elif dealer.get_hand_value() > 21:
                print("Dealer busts")
                player_wins = True
        elif player.get_hand_value() > 21:
            print("You bust")
            player_lost = True
            print("Dealer reveils a %s" % dealer.get_hidden())
            dealer.reveal_hidden()
            print("Dealer has a total of %d" % dealer.get_hand_value())

        # Presenting decisions for player to take
        if not player_lost and not player_wins and not stay:
            print("Dealer has a total of %d" % dealer.get_hand_value())
            print("You have a total of %d" % player.get_hand_value())
            print("What would you like to do?")
            print("[1] Hit")
            print("[2] Stay")
            print("[3] Split")
            print("[4] Double")
            print("[5] Check dealer's cards")
            print("[6] Check your cards")
            player_action = int(input("Pick an option: "))
            if player_action == 1:
                player.receive_card(deck.take_card())
            elif player_action == 2:
                print("Dealer reveils a %s" % dealer.get_hidden())
                dealer.reveal_hidden()
                stay = True
            elif player_action == 3:
                # TODO: Implement split option
                print("This option in not yet implemented")
            elif player_action == 4:
                try:
                    bet += player.place_bet(bet)
                    player.receive_card(deck.take_card())
                    stay = True
                except NotEnoughMoneyError as e:
                    print(e)
            elif player_action == 5:
                dealer.check_hand()
                input("Press a key to continue")
            elif player_action == 6:
                player.check_hand()
                input("Press a key to continue")
            else:
                print("That is not a valid option")

    if player_wins and player_lost:
        print("Game tied! Getting $%d bet back." % bet)
        player.receive_money(bet)
    elif player_wins:
        if player_has_blackjack:
            bet *= 1.25
        print("You win $%d" % (bet*2))
        player.receive_money(bet*2)
    else:
        print("You lose $%d!" % bet)

    print("You now have $%d" % player.check_money())
    player.clear_hand()


if __name__ == '__main__':
    player = HumanPlayer()
    player.receive_money(100)
    game(player)
    another = "y"
    while another == "y" and player.check_money() > 0:
        another = input("Would you like to play another game? (y/n) ")
        if another == "y":
            game(player)

    if player.check_money() == 0:
        print("You ran out of money!")
    print("Come back again soon!")