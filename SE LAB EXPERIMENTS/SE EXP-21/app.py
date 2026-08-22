from flask import Flask, request, redirect

app = Flask(__name__)

todos = ["Learn Flask", "Dockerize Application"]

@app.route("/")
def home():
    items = "".join(f"<li>{todo}</li>" for todo in todos)
    return f"""
    <html>
    <head>
        <title>Flask To-Do List</title>
    </head>
    <body>
        <h1>My To-Do List</h1>
        <form method="POST" action="/add">
            <input name="todo" placeholder="Enter a task" required>
            <button type="submit">Add Task</button>
        </form>
        <ul>{items}</ul>
    </body>
    </html>
    """

@app.route("/add", methods=["POST"])
def add():
    todos.append(request.form["todo"])
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)