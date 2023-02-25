from textblob import TextBlob
a = TextBlob('Quelle plat avez vous manger hier?')
#print(a.detect_language())
print(a.translate(from_lang= 'fr', to='en'))