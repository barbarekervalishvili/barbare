from flask import Flask, render_template, request, redirect, url_for

app: Flask = Flask(__name__)

reviews_data = []

# Define role and long_in in the global scope
role = "user"
long_in = True


@app.route('/')
def home():
    course = [
        {"title": "Dagree"},
        {"title": "intermadiate"},
        {"title": "steps"}
    ]
    return render_template("1.html", course=course, role=role, long_in=long_in)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/test')
def abou():
    users = [
        {"name": "barbare", "surname": "kervalishvili"},
        {"name": "dato", "surname": "gagnidze"}
    ]
    return render_template("test.html", users=users)


registered_users = [
    {"Username": "barbare kervalishvili", "Email": "barbarekervalishvili2019@gmail.com", "Password": "12345678"}
]


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']

        if not (username and password and confirm_password and email):
            return "Please fill in all fields"

        if password != confirm_password:
            return "Passwords do not match"

        # Perform validation or store in the database (in real-world scenario)
        registered_users.append({"Username": username, "Email": email, "Password": password})

        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Email: {email}")

        return "Registration Successful"

    # If GET request, render the registration form
    return render_template('registration_form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password match any registered user
        for user in registered_users:
            if user['Username'] == username and user['Password'] == password:
                # Redirect to the home page after successful login
                return redirect(url_for('home'))

        return "Invalid credentials. Please try again."

    return render_template('login.html')


@app.route('/submit_review', methods=['POST'])
def submit_review():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        review_text = request.form.get('review')
        rating = int(request.form.get('rating'))

        # Store review in the dummy list (in a real application, you'd use a database)
        reviews_data.append({'course_name': course_name, 'review': review_text, 'rating': rating})

        return render_template('review_thankyou.html')

    return "Invalid request method."


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
