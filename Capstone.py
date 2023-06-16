
class Database:
    def __init__(self): #does not require 5 positional arguments
        self.host = os.getenv('HOST')
        self.port = os.getenv('PORT')
        self.username = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.database = os.getenv('DATABASE')

def connect(self):
    error = None
    self.connection = None
    self.cursor = None
 
    if self.host and self.port and self.username and self.password and self.database:
        try:
            conn = psycopg2.connect(
            host="containers-us-west-124.railway.app",
            database="railway",
            port=6105,
            user="postgres",
            password="nMph7vIhN07HdLO3PY2c"
            )
            self.cur = conn.cursor()
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                database=self.database
            )

        except:
            print('failed to connect')
def execute_query(self, query): #function to test
    try: 
        self.cursor.execute(query)
        self.connection.commit() #committing changes 
        print('Query executed successfully')
    except: 
        psycopg2.Error
def fetching_results(self):
    return self.cursor.fetchall()


###SQL MEMBER CLASS

class Member: #function of member details
    def __init__(self, name, member_id, borrowed_books):
                                    self.name = name
                                    self.member_id = member_id
                                    self.db = Database(host, port, username, password, database)
                                    self.db.connect() #assign previous values in tuple
                                    self.borrowed_books = [] #list of borrowed books for EACH MEMBER)
                                

    def borrows(self, book):#function for borrowing, book will come from book class
        query = 'INSERT INTO borrowed_books (member_id, book_name, return_date) VALUES (%s, %s, %s)'
        self.db.execute_query(query)

    def returns(self, book):
        return_date = datetime.date.today()
        values = (return_date, self.membership_id, book.id)
        query = 'UPDATE borrowed_books SET return_date = %s WHERE member_id = %s AND book_name = %s VALUES (%s, %s,%s)'
        self.db.execute_query(query, values)
    
    def borrowed_account(self, member_id):
        query = f'SELECT COUNT(*) AS borrowed books FROM borrowed_books WHERE {member_id} GROUP BY {member_id}' 
        self.db.execute_query(query)
        results = self.db.fetch_results()
        return results

database = Database()


