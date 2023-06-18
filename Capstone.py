
from dotenv import load_dotenv
import os
import matplotlib as plt
import datetime
import psycopg2
from faker import Faker
import random
from tqdm import tqdm


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
    self.cur = None ### I changed self.cursor to self.cur
 
    if self.host and self.port and self.username and self.password and self.database: #if all these attributes arent none...
        try:  #tries to get connnection to railway database
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

        except: #if no connection, prints error message
            print('failed to connect')
def execute_query(self, query): #function to execute queries
    try: 
        self.cur.execute(query) ###I changed self.cursor to self.cur
        self.connection.commit() #committing changes 
        print('Query executed successfully')
    except: 
        psycopg2.Error
def fetching_results(self):
    return self.cur.fetchall()


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


###SQL LIBRARY CLASS
class Library:
    def __init__(self):
        self.database = Database()
        self.database.connect() #connect to railway database

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


db = Database(host, port, username, password, database)
db.connect()
library = Library(db)
borrowed_count = [("Member 1", 10), ("Member 2", 5), ("Member 3", 8)]
# Call visualize_borrowed_count method to display the graph
library.visualize_borrowed_count(borrowed_count)


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
        query = SELECT b.title COUNT(*) FROM books b JOIN           

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



