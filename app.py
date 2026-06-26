from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Skills Page
@app.route("/skills")
def skills():
    return render_template("skills.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)