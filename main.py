def calcular_agenda(horarios_ocupados, novo_horario):
    total_minutos = 10 * 60
    minutos_ocupados = 0
    conflito = False

    for h in horarios_ocupados:
        minutos_ocupados += 30
        partes = h.split(':')
        minutos_horario = int(partes[0]) * 60 + int(partes[1])
        
        partes_novo = novo_horario.split(':')
        min_novo = int(partes_novo[0]) * 60 + int(partes_novo[1])
        
        if abs(minutos_horario - min_novo) < 30:
            conflito = True

    horas_livres = (total_minutos - minutos_ocupados) / 60
    return conflito, horas_livres

ocupados = ['08:00', '08:30', '09:00']
novo = '08:30'

conf, livres = calcular_agenda(ocupados, novo)

if conf:
    print(f"Conflito detectado. Horas livres: {livres}")
else:
    print(f"Agendado com sucesso. Horas livres: {livres}")