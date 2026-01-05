from datetime import datetime
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = Path(__file__).parent
DATABASE_PATH = BASE_DIR / "financial.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False, default="USD")
    acquired_on = db.Column(db.Date, nullable=True)


class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    asset_class = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False, default="USD")
    invested_on = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)


@app.before_request
def create_tables():
    db.create_all()


@app.route("/")
def index():
    assets = Asset.query.all()
    investments = Investment.query.all()
    total_assets = sum(asset.value for asset in assets)
    total_investments = sum(inv.amount for inv in investments)
    return render_template(
        "index.html",
        assets=assets,
        investments=investments,
        total_assets=total_assets,
        total_investments=total_investments,
    )


@app.route("/assets", methods=["GET", "POST"])
def manage_assets():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        value = float(request.form.get("value", 0))
        currency = request.form.get("currency", "USD").strip() or "USD"
        acquired_on_raw = request.form.get("acquired_on") or None
        acquired_on = (
            datetime.strptime(acquired_on_raw, "%Y-%m-%d").date()
            if acquired_on_raw
            else None
        )

        if name and category and value:
            asset = Asset(
                name=name,
                category=category,
                value=value,
                currency=currency,
                acquired_on=acquired_on,
            )
            db.session.add(asset)
            db.session.commit()
        return redirect(url_for("manage_assets"))

    assets = Asset.query.order_by(Asset.acquired_on.desc().nullslast()).all()
    return render_template("assets.html", assets=assets)


@app.route("/investments", methods=["GET", "POST"])
def manage_investments():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        asset_class = request.form.get("asset_class", "").strip()
        amount = float(request.form.get("amount", 0))
        currency = request.form.get("currency", "USD").strip() or "USD"
        invested_on_raw = request.form.get("invested_on") or None
        invested_on = (
            datetime.strptime(invested_on_raw, "%Y-%m-%d").date()
            if invested_on_raw
            else None
        )
        notes = request.form.get("notes")

        if name and asset_class and amount:
            investment = Investment(
                name=name,
                asset_class=asset_class,
                amount=amount,
                currency=currency,
                invested_on=invested_on,
                notes=notes,
            )
            db.session.add(investment)
            db.session.commit()
        return redirect(url_for("manage_investments"))

    investments = Investment.query.order_by(
        Investment.invested_on.desc().nullslast()
    ).all()
    return render_template("investments.html", investments=investments)


if __name__ == "__main__":
    app.run(debug=True)
