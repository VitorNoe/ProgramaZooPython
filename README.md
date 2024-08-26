# ProgramaZooPython

Sistema de Cadastro de Animais no Zoológico
Descrição
Este programa é um sistema de cadastro e gerenciamento de animais em um zoológico. Ele permite cadastrar diferentes tipos de animais, listá-los, buscar informações detalhadas sobre cada um, e organizar os animais por categoria. A interface é baseada em um menu interativo, onde o usuário pode escolher diferentes ações.

Funcionalidades
Cadastrar novo animal: O usuário pode cadastrar animais de diferentes categorias: Mamíferos, Aves e Répteis. Durante o cadastro, são solicitadas informações como nome, idade, barulho característico, forma de locomoção, dieta, habitat, horário de alimentação e, dependendo da categoria, características adicionais como tipo de pelo, envergadura ou tipo de pele.

Listar todos os animais: Exibe uma lista com o nome de todos os animais cadastrados no zoológico.

Buscar animal por nome: Permite ao usuário procurar por um animal específico pelo nome. Se encontrado, o programa exibe todas as informações cadastradas sobre o animal.

Listar animais por categoria: Filtra e exibe os animais cadastrados com base em sua categoria (Mamífero, Ave ou Réptil).

Controle de vizinhos: Durante o cadastro de um animal, o usuário pode informar até dois vizinhos que compartilham o habitat com o animal. O programa valida para garantir que o número de vizinhos não exceda dois.

Como Executar
Clonar o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Executar o programa:

Execute o script Python utilizando o comando:

bash
Copiar código
python nome_do_arquivo.py
Certifique-se de que você tenha o Python instalado em sua máquina.

Interagir com o menu:

Após a execução, o menu principal será exibido, oferecendo as seguintes opções:

Cadastrar novo animal
Listar todos os animais
Buscar animal por nome
Listar animais por categoria
Sair
Selecione a opção desejada digitando o número correspondente e seguindo as instruções exibidas.

Estrutura do Código
Classe Animal: Classe base que representa um animal genérico. Contém atributos comuns a todos os animais, como nome, idade, barulho, movimento, alimentação, habitat, horário de alimentação, e vizinhos.

Classes Mamifero, Ave, Reptil: Subclasses de Animal que representam categorias específicas de animais, com atributos adicionais como tipo de pelo, envergadura ou tipo de pele.

Classe Zoologico: Gerencia a coleção de animais cadastrados, fornecendo métodos para cadastro, listagem e busca de animais.
