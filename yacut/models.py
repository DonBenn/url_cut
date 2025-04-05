from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, unique=True, nullable=False)
    short = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def to_dict(self):
        return dict(
            id = self.id,
            original = self.original,
            short = self.short,
            timestamp = self.timestamp
        )

    def from_dict(self, data):
        if 'url' in data:
            setattr(self, 'original', data['url'])
        if 'custom_id' in data:
            setattr(self, 'short', data['custom_id'])