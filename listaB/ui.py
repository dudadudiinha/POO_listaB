from view import ContatoView
from datetime import datetime

class ContatoUI:

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Listar pelo ID, 4-Atualizar, 5-Excluir, 6-Pesquisar, 7-Aniversariantes, 8-Salvar, 9-Abrir, 10-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def main(cls):
        op = 0
        while op != 10:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.listar_id()
            if op == 4: cls.atualizar()
            if op == 5: cls.excluir()
            if op == 6: cls.pesquisar()
            if op == 7: cls.aniversariantes()
            if op == 8: cls.salvar()
            if op == 9: cls.abrir()

    @classmethod
    def inserir(cls):
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        nasc = datetime.strptime(input("Nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        for c in ContatoView.listar():
            if c.get_id() == id:
                print("ID já cadastrado.")
                return
            if c.get_email() == email:
                print("Email já cadastrado.")
                return
        ContatoView.inserir(id, nome, email, fone, nasc)

    @classmethod
    def listar(cls):
        contatos = ContatoView.listar()
        if len(contatos) == 0:
            print("Nenhum contato.")
        for c in contatos:
            print(c)

    @classmethod
    def listar_id(cls):
        id = int(input("ID: "))
        c = ContatoView.listar_por_id(id)
        if c: print(c)
        else: print("Contato não encontrado.")

    @classmethod
    def atualizar(cls):
        id = int(input("ID do contato a atualizar: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo fone: ")
        ContatoView.atualizar(id, nome, email, fone)
        print("Contato atualizado.")

    @classmethod
    def excluir(cls):
        id = int(input("ID do contato a excluir: "))
        ContatoView.excluir(id)
        print("Contato excluído.")

    @classmethod
    def pesquisar(cls):
        termo = input("Digite parte do nome: ")
        resultados = ContatoView.pesquisar(termo)
        if resultados:
            for c in resultados:
                print(c)
        else:
            print("Nenhum contato encontrado.")

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Mês (1 a 12): "))
        contatos = ContatoView.aniversariantes(mes)
        if contatos:
            for c in contatos:
                print(c)
        else:
            print("Nenhum aniversariante neste mês.")

    @classmethod
    def abrir(cls):
        ContatoView.abrir()
        print("Contatos carregados.")

    @classmethod
    def salvar(cls):
        ContatoView.salvar()
        print("Contatos salvos.")


ContatoUI.main()