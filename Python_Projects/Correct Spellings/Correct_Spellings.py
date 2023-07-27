
# //pip install pyspellchecker

from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter A Word :- ")

if word in corrector:
    print("Word is Correct")
    
else :
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)
        
    
# Output:
#Enter A Word :- Pyython
# Correct Spelling is  python