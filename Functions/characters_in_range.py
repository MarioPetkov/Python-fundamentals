def symbols_between_inputs(a:str,b:str):
  for i in range(ord(a_character)+1,ord(b_character)):
    string_list.append(chr(i))
  return string_list    
a_character = input()
b_character = input()
string_list = []
final_result = symbols_between_inputs(a_character, b_character)
print(" ".join(final_result))
