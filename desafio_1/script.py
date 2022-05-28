import time as tm

def SENSOR(parametro):
    paramentro_selecionado = input(f"Informe a {parametro}")
    return paramentro_selecionado


def EXAUSTOR(estado):
    print(f'EXAUSTOR: {estado}')


def AQUECIMENTO(temperatura):
    print(f'AQUECIMENTO: {temperatura}')


def desumidificacao():
    print("Iniciando desumidificação...")

    temp_int = int(SENSOR("Temperatura interna do forno: "))
    umidade = int(SENSOR("Umidade do ar interna do forno: "))

    if temp_int > 15 and umidade >= 40:
        EXAUSTOR("ON")
    else:
        EXAUSTOR("ON")
        AQUECIMENTO("ON")

    def aquecimento_forno(temp_int):
        if temp_int < 100:
            while temp_int < 100:
                temp_int += 1
            print(f"forno aquecido à {temp_int}°C")
    aquecimento_forno(temp_int)

    def estado_exaustor():
        if umidade < 5:
            EXAUSTOR("OFF")
        elif AQUECIMENTO("ON"):
            AQUECIMENTO("OFF")
    estado_exaustor()

    return print("Desumidificação concluida")


def coccao():
    print("inciando cocção...")

    umidade = int(SENSOR("Umidade: "))
    temp_int = int(SENSOR("Temperatura interna: "))
    if umidade > 15:
        EXAUSTOR("ON")
    else:
        EXAUSTOR("OFF")

    def aquecimento_forno(temp_int):
        if temp_int < 200:
            while temp_int < 380:
                temp_int += 1
            print(f"O forno foi aquecido para {temp_int}°C")
    aquecimento_forno(temp_int)

    def analise():
        if umidade <= 5:
            EXAUSTOR("OFF")
            AQUECIMENTO("OFF")
            print("Desumidificação concluida")
    analise()

    estado_botao = input("Insira 'pronto' para iniciar: ").upper().strip()

    if estado_botao == "pronto":
        print("aquecimento será mantido por mais 3 horas")
    while estado_botao != "PRONTO":
        print("Comando incorreto!")
        estado_botao = input("Insira 'pronto' para iniciar: ").upper().strip()

    def cronometro(num_of_secs):
        while num_of_secs:
            # multiplica o número de segundos por 60
            m, s = divmod(num_of_secs, 60)
            min_sec_format = f"{m:02d}:{s:02d}"
            print(min_sec_format, end="\r")
            tm.sleep(1)
            num_of_secs -= 1
        print("Cocção concluida")
        AQUECIMENTO("OFF")
    tempo = 10
    cronometro(tempo)


umidade = int(SENSOR("umidade: "))
temp_ext = int(SENSOR("Temperatura externa: "))
temp_int = int(SENSOR("Temperatura interna: "))

if temp_ext <= 20 and umidade > 40:
    print("condição de inverno identificada!")
    desumidificacao()
    coccao()
else:
    print("outro clima identificado...")
    coccao()
