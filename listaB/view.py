from model import Contato, ContatoDAO
from datetime import datetime
import json

class ContatoView:
    @classmethod
    def inserir(cls, id, nome, email, fone, nasc):
        for c in ContatoDAO.listar():
            if c.get_id() == id:
                raise ValueError("ID já cadastrado.")
            if c.get_email() == email:
                raise ValueError("Email já cadastrado.")
        contato = Contato(id, nome, email, fone, nasc)
        ContatoDAO.inserir(contato)

    @classmethod
    def listar(cls):
        return ContatoDAO.listar()

    @classmethod
    def listar_por_id(cls, id):
        return ContatoDAO.buscar_id(id)
    
    @classmethod
    def atualizar(cls, id, nome, email, fone):
        c = ContatoDAO.buscar_id(id)
        if c:
            c.set_nome(nome)
            c.set_email(email)
            c.set_fone(fone)
        else:
            raise ValueError("Contato não encontrado.")
    
    @classmethod
    def excluir(cls, id):
        c = ContatoDAO.buscar_id(id)
        if c:
            ContatoDAO.excluir(c)
        else:
            raise ValueError("Contato não encontrado.")
    
    @classmethod
    def pesquisar(cls, termo):
        resultado = []
        for c in ContatoDAO.listar():
            if c.get_nome().startswith(termo):
                resultado.append(c)

    @classmethod
    def aniversariantes(cls, mes):
        resultado = []
        for c in ContatoDAO.listar():
            if c.get_nasc().month == mes:
                resultado.append(c)

    @classmethod
    def abrir(cls, nome_arq="contatos.json"):
        with open(nome_arq, mode="r") as arquivo:
            contatos_json = json.load(arquivo)
            lista = [Contato.dict2(obj) for obj in contatos_json]
            ContatoDAO.carregar(lista)

    @classmethod
    def salvar(cls, nome_arq="contatos.json"):
        lista = [c.dict1() for c in ContatoDAO.get_contatos()]
        with open(nome_arq, mode="w") as arquivo:
            json.dump(lista, arquivo)
