# For validations Stuff
# we define what is required while requesting or sending data here
# It will be used later in final python coding files for validation

from marshmallow import Schema, fields


class ItemSchema(Schema):
    # dump_only meaning only for returning data
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)