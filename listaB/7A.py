from datetime import datetime
import json

class Contato:
    def __init__(self, i, n, e, f, b):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nasc = b
        self.set_nasc(self.__nasc) 
    
    def set_nasc(self, b):
        if b > datetime.today(): 
            raise ValueError("A data de nascimento é inválida")
        self.__nasc = b
    def get_nasc(self):
        return self.__nasc

    def set_nome(self, n):
        if n == "": raise ValueError("Nome não pode ser vazio.")
        self.__nome = n
    def get_nome(self):
        return self.__nome
    
    def set_id(self, i):
        if i < 0: raise ValueError("ID não pode ser negativo.")
        self.__id = i
    def get_id(self):
        return self.__id 
    
    def set_email(self, e):
        if e == "": raise ValueError("Nome não pode ser vazio.")
        self.__email = e
    def get_email(self):
        return self.__email
    
    def set_fone(self, f):
        if f == "": raise ValueError("Nome não pode ser vazio.")
        self.__fone = f
    def get_fone(self):
        return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}"
    
    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "e-mail": self.__email,
            "fone": self.__fone,
            "nasc": self.__nasc.strftime('%d/%m/%Y')
        }

    @classmethod
    def from_dict(cls, d):
        nasc = datetime.strptime(d["nasc"], '%d/%m/%Y')
        return cls(d["id"], d["nome"], d["e-mail"], d["fone"], nasc)


class ContatoDAO:
    __contatos = []
    __arquivo = "contatos.json"

    @classmethod
    def __abrir(cls, c):
        try:
            with open(cls.__arquivo, mode="r") as arquivo:
                contatos_json = json.load(arquivo)
                lista = []
                for obj in contatos_json:
                    c = Contato.from_dict(obj)
                    lista.append(c)
                cls.__contatos = lista
        except FileNotFoundError:
            cls.__contatos = []

    @classmethod
    def __salvar(cls):
        lista = []
        for c in cls.__contatos:
            lista.append(c.to_dict())
        with open(cls.__arquivo, mode="w") as arquivo:
            json.dump(lista, arquivo)
    
    @classmethod
    def inserir(cls, contato):
        cls.__abrir()
        cls.__contatos.append(contato)
        cls.__salvar()
    
    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__contatos

    @classmethod
    def listar_id(cls, id):
        cls.__abrir()
        for c in cls.__contatos:
            if id == c.get_id():
                return c
        return None

    @classmethod
    def atualizar(cls, contato):
        cls.__abrir()
        for c in cls.__contatos:
            if id == contato.get_id():
                c.set_nome(contato.get_nome())
                c.set_email(contato.get_email())
                c.set_fone(contato.get_fone())
                c.set_nasc(contato.get_nasc())
                cls.__salvar()
                return True
        return False

    @classmethod
    def excluir(cls, id):
        cls.__abrir()
        for c in cls.__contatos:
            if id == c.get_id():
                cls.__contatos.remove(c)
                cls.__salvar()
                return True
        return False
    
class ContatoView:

    @staticmethod
    def inserir(i, n, e, f, b):
        contato = Contato(i, n, e, f, b)
        ContatoDAO.inserir(contato)

    @staticmethod
    def listar():
        return ContatoDAO.listar()

    @staticmethod
    def listar_id(id):
        return ContatoDAO.listar_id(id)

    @staticmethod
    def atualizar(i, n, e, f, b):
        contato = Contato(i, n, e, f, b)
        return ContatoDAO.atualizar(contato)

    @staticmethod
    def excluir(id):
        return ContatoDAO.excluir(id)

class ContatoUI:

    @classmethod
    def menu(cls):
        return int(input("1-Inserir, 2-Listar, 3-Listar pelo ID, 4-Atualizar, 5-Excluir, 6-Fim\nInforme uma opção: "))
    
    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = cls.menu()
            match op:
                case 1: cls.inserir()
                case 2: cls.listar()
                case 3: cls.listar_id()
                case 4: cls.atualizar()
                case 5: cls.excluir()

    @classmethod
    def inserir(cls):
        i = int(input("Informe o ID: "))
        n = input("Informe o nome: ")
        e = input("Informe o e-mail: ")
        f = input("Informe o fone: ")
        b = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%M/%Y")
        ContatoView.inserir(i, n, e, f, b)

    @classmethod
    def listar(cls):
        lista = ContatoView.listar()
        if lista:
            for c in lista:
                print(c)
        else: print("Nenhum contato encontrado.")

    @classmethod
    def listar_id(cls):
        id = int(input("Informe o ID: "))
        c = ContatoView.listar_id(id)
        if c: print(c)
        else: print("Contato não encontrado.")

    @classmethod
    def atualizar(cls):
        i = int(input("Informe o ID: "))
        n = input("Informe o nome: ")
        e = input("Informe o e-mail: ")
        f = input("Informe o fone: ")
        b = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%M/%Y")
        if ContatoView.atualizar(i, n, e, f, b): print("Contato atualizado.")
        else: print("Contato não encontrado.")

    @classmethod
    def excluir(cls):
        ContatoView.listar()
        id = int(input("Informe o ID do contato a ser excluído: "))
        if ContatoView.excluir(id): print("Contato excluído.")
        else: print("Contato não encontrado.")

ContatoUI.main()