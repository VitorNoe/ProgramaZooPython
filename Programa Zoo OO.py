class Animal:
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, vizinhos=None):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.horas_alimentacao = horas_alimentacao
        self.vizinhos = vizinhos if vizinhos else []

    def acao_barulho(self):
        return f"{self.nome} faz {self.barulho}!"

    def acao_movimento(self):
        return f"{self.nome} se move {self.movimento}."

    def exibir_info(self):
        info = f"Nome: {self.nome}\nIdade: {self.idade} anos\nBarulho: {self.barulho}\n"
        info += f"Movimento: {self.movimento}\nAlimentação: {self.alimentacao}\n"
        info += f"Habitat: {self.habitat}\nHorário de Alimentação: {self.horas_alimentacao}\n"
        if self.vizinhos:
            info += f"Vizinhos: {', '.join(self.vizinhos)}\n"
        return info

class Mamifero(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, tipo_pelo, vizinhos=None):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, vizinhos)
        self.tipo_pelo = tipo_pelo

    def exibir_info(self):
        info = super().exibir_info()
        info += f"Tipo de Pelo: {self.tipo_pelo}\n"
        return info

class Ave(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, envergadura, vizinhos=None):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, vizinhos)
        self.envergadura = envergadura

    def exibir_info(self):
        info = super().exibir_info()
        info += f"Envergadura: {self.envergadura} metros\n"
        return info

class Reptil(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, tipo_pele, vizinhos=None):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, vizinhos)
        self.tipo_pele = tipo_pele

    def exibir_info(self):
        info = super().exibir_info()
        info += f"Tipo de Pele: {self.tipo_pele}\n"
        return info

class Zoologico:
    def __init__(self):
        self.animais = []

    def cadastrar_animal(self, animal):
        if len(animal.vizinhos) > 2:
            raise ValueError("O número de vizinhos não pode ser maior que 2.")
        self.animais.append(animal)

    def listar_todos_animais(self):
        if not self.animais:
            print("Nenhum animal cadastrado.")
        for animal in self.animais:
            print(f"- {animal.nome}")

    def buscar_animal(self, nome):
        for animal in self.animais:
            if animal.nome.lower() == nome.lower():
                print(animal.exibir_info())
                return
        print(f"Animal '{nome}' não encontrado.")

    def listar_animais_por_categoria(self, categoria):
        categoria = categoria.lower()
        categorias = {
            'mamífero': Mamifero,
            'ave': Ave,
            'réptil': Reptil
        }
        if categoria not in categorias:
            print("Categoria inválida.")
            return

        encontrados = [animal for animal in self.animais if isinstance(animal, categorias[categoria])]
        if not encontrados:
            print(f"Nenhum animal da categoria '{categoria}' encontrado.")
        else:
            for animal in encontrados:
                print(f"- {animal.nome}")

def menu():
    zoologico = Zoologico()

    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar novo animal")
        print("2. Listar todos os animais")
        print("3. Buscar animal por nome")
        print("4. Listar animais por categoria")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tipo = input("Digite o tipo de animal (Mamífero, Ave, Réptil): ").strip().lower()
            nome = input("Nome: ").strip()
            idade = int(input("Idade: "))
            barulho = input("Som característico: ").strip()
            movimento = input("Forma de locomoção: ").strip()
            alimentacao = input("Dieta: ").strip()
            habitat = input("Habitat natural: ").strip()
            horas_alimentacao = input("Horário de alimentação: ").strip()
            vizinhos = input("Nomes dos vizinhos (máximo 2, separados por vírgula): ").strip().split(',')

            if tipo == 'mamífero':
                tipo_pelo = input("Tipo de pelo: ").strip()
                animal = Mamifero(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, tipo_pelo, vizinhos)
            elif tipo == 'ave':
                envergadura = float(input("Envergadura (em metros): "))
                animal = Ave(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, envergadura, vizinhos)
            elif tipo == 'réptil':
                tipo_pele = input("Tipo de pele: ").strip()
                animal = Reptil(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, tipo_pele, vizinhos)
            else:
                print("Tipo de animal inválido.")
                continue
            
            zoologico.cadastrar_animal(animal)
            print(f"Animal '{nome}' cadastrado com sucesso.")

        elif opcao == '2':
            zoologico.listar_todos_animais()

        elif opcao == '3':
            nome = input("Digite o nome do animal a ser buscado: ").strip()
            zoologico.buscar_animal(nome)

        elif opcao == '4':
            categoria = input("Digite a categoria (Mamífero, Ave, Réptil): ").strip()
            zoologico.listar_animais_por_categoria(categoria)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()