def funcao_Externa():
    variavel = 'a variavel da função externa pode ser acessada mesmo após o fechamento da função'
    def funcao_interna():
        print(variavel)
    return funcao_interna
   

oi = funcao_Externa()

oi()
