from googletrans import Translator
translator = Translator()
text = input("Enter any text: ")
detected = translator.detect(text)
trans = translator.translate(text,src='en',dest='te')
print(f"The language detected is {detected.lang}")
print(f"After transalation : {trans.text}")