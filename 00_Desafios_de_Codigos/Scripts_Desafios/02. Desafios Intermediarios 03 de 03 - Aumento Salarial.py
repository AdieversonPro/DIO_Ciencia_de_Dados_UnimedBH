# Desafio 03 - Aumento Salarial

salario = int(input()) 

if (salario >= 0 and salario <= 600.00):
  reajuste = salario * 17 / 100
  salario = salario + reajuste
  
  print(f'Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 17 %')
           
elif (salario > 600.00 and salario <= 900.00):
  reajuste = salario * 13 / 100
  salario = salario + reajuste
    
  print(f'Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 13 %')

elif (salario > 900.00 and salario <= 1500.00):
  reajuste = salario * 12 / 100
  salario = salario + reajuste
  
  print(f'Novo salario: {salario:.2f}znReajuste ganho: {reajuste:.2f}\nEm percentual: 12 %')

elif (salario > 1500 and salario <= 2000.00):
  reajuste = salario * 10 / 100
  Salario = salario + reajuste
  
  print(f'Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 10 %' )

else: 
  reajuste = salario * 5 / 100
  Salario = salario + reajuste
  
  print(f'Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 5 %')