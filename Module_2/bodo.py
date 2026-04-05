class Database_2:

    global db



    def __init__(self,connection = None):
        self.connection = connection

    def initialize(self,db):

        if db is None:


            db =Database_2(self.connection)
        print (f'funkcja db2 się uruchomiła {db}')
        return db