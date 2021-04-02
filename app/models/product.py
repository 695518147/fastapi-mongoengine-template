# Standard Library Imports
# None

# 3rd-Party Imports
from mongoengine import StringField, FloatField, Document

# App-Local Imports
# None


class Product(Document):
    name = StringField(unique=True, required=True)
    price = FloatField(required=True)
