import json

from app.models import db


class CustomFormTranslates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    custom_form_id = db.Column(
        db.Integer, db.ForeignKey('custom_forms.id', ondelete='CASCADE')
    )
    custom_form = db.relationship('CustomForms', backref='custom_form_translate', foreign_keys=[custom_form_id])
    language_code = db.Column(db.String, nullable=False)
    form_id = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<CustomFormTranslate %r>' % self.id
    
    def convert_to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'language_code': self.language_code,
            'form_id': self.form_id
        }
        