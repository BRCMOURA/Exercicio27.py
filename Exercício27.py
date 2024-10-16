#Peça um valor em dias e converta para semanas e dias

dias = int(input("Digite um valor em dias:"))

semanas = dias // 7

dias = dias % 7

print(f'A quantidade de dias equivalem a {semanas} semanas e {dias} dias')
