import Database
from bson.objectid import ObjectId

import Animal
import Cuidador
import Database
import Habitat


def __init__(self, database, collection):
    self.db = Database(database, collection)

class ZoologicoDao:
    def createAnimal(self, animal: Animal) -> None:
        animal_dict = {
            "id": ObjectId(animal.id),
            "nome": animal.nome,
            "especie": animal.especie,
            "idade": animal.idade,
            "habitat": {
                "id": ObjectId(animal.habitat.id),
                "nome": animal.habitat.nome,
                "tipoAmbiente": animal.habitat.tipoAmbiente,
                "cuidador": {
                    "id": ObjectId(animal.habitat.cuidador.id),
                    "nome": animal.habitat.cuidador.nome,
                    "documento": animal.habitat.cuidador.documento
                }
            }
        }
        self.db.collection.insert_one(animal_dict)


def readAnimal(self, id: str) -> Animal:
    animal_dict = self.db.collection.find_one({"id": id})
    habitat_dict = animal_dict["habitat"]
    cuidador_dict = habitat_dict["cuidador"]
    cuidador = Cuidador(cuidador_dict["id"], cuidador_dict["nome"], cuidador_dict["documento"])
    habitat = Habitat(habitat_dict["id"], habitat_dict["nome"], habitat_dict["tipoAmbiente"], cuidador)
    animal = Animal(animal_dict["id"], animal_dict["nome"], animal_dict["especie"], animal_dict["idade"], habitat)
    return animal


def updateAnimal(self, animal: Animal) -> None:
    animal_dict = {
        "id": animal.id,
        "nome": animal.nome,
        "especie": animal.especie,
        "idade": animal.idade,
        "habitat": {
            "id": animal.habitat.id,
            "nome": animal.habitat.nome,
            "tipoAmbiente": animal.habitat.tipoAmbiente,
            "cuidador": {
                "id": animal.habitat.cuidador.id,
                "nome": animal.habitat.cuidador.nome,
                "documento": animal.habitat.cuidador.documento
            }
        }
    }
    self.db.collection.replace_one({"id": animal.id}, animal_dict)


def deleteAnimal(self, id: str) -> None:
    self.db.collection.delete_one({"id": id})
