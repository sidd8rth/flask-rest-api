import uuid
from flask.views import MethodView
from flask import Flask, request
from flask_smorest import abort, Blueprint
from db import items


blp = Blueprint("Items",__name__, description="Items information")

@blp.route("/item")
class ItemList(MethodView):

    def get(self):
        return {"items": list(items.values())}

    def post(self):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data or "store_id" not in item_data:
            abort(400, message="Ensure, price, name and store_id included in json payload")

        for item in items.values():
            if item_data["name"] == item["name"] or item_data["store_id"] == items["store_id"]:
                abort(400, message="Item Already Exist")

        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201

@blp.route("/item/<string:item_id>")
class Item(MethodView):

    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")

    def put(self, item_id):
        item_data = request.get_json()

        if "price" not in item_data or "name" not in item_data:
            abort(404, message="Bad request, ensure all info is there in payload")

        try:
            item = items[item_id]
            # dictionary inplace update method
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found")