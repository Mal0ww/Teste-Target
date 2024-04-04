def fibonacci(n: int) -> int:
    if(n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def verificar_numero(n: int) -> int:
    i = 0
    while(fibonacci(i) < n):
        i += 1
    return fibonacci(i) == n

if __name__ == '__main__':
    
    n = int(input("Numero: "))
    
    if(verificar_numero(n)):
        print(f"O número {n} faz parte da sequencia!")
    else:
        print(f"O número {n} não faz parte da sequencia")