class Musica:
    __titulo = str
    __artista = str
    __album = str

    def __init__(self, titulo, artista, album):
        self.setTitulo(titulo)
        self.setArtista(artista)
        self.setAlbum(album)
    
    def __str__(self):
        dados = ""
        dados += f"Título: {self.getTitulo()}\n"
        dados += f"Artista: {self.getArtista()}\n"
        dados += f"Album: {self.getAlbum()}\n"
        return dados
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setArtista(self, artista):
        self.__artista = artista
    
    def setAlbum(self, album):
        self.__album = album
    
    def getTitulo(self):
        return self.__titulo
    
    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

class Playlist:
    __nome = str
    __descricao = str
    __musicas = []

    def __init__(self, nome, descricao):
        self.setNome(nome)
        self.setDescricao(descricao)
    
    def __str__(self):
        return f"Quantidade de músicas: {len(self.listar())}"
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setDescricao(self, descricao):
        self.__descricao = descricao
    
    def getNome(self):
        return self.__nome
    
    def getDescricao(self):
        return self.__descricao

    def inserir(self, musica):
        self.__musicas.append(musica)
    
    def listar(self):
        return self.__musicas

""" Testando as classes """
musica1 = Musica("Árvore de vento", "Roberto", "Árvores")
musica2 = Musica("Árvore de fogo", "Roberto", "Árvores")
musica3 = Musica("Árvore de sal", "Roberto", "Árvores")
playlist = Playlist("Meu artista favorito", "Músicas de Roberto")
playlist.inserir(musica1)
playlist.inserir(musica2)
playlist.inserir(musica3)
print(playlist)
print(playlist.listar())