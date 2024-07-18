def solo_numeros(var):
    if not var:   
      return False
    
    for str in var:
        if str < '0' or str > '9':
            return False 
    return True 

# ejemplos de los usos
print(solo_numeros("12345"))  
print(solo_numeros("123c5"))  
print(solo_numeros(""))       
