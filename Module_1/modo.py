class Database:
    def __init__(self,connection):
        self.connection = connection
        print(f"To jest 'connection' w obiekcie Database: {self.connection}")
