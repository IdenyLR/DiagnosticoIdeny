#fibonacci 
def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[i-1] + secuencia[i-2])
    return secuencia

if __name__ == "__main__":
    n = int(input("¿Cuántos términos de Fibonacci deseas?: "))
    print(f'Secuencia de Fibonacci: {fibonacci(n)}')
