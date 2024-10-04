from Database.database import *
from Interfaces.gui import *

if __name__ == '__main__':
    database = Database()
    database.load_parties()

    for i in database.parties:
        print(i)

    interface = Interface(database)
    interface.run_main_window()