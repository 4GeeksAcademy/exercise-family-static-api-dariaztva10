
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
# API de una familia:
# Agregar miembros
# Actualizar miembros
# Borrar un miembro
# Obtener un miembro
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
 
    def add_member(self, member):
        #En python, las listas tienen el metodo append
        if not member.get("id"): #si el miembro nuevo no tiene id...
            member["id"] = self._generateId() #...creale un id
        member["last_name"] = self.last_name  # aseguro  que el apellido sea Jackson
        self._members.append(member)
         
        

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        # Si no existe ese miembro:
        return False


    def update_member(self, id, member):
        for family_member in self._members:
            if family_member["id"] == id:
                # Asegúrate de que el nuevo miembro tenga la clave 'id'
                if 'id' not in member:
                    member["id"] = id
                # Elimina el miembro existente
                self._members.remove(family_member)
                # Agrega el miembro actualizado
                self._members.append(member)
                return True
        return False

        

    def get_member(self, id):
        for family_member in self._members:
            if family_member ["id"] == id:
                return family_member
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
