from Database.database import *
from Interfaces import *

if __name__ == '__main__':
    database = Database()
    database.load_parties()

    interface = Interface(database)
    interface.run_main_interface()
    