import create_matrix as cm
import json
import random

def import_matrix(path : str) -> dict:
  """
  Import the matrix from a file.
  """
  with open(path, "r") as f:
    matrix = json.load(f)
  return matrix

def generate_word(matrix : dict, word_size : int, word : str, n : int) -> str:
  """
  Generate a word using the Markov chain.
  """
  # word must be at least the size of 1
  for _ in range(word_size):
    key_size = min(n, len(word))
    key = word[-key_size:]
    while key not in matrix:
      key = key[1:]
      if key == "":
        key = random.choice(list(matrix.keys()))
    next_char = random.choices(list(matrix[key].keys()), matrix[key].values())[0]
    # if next_char == " ":
    #   break
    word += next_char
  return word

  

if __name__ == "__main__":
  word_size = 20
  matrix = import_matrix("matrix.json")
  for _ in range(10):
    gen = random.choice("abcdefghijklmnopqrstuvwxyz")
    gen = generate_word(matrix, word_size, gen, 4)
    print(gen)