conta = float(input("Quanto deu a conta: "))  

def exibirConta(conta):
  valor = conta * 0.1
  
  print("Com a gorjeta, vai ficar ",valor+conta)

exibirConta(conta)