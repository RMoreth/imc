

try:
    r = ''
    while r != "n":
        nome = str(input("Informe o nome do paciente", end=''))
        peso = str(input("informe o peso em KG", end='')).replace(',','.')
        altura = str(input("informe a altura", end='')).replace(',','.')

        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura * altura) 

        if imc <= 18.5:
                resultado = "baixo peso"
        elif imc <= 25:
                resultado ="peso adequado"
        elif imc <= 30:
                resultado = "sobrepeso"
        elif imc <= 35:
                resultado = "obesidade grau I"
        elif imc <= 40:
                resultado = "obesidade grau II"
        else:
                resultado = "obesidade grau III"
        print(f"Paciente: {nome}, tem o imc: {imc:,.2f} e esta com {resultado}")
        r = str(input("quer adicionar outro paciente?")).strip()[:1]
except Exception as e:
    print(f"Erro detectado. Erro: {e}")
finally:
    print("saindo do programa")
