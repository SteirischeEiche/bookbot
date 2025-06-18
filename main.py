def get_book_text(path):
   with open(path) as f:
      contents_string = f.read()
   return contents_string

def main():
   contents = get_book_text("books/frankenstein.txt")
   print(contents)

main()
