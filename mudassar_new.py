import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@db:5432/mudassar"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/", methods=["GET"])
def index():
    count = Message.query.count()
    return jsonify({"message": "Welcome to Mudassar Project", "messages": count})


@app.route("/messages", methods=["GET"])
def get_messages():
    messages = Message.query.order_by(Message.id).all()
    return jsonify([{"id": m.id, "text": m.text} for m in messages])


@app.route("/messages", methods=["POST"])
def post_message():
    data = request.get_json(silent=True) or {}
    text = data.get("text")
    if not text:
        return jsonify({"error": "Missing text field"}), 400

    message = Message(text=text)
    db.session.add(message)
    db.session.commit()
    return jsonify({"id": message.id, "text": message.text}), 201


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
