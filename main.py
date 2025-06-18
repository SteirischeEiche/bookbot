def main():
   book_path ="books/frankenstein.txt"
   text_string = get_book_text(book_path)
   num_words = count_words(text_string)
   print(f"{num_words} words found in the document")

def get_book_text(path):
   with open(path) as f:
      return f.read()

from stats import count_words

main()
