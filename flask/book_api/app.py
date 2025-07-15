from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__) 
api = Api(app) 

BOOKS = []
print(BOOKS)    

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
parser.add_argument('author', type=str, required=True, help='Author cannot be blank') 

class Book(Resource):
    def get(self, book_id):
        book = next((b for b in BOOKS if b['id'] == book_id), None)
        if book is None:
            return {'message': 'Book not found'}, 404
        return book, 200 

class BookList(Resource):
    def get(self):
        return BOOKS, 200
    
    def post(self):
        args = parser.parse_args()
        book_id = len(BOOKS) + 1
        book = {'id': book_id, 'title': args['title'], 'author': args['author']}
        BOOKS.append(book)
        return book, 201 

api.add_resource(BookList, '/books',) 
api.add_resource(Book,  '/books/<int:book_id>/') 

if __name__ == '__main__':
    app.run(debug=True)