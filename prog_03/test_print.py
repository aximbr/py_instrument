import sys, time

leitura = [1, 4, 5, 6, 7, 2, 40, 25, 100, 99]

# for n in leitura:
#     print(n)

for n in leitura:
    sys.stdout.write(f"A leitura é: {n}   \r")
    time.sleep(0.2)
    sys.stdout.flush()