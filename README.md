# agendador-corte-cabelo
## Descrição do Problema
Um barbeiro atende clientes com horários fixos de 30 minutos. O sistema deve calcular o tempo total disponível no dia e verificar se um novo cliente cabe na agenda sem sobrepor horários existentes.
## Requisitos
- Receber lista de horários já ocupados (string HH:MM)
- Receber horário desejado pelo novo cliente
- Verificar conflitos de agenda
- Calcular horas livres no dia
## Exemplo de Uso
Entrada: ocupados = ['09:00', '09:30'], novo = '09:30'
Saída: Conflito detectado. Horas livres: 7.5