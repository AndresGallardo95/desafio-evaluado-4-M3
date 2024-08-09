from datetime import datetime

# Lista inicial de recordatorios
recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# 1. Agregar un evento el 2 de Enero de 2021 a las 6 de la mañana para “Empezar el Año”.
recordatorios.append(['2021-01-02', "06:00", "Empezar el año"])

# 2. Editar evento del 15 de Julio al 16 de Julio
for recordatorio in recordatorios:
    if recordatorio[0] == '2021-07-15':
        recordatorio[0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo (1 de mayo)
recordatorios = [recordatorio for recordatorio in recordatorios if not (recordatorio[0] == '2021-05-01' and "No trabajar" in recordatorio[2])]

# 4. Agregar una cena de Navidad (24 de diciembre a las 22:00) y de Año Nuevo (31 de diciembre a las 22:00)
recordatorios.append(['2021-12-24', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

# Ordenar los recordatorios por fecha y hora
recordatorios.sort(key=lambda x: datetime.strptime(x[0] + ' ' + x[1], '%Y-%m-%d %H:%M'))

# Output
for recordatorio in recordatorios:
    print(recordatorio)
