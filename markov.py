import numpy as np

### Helper Functions

def strip_string(str):
	clean_str = str.replace("'", "")
	clean_str = clean_str.replace("’", "")
	clean_str = clean_str.replace("“", "")
	clean_str = clean_str.replace("”", "")
	clean_str = clean_str.replace("  ", " ")
	clean_str = clean_str.replace('"', "")
	clean_str = clean_str.replace("(", "")
	clean_str = clean_str.replace(")", "")
	clean_str = clean_str.replace(".", " .")
	clean_str = clean_str.replace("&", "")
	#clean_str = clean_str.replace("-", "")
	clean_str = clean_str.replace("_", "")
	clean_str = clean_str.replace("—", ", ")
	clean_str = clean_str.replace(",", " ,")
	
	return clean_str


def newPage():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	

text = open("/content/Markov/bush.txt", "r").read().lower()


text =  strip_string(text)

text_list = text.split(" ")

unique_words = []

for word in text_list:
  if word not in unique_words:
    unique_words.append(word)

unique_words_dict = { word : i for i, word in enumerate(unique_words) }
unique_words_dict2 = { i : word for i, word in enumerate(unique_words) }

frequency_matrix = np.zeros((len(unique_words), len(unique_words)))

for i in range(len(text_list)-1):
  current_word = text_list[i]
  next_word = text_list[i+1]
  frequency_matrix[unique_words_dict[current_word], unique_words_dict[next_word]] += 1	

likelihood_matrix = frequency_matrix.copy()
for row in range(frequency_matrix.shape[0]):
  if np.sum(frequency_matrix[row]) != 0:
    likelihood_matrix[row] /= np.sum(frequency_matrix[row])

M = likelihood_matrix

next = unique_words_dict["."]

response = "\n"
while response[-1] != "." and response != "!" and response[-1] != "?":
  next = np.random.choice(len(M[next]), 1, p=M[next])[0]
  if unique_words_dict2[next] == "." or unique_words_dict2[next] == ",":
    response = response + unique_words_dict2[next]
  else:
    response = response + " " + unique_words_dict2[next]

print(response)
