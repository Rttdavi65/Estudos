peso= float(input('[Digite seu peso (kg): '))
altura = float(input('[Digite sua altura (metro e cm): '))
imc = peso/(altura*altura)
print('Seu imc é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif imc > 18.5 and imc < 25:
    print('Você está com um peso ideal!')
elif imc > 25 and imc < 30:
    print('Você está com um sobrepeso!')
elif imc > 30 and imc < 40:
    print('Você está com obesiade!')
elif imc > 40:
    print('Você está com obesidade mórbida!')