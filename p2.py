dinheiro_do_dia = float(input('Digite o total de dinheiro do dia '))

dinheiro_dos_vales = float(input('Digite o total de dinheiro dos vales '))


valor_do_litro_b1_b4 = float(input('Digite o valor do litro da B1 e B4 '))

valor_do_litro_b2_b5 = float(input('Digite o valor do litro da B2 e B5 '))

valor_do_litro_b3_b6 = float(input('Digite o valor do litro da B3 e B6 '))

codigo_b1_1 = float(input('Código da b1 de manhã '))
codigo_b4_1 = float(input('Código da b4 de manhã '))
codigo_b2_1 = float(input('Código da b2 de manhã '))
codigo_b5_1 = float(input('Código da b5 de manhã '))
codigo_b3_1 = float(input('Código da b3 de manhã '))
codigo_b6_1 = float(input('Código da b6 de manhã '))

codigo_b1_2 = float(input('Código da b1 de noite '))
codigo_b4_2 = float(input('Código da b4 de noite '))
codigo_b2_2 = float(input('Código da b2 de noite '))
codigo_b5_2 = float(input('Código da b5 de noite '))
codigo_b3_2 = float(input('Código da b3 de noite '))
codigo_b6_2 = float(input('Código da b6 de noite '))

soma_dos_litros_rv_b1 = float(
    input("Digite a soma dos litros da Revenda do B1 "))
soma_dos_dinheiro_rv_b1 = float(
    input("Digite a soma do dinheiro da Revenda do B1 "))

soma_dos_litros_rv_b5 = float(
    input("Digite a soma dos litros da Revenda do B5 "))
soma_dos_dinheiro_rv_b5 = float(
    input("Digite a soma do dinheiro da Revenda do B5  "))

soma_dos_litros_dos_vales_b1 = float(
    input("Digite a soma dos litros dos vales da B1 "))

soma_dos_litros_dos_vales_b5 = float(
    input("Digite a soma dos litros dos vales da B5 "))

soma_dos_litros_dos_vales_b3 = float(
    input("Digite a soma dos litros dos vales da B3 "))


codigo_b1_final = abs(codigo_b1_2-codigo_b1_1)
codigo_b4_final = abs(codigo_b4_2-codigo_b4_1)
litros_vendidos_b1_b4 = codigo_b1_final + codigo_b4_final

codigo_b2_final = abs(codigo_b2_2-codigo_b2_1)
codigo_b5_final = abs(codigo_b5_2-codigo_b5_1)
litros_vendidos_b2_b5 = codigo_b2_final + codigo_b5_final

codigo_b3_final = abs(codigo_b3_2-codigo_b3_1)
codigo_b6_final = abs(codigo_b6_2-codigo_b6_1)
litros_vendidos_b3_b6 = codigo_b3_final + codigo_b6_final

litro_final_b3 = abs(litros_vendidos_b3_b6 - soma_dos_litros_dos_vales_b3)
litro_final_b5 = abs(litros_vendidos_b2_b5 -
                     soma_dos_litros_dos_vales_b5 - soma_dos_litros_rv_b5)
litro_final_b1 = abs(litros_vendidos_b1_b4 -
                     soma_dos_litros_dos_vales_b1 - soma_dos_litros_rv_b1)


dinheiro_do_litro_b1 = (litro_final_b1*valor_do_litro_b1_b4)
dinheiro_do_litro_b5 = (litro_final_b5*valor_do_litro_b2_b5)

dinheiro_total_b1 = dinheiro_do_litro_b1 + soma_dos_dinheiro_rv_b1
dinheiro_total_b5 = dinheiro_do_litro_b5 + soma_dos_dinheiro_rv_b5
dinheiro_total_b3 = (litro_final_b3*valor_do_litro_b3_b6)

dinheiro_total_das_bombas = (
    dinheiro_total_b1 + dinheiro_total_b5 + dinheiro_total_b3)

dinheiro_total = dinheiro_do_dia + dinheiro_dos_vales

diferenca = dinheiro_total_das_bombas - dinheiro_total


print('Litros vendido na b1 e b4 ', litros_vendidos_b1_b4)
print('Litros vendido na b1 e b4 sem vale e sem revenda', litro_final_b1)

print('Quantidade de dinheiro do litro vendido sem vale e sem revenda b1 ',
      dinheiro_do_litro_b1)

print('Litros vendido na b2 e b5 ', litros_vendidos_b2_b5)
print('Litros vendido na b2 e b5 sem vale e sem revenda', litro_final_b5)
print('Quantidade de dinheiro do litro vendido sem vale e sem revenda b2 ',
      dinheiro_do_litro_b5)

print('Litros vendido na b3 e b6 ', litros_vendidos_b3_b6)
print('Litros vendido na b3 e b6 sem vale e sem revenda', litro_final_b3)
print('Quantidade de dinheiro do litro vendido sem vale e sem revenda b3 ',
      dinheiro_total_b3)

print('dinheiro total da b1 ', dinheiro_total_b1)
print('dinheiro total da b5 ', dinheiro_total_b5)
print('dinheiro total da b3 ', dinheiro_total_b3)

print('Dinheiro total recebido com os vales', dinheiro_total)
print('Dinheiro total das bombas do dia', dinheiro_total_das_bombas)
print('A diferenca do dinheiro do dia foi', diferenca)

with open('resultado.txt', 'w') as arquivo:
    for valor in 'Dinheiro total recebido com os vales', dinheiro_total,'\n', 'Dinheiro total das bombas do dia', dinheiro_total_das_bombas, '\n','A diferenca do dinheiro do dia foi', diferenca:arquivo.write(str(valor) + '\n')
