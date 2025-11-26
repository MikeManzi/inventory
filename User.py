import csv
class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.__password = password

    @staticmethod
    def login(email, password):
        try:
            with open('users.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['email'] == email and row['password'] == password:
                        return User(row['id'], row['email'], row['password'])
            return None
        except FileNotFoundError:
            print("Error: users.csv file not found")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None