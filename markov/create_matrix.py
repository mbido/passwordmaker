import json

def get_text(path : str, alphabet : str) -> str:
  """
  Read the text from a file.
  """
  with open(path, "r") as f:
    s = f.read()
  res = ""
  for c in s:
    if c in alphabet:
      res += c
  return res
  

def init_for_n_char(matrix : dict, n : int, text : str):
  """
  Initialize the matrix looking at n characters at a time.
  """
  set_txt = set(text)
  for i in range(n, len(text)):
    key = text[i - n:i]
    next_char = text[i]
    # print(f"key: {key}, next_char: {next_char}")
    
    if key not in matrix:
      matrix[key] = {c: 0 for c in set_txt}
    
    if next_char not in matrix[key]:
      continue
    else:
      matrix[key][next_char] += 1

def normalize(matrix : dict, noise : float = 0.01):
  """
  Normalize the matrix.
  """
  for key in matrix:
    total = sum(matrix[key].values())
    for k in matrix[key]:
      matrix[key][k] = (matrix[key][k] + noise) / (total + noise * len(matrix[key]))
  return matrix

def save_normalized_matrix(matrix : dict, path : str):
  """
  Save the matrix to a file.
  """
  with open(path, "w") as f:
    json.dump(matrix, f)

if __name__ == "__main__":
  print("Creating the matrix for the Markov chain")
  
  # the matrix looks something like this:
  # {
  #   'h': {'e': 1}, 
  #   'e': {'l': 1}, 
  #   'l': {'l': 1, 'o': 1}, 
  #   'he': {'l': 1}, 
  #   'el': {'l': 1}, 
  #   'll': {'o': 1}
  # }
  matrix = {}
  max_char = 5
  alphabet = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûëïüÿ"
  text = get_text("../data/1984-fr.txt", alphabet)
  
  for i in range(1, max_char + 1):
    print(f"Initializing for {i} characters")
    init_for_n_char(matrix, i, text)
  # print(matrix)
  normalize(matrix, 0.00)
  # print(matrix)
  
  save_normalized_matrix(matrix, "matrix.json")
