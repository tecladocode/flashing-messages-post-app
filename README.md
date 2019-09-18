# Flashing messages

This short code repository contains a Flask application that uses render_template to show some HTML.

It is used in our blog post, "Flashing messages with Flask". Read that for more info!

In that blog post, we add some code to the app. You can see the final code by going to the branch `end`.

## Installing

You'll need `flask` to run this code sample. Install it like so:

```
pipenv install flask
```

## Running the app

To run this app, enter the Pipenv shell and run the app via the Flask CLI. Make sure you're in the correct directory first:

```
pipenv run flask run
```

## The routes

We have two endpoints in this starter app: `home`, and `profile`.

At the moment these only return HTML pages (from the `templates` folder). In the blog post we modify one of them to flash a message, as well as the corresponding endpoint to show the flashed messages.

```python
@app.route("/")
def home():
    return render_template("home.jinja2")


@app.route("/profile")
def profile():
    return render_template("profile.jinja2")
```
