from exceptions.card_exceptions.card_face_down_error import CardFaceDownError

class Card:
    def __init__(self, card_type: str, value, face_down : bool = True):
        self.card_type = card_type
        self.value = value
        self.face_down = face_down

    def __str__(self) -> str:
        if self.face_down:
            raise CardFaceDownError("La carte est face cachée. Impossible de récupérer la valeur.")
        return f'{self.card_type} - {self.value}'