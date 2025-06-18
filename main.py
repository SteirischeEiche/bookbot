def main():
   book_path ="books/frankenstein.txt"
   text_string = get_book_text(book_path)
   num_words = count_words(text_string)
   print(f"{num_words} words found in the document")
   dict_chars = count_chars(text_string)
   print(dict_chars)

from stats import get_book_text
from stats import count_words
from stats import count_chars

main()
