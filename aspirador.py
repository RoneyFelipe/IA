class No :
        def __init__(self, pR) :
            self.posicaoRobo = pR
            self.pai = None
            self.esq = None
            self.dir = None
            self.salaA = "N"
            self.salaB = "N"
              
        def expandeEsq (self, noNavegacao):
             novoNo = No(1)
             novoNo.pai = noNavegacao
             noNavegacao.esq = novoNo
             
             return novoNo

        def expandeDir(self, noNavegacao):
             novoNo = No(2)
             novoNo.pai = noNavegacao
             noNavegacao.dir = novoNo
             
             return novoNo

        def expandeLimpar(self, noNavegacao):
             novoNo = No(noNavegacao.posicaoRobo)
             if noNavegacao.posicaoRobo == 1:
                  novoNo.salaA = "S"

             elif noNavegacao.posicaoRobo == 2:
                  novoNo.salaB = "S"
            
             return novoNo
        


def verificaObjetivo(noNavegacao):
        
        print("-------------Verificando----------")

        print(noNavegacao.posicaoRobo, noNavegacao.salaA, noNavegacao.salaB)

        if noNavegacao.salaA == "S" and noNavegacao.salaB == "S":
            
            print("Programa Encerrado, salas limpas")
            print("---------------------------------------")
            return 0
        
        else:
            return 1

     
     
def expansao(fronteira, noNavegacao):
     
     if noNavegacao.posicaoRobo == 0:
          fronteira.append(noNavegacao.expandeEsq(noNavegacao))
          fronteira.append(noNavegacao.expandeDir(noNavegacao))
          print("ENtrei")
    
     else: 
        

        if noNavegacao.posicaoRobo == 1:
            fronteira.append(noNavegacao.expandeDir(noNavegacao))

            if noNavegacao.salaA == "N":
                fronteira.append(noNavegacao.expandeLimpar(noNavegacao))
            
        elif noNavegacao.posicaoRobo == 2:
            fronteira.append(noNavegacao.expandeEsq(noNavegacao))

            if noNavegacao.salaB == "N":
                fronteira.append(noNavegacao.expandeLimpar(noNavegacao))


    
     
def buscaLargura(noInicial, caminhoPercorridoLargura):

     fronteira = []
     fronteira.append(noInicial)
     noNavegacao = noInicial
     posicao = 0
     

     while (verificaObjetivo(noNavegacao)):
          
          caminhoPercorridoLargura.append(noNavegacao)
        
          expansao(fronteira, noNavegacao)

          del(fronteira[0])

          print("Iteração")
          print("Tamanho:", len(fronteira))

          noNavegacao = fronteira[0]

          print(posicao)
          posicao = posicao + 1
          

          
     

def main():
     caminhoPercorridoLargura = []
     noInicialLargura = No(0)
     buscaLargura(noInicialLargura, caminhoPercorridoLargura)
     print(caminhoPercorridoLargura)
     caminhoPercorridoProfundidade = []
     #buscaProfundidade(noInicialProfundiade)

main()