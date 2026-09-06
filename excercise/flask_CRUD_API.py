from flask import Flask, jsonify, request

app = Flask(__name__)

books = []
book_id = 1

@app.route('/post', methods=['POST'])
def post_book():
    global book_id
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({"error": 'Valid JSON data require'}), 400

    book = {
        'id': book_id,
        'title': data['title']
    }

    books.append(book)
    book_id += 1

    return jsonify(book), 201

@app.route('/get', methods=['GET'])
def get_book():
    return jsonify(books), 200

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message":"book deleted"}), 200

if __name__ =='__main__':
    app.run(debug=True)


