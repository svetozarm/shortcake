from flask import render_template, flash, redirect, url_for, request

from app import app
from app.shortcake import get_short
from app.forms import UrlForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    url_form = UrlForm()
    if url_form.validate_on_submit():
        flash(f"Submitted url: {url_form.url.data}")
        url = {"link": url_form.url.data}
        return redirect(url_for("shorten"), url=url)
    return render_template("index.html", form=url_form)


@app.route("/shorten.html", methods=["POST"])
def shorten():
    url_form = UrlForm(request.form)
    if url_form.validate():
        url = {
            "link": url_form.url.data,
            "shortened": get_short(url_form.url.data).shortcake_url,
        }
        return render_template("shorten.html", url=url)
    else:
        return render_template("index.html", form=url_form)
