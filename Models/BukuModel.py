from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)