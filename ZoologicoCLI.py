from Database import Database
from ZologicoDAO import ZoologicoDao
from typing import List
from Animal import Animal
from Habitat import Habitat
from Cuidador import Cuidador


class ZoologicoCLI:
    def __init__(self):
        self.db = Database(database="my_database", collection="my_collection")
        self.dao = ZoologicoDao()


    def menu(self) -> None:
        while True:
            print("--------Bem vindo ao Zoologico-------")
            print("1 - Criar animal")
            print("2 - Ler animal")
            print("3 - Atualizar animal")
            print("4 - Deletar animal")
            print("0 - Sair")
            opcao = input("Digite a opção desejada: ")
            if opcao == "1":
                self.createAnimal()
            elif opcao == "2":
                self.readAnimal()
            elif opcao == "3":
                self.updateAnimal()
            elif opcao == "4":
                self.deleteAnimal()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def createAnimal(self):
        # Cria um objeto do tipo Cuidador
        print("Criar novo cuidador:")
        id_cuidador = input("ID: ")
        nome_cuidador = input("Nome: ")
        documento_cuidador = input("Documento: ")
        cuidador = Cuidador(id_cuidador, nome_cuidador, documento_cuidador)

        # Cria um ou mais objetos do tipo Habitat
        habitats: List[Habitat] = []
        while True:
            print("Criar novo habitat:")
            id_habitat = input("ID: ")
            nome_habitat = input("Nome: ")
            tipo_ambiente = input("Tipo de ambiente: ")
            id_cuidador_habitat = input("ID do cuidador responsável: ")
            habitat = Habitat(id_habitat, nome_habitat, tipo_ambiente, id_cuidador_habitat)
            habitats.append(habitat)
            resposta = input("Deseja criar mais habitats? (s/n): ")
            if resposta.lower() == "n":
                break

        # Cria um objeto do tipo Animal
        print("Criar novo animal:")
        id_animal = input("ID: ")
        nome_animal = input("Nome: ")
        especie_animal = input("Espécie: ")
        idade_animal = int(input("Idade: "))
        id_habitat_animal = input("ID do habitat: ")
        animal = Animal(id_animal, nome_animal, especie_animal, idade_animal, id_habitat_animal)
        # Chama o método createAnimal do ZoologicoDAO para criar o animal no banco de dados
        self.dao.createAnimal(animal)
        print("Animal criado com sucesso!")

    def readAnimal(self):
            animal_id = input("Digite o ID do animal: ")
            animal = self.dao.readAnimal(animal_id)
            if animal:
                print(f"ID: {animal.id}")
                print(f"Nome: {animal.nome}")
                print(f"Espécie: {animal.especie}")
                print(f"Idade: {animal.idade}")
                print(f"Habitat: {animal.habitat.nome}")
                print(f"Cuidador: {animal.habitat.cuidador.nome}")
            else:
                print("Animal não encontrado!")
    def updateAnimal(self):
        animal_id = input("Digite o ID do animal que deseja atualizar: ")
        animal = self.dao.readAnimal(animal_id)
        if animal:
            # Coletar novos dados do animal
            novo_nome = input("Digite o novo nome do animal: ")
            nova_especie = input("Digite a nova espécie do animal: ")
            nova_idade = int(input("Digite a nova idade do animal: "))

            # Atualizar os dados do animal
            animal.nome = novo_nome
            animal.especie = nova_especie
            animal.idade = nova_idade

            # Salvar as atualizações no banco de dados
            self.dao.updateAnimal(animal)

            print("Animal atualizado com sucesso!")
        else:
            print("Animal não encontrado!")

    def deleteAnimal(self):
        animal_id = input("Digite o ID do animal que deseja deletar: ")
        animal = self.dao.readAnimal(animal_id)
        if animal:
            self.dao.deleteAnimal(animal_id)
            print("Animal deletado com sucesso!")
        else:
            print("Animal não encontrado!")




if __name__ == "__main__":
    cli = ZoologicoCLI()
    cli.menu()

