from app import db


class ShortcakeUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, index=True, unique=True)
    shortcake_url = db.Column(db.String, index=True, unique=True)
    expiry = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Shortcake {self.shortcake_url}"
