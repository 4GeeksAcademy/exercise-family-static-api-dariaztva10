"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

#Se inicia la app de flask 
app = Flask(__name__)
app.url_map.strict_slashes = False #Nos simplifica el trabajo con los endpoints
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# ENDPOINTS

#* Running on http://127.0.0.1:3000/members
@app.route('/members', methods=['GET']) #Enpoint para OBTENER todos los miembros
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    return jsonify(members), 200
 #LA LINEA DE ARRIBA: jsonificamos (informacion), codigo de status 
    # 404 -> Not found!
    # 200 -> ok
    # 400 -> errores 
    # 500 -> normalmente va a ser un error del servidor(error nuestro o tal vez se cayó el servi, interent, etc  )
     
@app.route('/member', methods=['POST'])  #Enpoint para CREAR
def add_member():
    new_member = request.json
    
    jackson_family.add_member(new_member)
    return jsonify({"done": "Miembro creado exitosamente", "new_member": new_member}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])  #Enpoint para ELIMINAR
def delete_family_member(member_id):
    eliminar_familiar = jackson_family.delete_member(member_id)
    if not eliminar_familiar:
        return jsonify({"msj": "familiar no encontrado"}), 400
    return jsonify({"done": True}), 200
    
@app.route('/member/<int:member_id>', methods=['PUT'])  #Enpoint para ACTUALIZAR
def update_family_member(member_id):
    new_member = request.json
    updated_member = jackson_family.update_member(member_id, new_member)
    if not updated_member: 
        return jsonify({"msj": "familiar  no encontrado"}), 400
    return jsonify({"done": "familiar actualizado"}), 200

@app.route('/member/<int:member_id>', methods=['GET']) #Enpoint para buscar a un solo usuario
def get_one_member(member_id):
    found_member = jackson_family.get_member(member_id)
    if not found_member:
        return jsonify({"msj":"familiar no encontrado"}), 400
    return jsonify(found_member), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
