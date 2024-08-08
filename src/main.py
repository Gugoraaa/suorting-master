from db import Db
from Gui import GUI



DB=Db()
gui=GUI(list=DB.lista(),map=DB.hash_map())
       



gui.loop()


