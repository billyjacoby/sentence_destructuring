import nltk
from nltk.corpus import wordnet

input_sentence = raw_input("Please enter a sentence to be evaluated: ")
# input_sentence = "The dog eats food"
print("\n")
print("\t" + input_sentence)
print("\n\n")
raw_input("Press enter to continue...")
print("\n\n")

tokenized_text = nltk.word_tokenize(input_sentence)
tagged_text = nltk.pos_tag(tokenized_text)

print("\n")
print("\t"),
print(tagged_text)
print("\n\n")
raw_input("Press enter to continue...")
print("\n\n")
output_sentence = ""

synonyms = []
for word in tokenized_text:
    word_syns = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            word_syns.append(str(l.name()))
    output_sentence += word + str(word_syns) + "\n\n"
print (output_sentence)
