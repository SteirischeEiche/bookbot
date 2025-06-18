def count_words(string):
   text_list = string.split()
   return len(text_list)

def get_book_text(path):
   with open(path) as f:
      return f.read()

def count_chars(string):
   dic = {}
   text_lower = string.lower()

   for char in text_lower:
      if char in dic:
         dic[char] += 1
      else:
         dic[char] = 1

   return dic
