import pyttsx3
import pypdf


droid = pyttsx3.init()
droid.say("Bonjour je suis un droid de la 3eme generation et je suis siris")
droid.say("maintenant tu peux te relaxer et dormir je m'occuppe de tout")

""" livre = open("EPS Assigment3 on Web development", 'rb')
lecture = pypdf.PdfFileReader(livre)
pages = lecture.numpages
print(pages)
debutlecture = lecture.getpage(0)
text = debutlecture.extractText()
droid.say(text)  """

droid.runAndWait()
































