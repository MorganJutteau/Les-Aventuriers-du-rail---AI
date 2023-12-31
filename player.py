from abc import abstractmethod


class Player:
    @abstractmethod
    def get_action(self, player_input):
        pass

    @abstractmethod
    def choose_destination_card(self, destination_cards):
        pass
