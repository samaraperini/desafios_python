# Considere a seguinte agenda de disponibilidade de atendimento de uma clínica com vários médicos, cada um de uma especialidade distinta. 
# Essa clínica possuí apenas três consultórios, e, por isso, no máximo três médicos podem atender por dia.
# A clínica percebeu que os pacientes que desejam se consultar com mais de um médico sempre solicitam que o atendimento seja realizado no mesmo dia.
# Você, como um(a) aspirante a desenvolvedor Python, aceitou o desafio de ajudar a automatizar essa tarefa. 
# Para tanto, irá desenvolver duas funções que receberão a relação de disponibilidade de cada médico e que retornarão os dias disponíveis:

cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

def disp_dois_especialistas(medico01, medico02):  
  for dias in medico01:
    if dias in medico02:
      print(dias)

def disp_tres_especialistas(medico01, medico02, medico03):  
  for dias in medico01:
    if dias in medico02 and medico03:
      print(dias)

disp_dois_especialistas(ortopedista,neurologista)
disp_tres_especialistas(dermatologista, neurologista, psiquiatra)
