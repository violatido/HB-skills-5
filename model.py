"""Skills 5: SQLAlchemy & AJAX

Part 1: Define Model Classes
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Human(db.Model):
    """Data model for a human."""
    __tablename__ = 'humans'

    human_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """ Show Human Info """
        return f'<Human human_id={self.human_id} fname={self.fname}>'


class Animal(db.Model):
    """Data model for an animal."""
    __tablename__ = 'animals'

    animal_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)

    human = db.relationship("Human", backref="animals")

    def __repr__(self):
        """ Show Animal Info """
        return f'<Animal animal_id={self.animal_id} name={self.name}>'

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
