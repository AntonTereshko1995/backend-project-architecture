from flask import Blueprint, current_app, jsonify, request
from src.app.controllers.key_value_controller import KeyValueController

blueprint_key_value = Blueprint("key_value", __name__)

@blueprint_key_value.route("/create/", methods=["POST"])
def create_key_value_blueprint():
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = KeyValueController(logger)
    result = controller.create(input_json)
    return jsonify(result), 201

@blueprint_key_value.route("/get/<string:key>", methods=["GET"])
def get_key_value_blueprint(key):
    logger = current_app.config["logger"]
    controller = KeyValueController(logger)
    result = controller.get(key)
    return jsonify(result), 201

@blueprint_key_value.route("/delete/<string:key>", methods=["DELETE"])
def delete_key_value_blueprint(key):
    logger = current_app.config["logger"]
    controller = KeyValueController(logger)
    result = controller.delete(key)
    return jsonify(result), 201

@blueprint_key_value.route("/update/", methods=["PUT"])
def update_key_value_blueprint():
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = KeyValueController(logger)
    result = controller.update(input_json)
    return jsonify(result), 201