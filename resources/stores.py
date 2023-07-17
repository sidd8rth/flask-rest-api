import uuid
from flask.views import MethodView
from flask import Flask, request
from flask_smorest import abort, Blueprint
from db import stores

blp = Blueprint("Stores",__name__, description="Stores information")


@blp.route("/store")
class StoreList(MethodView):

    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400, message="Ensure, name is included in json payload")

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store Already Exist")

        store_id = uuid.uuid4().hex
        # it changes the form of data is required format **
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201


@blp.route("/store/<string:store_id>")
class Store(MethodView):

    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")