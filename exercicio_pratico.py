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
