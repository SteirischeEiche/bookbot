def main():
   import sys
   if not len(sys.argv) == 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   book_path = sys.argv[1]

   text_string = get_book_text(book_path)
   num_words = count_words(text_string)
   dict_chars = count_chars(text_string)

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}...")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   
   print("--------- Character Count -------")
   sorted_list = make_list(dict_chars)
   for dic in sorted_list:
      if dic["char"].isalpha():
         char = dic["char"]
         num = dic["num"]
         print(f"{char}: {num}")
   print("============= END ===============")

from stats import get_book_text
from stats import count_words
from stats import count_chars
from stats import make_list

main()
