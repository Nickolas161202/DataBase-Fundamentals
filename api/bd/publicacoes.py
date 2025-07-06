class Publicacao:
    
    def __init__(self, texto: str, id_autor: uuid.UUID):
        self.id = id
        self.texto = texto  #
        self.id_autor = id_autor  #
        self.data_criacao = datetime.now()