# imported Flask, render_template, request, redirect, url_for class from flask module
from flask import Flask, render_template, request, redirect, url_for

# created an instance of Flask class
app = Flask(__name__)

# created a list to store all the books
all_books = []

# route decorator to tell Flask what URL should trigger the function
@app.route('/')
def home():
    return render_template("index.html", books=all_books)

# route decorator to tell Flask what URL should trigger the function
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        # get the data from the form
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        # create a dictionary to store the data
        book = {
            'title': title,
            'author': author,
            'rating': rating
        }

        # append the book to the list
        all_books.append(book)

        # redirect to the home page
        return redirect(url_for('home'))
    return render_template("add.html")

# checks if name of the function is main and run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

