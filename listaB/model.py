from datetime import datetime

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
    
    def dict1(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "e-mail": self.__email,
            "fone": self.__fone,
            "nasc": self.__nasc.strftime('%d/%m/%Y')
        }

    @classmethod
    def dict2(cls, d):
        nasc = datetime.strptime(d["nasc"], '%d/%m/%Y')
        return cls(d["id"], d["nome"], d["e-mail"], d["fone"], nasc)


class ContatoDAO:
    __contatos = []

    @classmethod
    def inserir(cls, c):
        cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        return cls.__contatos
    
    @classmethod
    def buscar_id(cls, id):
        for c in cls.__contatos:
            if c.get_id() == id:
                return c
        return None
    
    @classmethod
    def excluir(cls, c):
        cls.__contatos.remove(c)

    @classmethod
    def get_contatos(cls):
        return cls.__contatos

    @classmethod
    def carregar(cls, lista):
        cls.__contatos = lista