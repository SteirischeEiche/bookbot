def get_book_text(path):
   with open(path) as f:
      contents_string = f.read()
   return contents_string

def main():
   contents = get_book_text("books/frankenstein.txt")
   print(contents)

def count_words(text_string):
   text_list = text_string.split()
   i = 0
   for word in text_list:
      i += 1
   return i

text = get_book_text("books/frankenstein.txt")
num_words = count_words(text)
print (f"{num_words} words found in the document")
