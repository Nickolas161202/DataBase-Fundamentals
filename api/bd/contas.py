class Conta:
    
    def __init__(self, id: int, name: str, password: str, email: str, foto_perfil: str = None, banner: str = None ,sobre: str = None):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.foto_perfil = foto_perfil
        self.banner = banner
        self.sobre = sobre
    
    def to_dict(self):      
        return {
            'id': str(self.id),
            'nome': self.name,
            'email': self.email,
            'fotoPerfil': self.foto_perfil,
            'banner': self.banner,
            'sobre': self.sobre
        }

class Perfil_Pessoal(Conta):
    
    def __init__(self, id: int, name: str, email: str, senha: str, titulo: str, **kwargs):
        super().__init__(id,name, email, senha, **kwargs)
        self.titulo = titulo
    
    def to_dict(self):
        data = super().to_dict()
        data['titulo'] = self.titulo
        data['tipo'] = 'pessoal'
        return data
        
class Perfil_Empresarial(Conta):
    
    def __init__(self, id: int, name: str, email: str, senha: str, nome_fantasia: str, localizacao: str, setor: str, **kwargs):
        super().__init__(id,name, email, senha, **kwargs)
        self.nome_fantasia = nome_fantasia  
        self.localizacao = localizacao  
        self.setor = setor
        
    def to_dict(self):
        data = super().to_dict()
        data['nomeFantasia'] = self.nome_fantasia
        data['localizacao'] = self.localizacao
        data['setor'] = self.setor
        data['tipo'] = 'empresarial'
        return data
    

class Gerenciamento_Contas:
    
    def __init__(self):
        pass
    
    def criar_conta(dados: dict):
        pass