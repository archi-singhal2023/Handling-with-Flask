from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "my-secret-key"


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            flash("Name cannot be empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name}, your feedback was saved.")
        return render_template("thankyou.html", name=name)
    return render_template("form.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

