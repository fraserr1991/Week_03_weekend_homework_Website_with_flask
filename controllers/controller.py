from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book, delete_book_at_index
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_event():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  checked_out = True if 'checked_out' in request.form else False
  new_book = Book(title =  title, author = author, genre = genre, checked_out = checked_out)
  add_new_book(new_book)
  return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
  delete_book_at_index(index)
  return redirect('/books')

@app.route('/books/show/<index>')
def individual_book(index):
    book = books[int(index)]
    return render_template('show_book.html', title='Individual book', book=book)

