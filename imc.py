def verifyResultImc(imc):
    if(imc < 17):
        print('você está muito abaixo do peso')
    elif(imc >= 18 and imc <= 24):
        print('você está com o peso normal')
    elif(imc >= 25 and imc <= 29):
        print('você está acima do peso')
    else:
        print('você está com obesidade')


def imc():     
    nameUser = input('Digite seu nome:')
    weight = float(input('digite seu peso: '))
    height = float(input('agora digite sua altura: '))
    resultImc = weight / (height * height)
    print(nameUser,',o resultado do seu imc é de:',round(resultImc,2))
    verifyResultImc(resultImc)
imc()