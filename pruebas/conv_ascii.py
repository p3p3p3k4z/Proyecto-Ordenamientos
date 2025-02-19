def convert_to_ascii(char_list):
    # Convertir cada cadena en la lista a una lista de caracteres y luego a sus valores ASCII
    ascii_values = [ord(char) for string in char_list for char in string]
    return ascii_values

# Ejemplo de uso
ls = ['pepe pecas']
ascii_values = convert_to_ascii(ls)
print(ascii_values)
