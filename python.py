x = 5
x = "5 sdidfhisd dhfsiuhfus dshfiuhsiud"
x = ['andre', 'vitoria', 'victor', 'joao', 'manoel']

for item in x:
    print(item);





print(x[3])


def aprovacao(nota):
    if nota >= 7:
        return 'aluno aprovado'
    else: 
        return 'aluno reprovado' 
    
print(aprovacao(2))


class Usuario:
    
    saude = 10    
    
    def __init__(self, nome, passos):
        self.nome = nome
        self.passos = passos


    def andar(cls, passos):
        print( 'andou' + str(passos))

    @classmethod
    def aumentaSaudeGeral(cls):
        cls.saude = cls.saude + 10
        print(cls.saude)
usuari01 = Usuario('andre', 23)

usuari01.andar(10) 

Usuario.aumentaSaudeGeral()
Usuario.aumentaSaudeGeral()
Usuario.aumentaSaudeGeral()
Usuario.aumentaSaudeGeral()
Usuario.aumentaSaudeGeral()


class CriaCategorias:

    def __init__(self, categorias):
        dictx = []
        for categoria in categorias:
            dictx.append({'categoria': categoria })
        self.dictx = dictx


    def __repr__(self,) :               
        for item in dictx:
            print ('categoria' + item)



x = ['humor', 'esporte' , 'musicas' , 'natacao']

xcat = CriaCategorias(x)

print(xcat)