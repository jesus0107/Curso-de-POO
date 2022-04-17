from payment import Pyment

class CardPayment(Pyment):
  __number_card: int
  __card_expiration: int
  __cvv: int
  
  def __init__(self, number_card, card_expiration, cvv):
    self.__number_card = number_card
    self.__card_expiration = card_expiration
    self.__cvv = cvv
  
   
  