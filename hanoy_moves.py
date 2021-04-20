'''

                            Python Hanoy moves.

'''

def hanoi_mov(n):
    return (2**n)-1

def main():
    
    print("Digite a quantidade de discos:")
    quant = input()
    print("Quantidade de movimentos: " + str (hanoi_mov(int(quant))))
    

main()
