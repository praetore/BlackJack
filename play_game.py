from src.Errors import NegativeMoneyError, NotEnoughMoneyError
from src.Game import Game
from src.HumanPlayer import HumanPlayer

__author__ = 'Darryl'


def check_for_bust(game):
    dealer = game.get_dealer()
    player = game.get_player()
    if player.get_hand_value() > 21:
        print("%s busts" % (player.get_name()))
        game.set_result("loss")
        print("Dealer reveals a %s" % dealer.get_hidden())
        dealer.reveal_hidden()
        print("Dealer has a total of %d" % dealer.get_hand_value())


def hit(game):
    deck = game.get_deck()
    player = game.get_player()
    player.receive_card(deck.take_card())
    check_for_bust(game)


def double_down(game):
    deck = game.get_deck()
    player = game.get_player()
    try:
        game.increase_bet(player.place_bet(game.placed_bet()))
        player.receive_card(deck.take_card())
        check_for_bust(game)
        if not game.get_result():
            stay(game)
    except NotEnoughMoneyError as e:
        print(e)


def check_hand(player):
    player.check_hand()
    input("Press a key to continue")


def split(game):
    # TODO: Implement split option
    print("This feature is not yet implemented")


def make_decision(game):
    dealer = game.get_dealer()
    player = game.get_player()
    deck = game.get_deck()
    print("Dealer has a total of %d" % dealer.get_hand_value())
    print("%s has a total of %d" % (player.get_name(), player.get_hand_value()))
    print("What would this player like to do?")
    print("[1] Hit")
    print("[2] Stay")
    print("[3] Split")
    print("[4] Double down")
    print("[5] Check dealer's cards")
    print("[6] Check cards")
    player_action = int(input("Pick an option: "))
    if player_action == 1:
        hit(deck)
    elif player_action == 2:
        stay(game)
    elif player_action == 3:
        split(game)
    elif player_action == 4:
        double_down(game)
    elif player_action == 5:
        check_hand(dealer)
    elif player_action == 6:
        check_hand(player)
    else:
        print("That is not a valid option")


def check_for_blackjack(game):
    dealer = game.get_dealer()
    player = game.get_player()
    if player.get_hand_value() == 21:
        print("%s has Blackjack!" % (player.get_name()))
        stay(game)
    if (dealer.get_hand_value() + dealer.get_hidden().get_value()) == 21:
        print("Dealer has Blackjack!")
        dealer.reveal_hidden()
        stay(game)


def take_bet(game):
    while game.placed_bet() == 0:
        try:
            game.take_bet(game.get_player().increase_bet())
        except (NegativeMoneyError, NotEnoughMoneyError) as e:
            print(e)
        except ValueError:
            print("Please place a valid bet!")


def stay(game):
    dealer = game.get_dealer()
    player = game.get_player()
    print("Dealer reveals a %s" % dealer.get_hidden())
    dealer.reveal_hidden()
    while dealer.get_hand_value() < 17:
        dealer.receive_card(game.get_deck().take_card())
    print("Dealer has a total of %d" % dealer.get_hand_value())
    if dealer.get_hand_value() <= 21:
        if player.get_hand_value() > dealer.get_hand_value():
            print("%s beats the dealer!" % (player.get_name()))
            game.set_result("win")
        elif player.get_hand_value() == dealer.get_hand_value():
            print("%s ties!" % (player.get_name()))
            game.set_result("tie")
        elif player.get_hand_value() < dealer.get_hand_value():
            print("%s lost!" % (player.get_name()))
            game.set_result("loss")
    elif dealer.get_hand_value() > 21:
        print("Dealer busts")
        game.set_result("win")


def receive_payout(game):
    result = game.get_result()
    payout = game.placed_bet()
    player = game.get_player()
    if result == "tie":
        print("Game tied! %s gets $%d bet back." % (player.get_name(), payout))
        player.receive_money(payout)
    elif result == "win":
        if player.get_hand_size() == 2 and player.get_hand_value() == 21:
            payout *= 1.25
        print("%s wins $%d" % (player.get_name(), payout * 2))
        player.receive_money(payout * 2)
    else:
        print("%s loses $%d!" % (player.get_name(), payout))


def deal_cards(game):
    dealer = game.get_dealer()
    deck = game.get_deck()
    player = game.get_player()
    print("Cards are being dealt NOW!")
    dealer.receive_card(deck.take_card())
    dealer.receive_hidden(deck.take_card())
    for i in range(2):
        player.receive_card(deck.take_card())


def run_game(game):
    another = "y"
    player = game.get_player()
    while another == "y" and player.check_money() > 0:
        game.reset()
        take_bet(game)
        deal_cards(game)
        check_for_blackjack(game)
        while not game.get_result():
            make_decision(game)
        receive_payout(game)
        print("%s now has $%d" % (player.get_name(), player.check_money()))
        another = input("Would you like to play another game? (y/n) ")
    if player.check_money() == 0:
        print("%s ran out of money!" % (player.get_name()))
    print("Come back again soon!")


if __name__ == '__main__':
    name = input("What's your name?")
    player = HumanPlayer(name)
    game = Game(player)
    run_game(game)