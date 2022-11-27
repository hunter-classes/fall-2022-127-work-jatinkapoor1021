
#EXTRA:
#Second extra completed:
#Handle punctuation

import re

dictionary_of_translations  = {
    "hi": "hey",
    "buddy": "matey",
    "people": "landlubbers",
    "are": "can",
    "not": "hat",
    "like": "used", 
    "guys": "scurvey dogs",
    "before": "afore",
    "earlier": "afore",
    "the": "th'",
    "mean": "nicerieds",
   "silly": "monkeys",
   "translator": "lurking",
   "understanding": "getting"
   
}

def fix_format(output_list):
   
   final_answer = ''
   final_answer = ' '.join(output_list)
   final_answer = re.sub(r' ([^A-Za-z0-9])', r'\1', final_answer)
   
   return final_answer

def translate(original_text):
   
   text = original_text.lower()
   text = re.findall("[\w'\"]+|[,.!?]", text)
   output_list = []
   
   for x in text:
        if x in dictionary_of_translations:
           output_list.append(dictionary_of_translations[x])
        elif x in "[\w'\"]+|[,.!?]":
           output_list.append(x)

   return fix_format(output_list)   
  

f = open('input.txt')
sentence = f.read()
print(translate(sentence))
f.close()
