# calculadora.py
#teste de notificação 
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Testes automáticos para o CI
if __name__ == "__main__":
    print("Executando testes da calculadora...")
    assert soma(10, 5) == 15, "Soma está incorreta!"
    print("✅ Teste de soma OK")
    assert subtrai(10, 5) == 5, "Subtração está incorreta!"
    print("✅ Teste de subtração OK")
    assert multiplica(10, 5) == 50, "Multiplicação está incorreta!"
    print("✅ Teste de multiplicação OK")
    assert divide(10, 5) == 2, "Divisão está incorreta!"
    print("✅ Teste de divisão OK")
    print("\n🎉 Todos os testes foram concluídos com sucesso!")
