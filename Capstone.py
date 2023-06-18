import psycopg2

import matplotlib.pyplot as plt




class Database:

    def __init__(self, host, port, username, password, database):

        self.host = 'containers-us-west-124.railway.app'

        self.port = 6105

        self.username = 'postgres'

        self.password = 'nMph7vIhN07HdLO3PY2c'

        self.database = 'railway'

        self.connection = None

        self.cursor = None




    def connect(self):

        try:

            self.connection = psycopg2.connect(

                host=self.host,

                port=self.port,

                user=self.username,

                password=self.password,

                database=self.database

            )

            self.cursor = self.connection.cursor()

            print('Connected to the database successfully')

        except psycopg2.Error as e:

            print('Failed to connect to the database:', e)




    def execute_query(self, query):

        try:

            self.cursor.execute(query)

            self.connection.commit()

            print('Query executed successfully')

        except psycopg2.Error as e:

            print('Error executing query:', e)

    def fetch_results(self):

        return self.cursor.fetchall()




# Database connection details

host = "containers-us-west-124.railway.app"

port = 6105

username = "postgres"

password = "nMph7vIhN07HdLO3PY2c"

database = "railway"




# Check if the database exists

def database_exists():

    conn = psycopg2.connect(host=host, port=port, user=username, password=password)

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (database,))

    exists = cur.fetchone()

    cur.close()

    conn.close()

    return exists is not None




def create_database():

    conn = psycopg2.connect(host=host, port=port, user=username, password=password)

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    cur.execute(f"CREATE DATABASE {database}")

    cur.close()

    conn.close()



def create_tables():

    conn = psycopg2.connect(host=host, port=port, user=username, password=password, database=database)

    cur = conn.cursor()


# Create books table

    cur.execute("""

        CREATE TABLE IF NOT EXISTS books (

            id SERIAL PRIMARY KEY,

            title VARCHAR(255) NOT NULL,

            author VARCHAR(255) NOT NULL,

            category VARCHAR(255) NOT NULL

        )

    """)




    # Create members table

    cur.execute("""

        CREATE TABLE IF NOT EXISTS members (

            id SERIAL PRIMARY KEY,

            name VARCHAR(255) NOT NULL

        )

    """)




    # Create borrowed_books table

    cur.execute("""

        CREATE TABLE IF NOT EXISTS borrowed_books (

            id SERIAL PRIMARY KEY,

            member_id INT NOT NULL,

            book_id INT NOT NULL,

            borrowed_date DATE NOT NULL,

            FOREIGN KEY (member_id) REFERENCES members (id),

            FOREIGN KEY (book_id) REFERENCES books (id)

        )

    """)




    conn.commit()

    cur.close()

    conn.close()

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

database = Database(host, port, username, password, database)


###SQL LIBRARY CLASS
class Library:
    def __init__(self, db):
        self.db = db

    def get_most_active_member(self):
        query = 'SELECT member_id FROM borrowed_books GROUP BY {member_id} ORDER BY COUNT(*) DESC LIMIT 1'
        self.db.execute_query(query)
        results = self.db.fetch_results()
        return results
    
    def get_most_borrowed_books(self, borrowed_count):
        name = list(self.name)
        plt.bar(range(len(self.name)), borrowed_count)
        plt.xticks(range(len(self.name)), self.name)
        plt.xlabel('Members of the Library')
        plt.ylabel('Number of Borrowed Books')
        plt.title('Number of Books Borrowed Per Member')
        plt.show()

    def visualize_borrowed_count_per_month(self):

        query = "SELECT EXTRACT(MONTH FROM borrowed_date) AS month, COUNT(*) AS borrowed_count FROM borrowed_books GROUP BY month ORDER BY month"

        self.db.execute_query(query)

        results = self.db.fetch_results()

        months = [result[0] for result in results]

        counts = [result[1] for result in results]




        plt.plot(months, counts, marker='o')

        plt.xlabel("Month")

        plt.ylabel("Number of Books Borrowed")

        plt.title("Number of Books Borrowed per Month")

        plt.show()




    def get_active_members_per_month(self):

        query = "SELECT EXTRACT(MONTH FROM borrowed_date) AS month, COUNT(DISTINCT member_id) AS active_members FROM borrowed_books GROUP BY month ORDER BY month"

        self.db.execute_query(query)

        return self.db.fetch_results()




    def visualize_active_members_per_month(self):

        results = self.get_active_members_per_month()

        months = [result[0] for result in results]

        counts = [result[1] for result in results]




        plt.plot(months, counts, marker='o')

        plt.xlabel("Month")

        plt.ylabel("Number of Active Members")

        plt.title("Number of Active Members per Month")

        plt.show()




    def visualize_borrowed_count_per_category(self):

        query = "SELECT b.category, COUNT(*) AS borrowed_count FROM borrowed_books bb JOIN books b ON bb.book_id = b.id GROUP BY b.category"

        self.db.execute_query(query)

        borrowed_count = self.db.fetch_results()




        categories = [item[0] for item in borrowed_count]

        counts = [item[1] for item in borrowed_count]




        plt.bar(range(len(categories)), counts)

        plt.xticks(range(len(categories)), categories)

        plt.xlabel("Category")

        plt.ylabel("Number of Books Borrowed")

        plt.title("Number of Books Borrowed per Category")

        plt.show()

db = Database(host, port, username, password, database)
db.connect()
library = Library(db)
borrowed_count = [("Member 1", 10), ("Member 2", 5), ("Member 3", 8)]
# Call visualize_borrowed_count method to display the graph


###SQL BOOK CLASS
class Book:
    def __init__(self, title, author, category): 
        self.title = title
        self.author = author
        self.category = category
        self.db = Database()
        self.db.connect()

    def save(self): #saves book into the books database
        query = f'INSERT INTO books (Title, Author, Category) VALUES({self.title},{self.author},{self.category})'
        self.db.execute_query(query)
        results = self.db.fetch_results()
        return results
    

    def get_borrowed_books_per_month(self):
        query = 'SELECT b.title COUNT(*) FROM books b JOIN borrowed_books ON b.id = bb.book_id GROUP BY '

    #def get_active_members_per_month(self):
             

    def get_borrowed_books_per_category(self): #returns number of borrowed books per category
        query = 'SELECT Category COUNT(*) AS borrowed_count FROM books b JOIN borrowed_books bb ON b.id = bb.book_id GROUP BY category'
        self.db.execute_query(query)
        results = self.db.fetch_results()
        return results
    
    def get_top_result_borrowed_books(self): #returns most borrowed bookS
        query = 'SELECT b.title, COUNT(*) AS borrowed_count FROM books b JOIN borrowed_books bb ON b.id = bb.book_id GROUP BY b.title ORDER BY borrowed_count'
        self.db.execute_query(query)
        results = self.db.fetch_results()
        return results
    
    #def get_book_count_top_members(self):
         
    #def get_most_active_member(self):



