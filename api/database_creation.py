class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    user_email = db.Column(db.String(20), nullable=False)

class prak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(800))