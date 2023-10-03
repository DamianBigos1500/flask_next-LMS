from marshmallow import Schema, fields

class RegisterSchema(Schema):
  name = fields.Str(required=True)