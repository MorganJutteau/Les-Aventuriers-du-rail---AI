from card.card import Card
from card.destination_card import DestinationCard
from card.transport_card import TransportCard 

##########################################################################################################
#                            ___              _   _            _                                         #
#                           / __\__ _ _ __ __| | | |_ ___  ___| |_                                       #
#                          / /  / _` | '__/ _` | | __/ _ \/ __| __|                                      #
#                         / /__| (_| | | | (_| | | ||  __/\__ \ |_                                       #
#                         \____/\__,_|_|  \__,_|  \__\___||___/\__|                                      #
#                                                                                                        #
##########################################################################################################

# Créer une carte normale ( peu utile de créer une carte directement avec ce constructeur )
normal_card = Card(card_type="Transport", value="Blue", face_down=False)
print(normal_card)

# Créer une carte de destination
destination_card = DestinationCard(origin="Paris", destination="Madrid", face_down=False)
print("Carte de destination:", destination_card)

# Créer une carte de transport
transport_card = TransportCard(color="Red",face_down = False)
print("Carte de transport:", transport_card)

# Tester une exception pour une carte face cachée
face_down_card = TransportCard(color="Blue")
print(face_down_card)


