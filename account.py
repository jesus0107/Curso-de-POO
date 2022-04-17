from pydoc import doc
from xml.dom.minidom import Document


class Account:
  id = int
  name = str
  document = str
  email = str
  password = str
  
  def __init__(self, id = 0, name = "", document = "", email = "", password = ""):
    self.id = id
    self.name = name
    self.document = document
    self.email = email
    self.password = password