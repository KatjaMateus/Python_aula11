class Material:
    def __init__(self, titulo, autor_ou_editora) -> None:
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
    
    def exibir_informacoes(self):
        return f"""
        Informações:
        Titulo: {self.titulo}
        Autor / Editora: {self.autor_ou_editora}"""

class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        return f"""{Material.exibir_informacoes(self)}
        Genero: {self.genero}"""

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    
    def exibir_informacoes(self):
        return f"""{Material.exibir_informacoes(self)} 
        Edição: {self.edicao}"""

livro1= Livro(titulo="It", autor_ou_editora="Stephen King", genero="terror")
revista1= Revista(titulo="Hello", autor_ou_editora="Weiling", edicao="janeiro 2024")

print(livro1.exibir_informacoes())
print(revista1.exibir_informacoes())