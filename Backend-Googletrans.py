import googletrans
from googletrans import Translator
translator=Translator()
text=str(input('Enter the text:'))
option=""
language_code=['af','afrikaans','sq','albanian','am','amharic','ar','arabic',
'hy','armenian','az','azerbaijani','eu','basque','be','belarusian','bn','bengali','bs','bosnian','bg','bulgarian','ca','catalan',
'ceb','cebuano','ny','chichewa','zh-cn','chinese','zh-tw','chinese','co','corsican','hr','croatian','cs','czech','da','danish',
'nl','dutch','en','english','eo','esperanto','et','estonian','tl','filipino','fi','finnish','fr','french','fy','frisian',
'gl','galician','ka','georgian','de','german','el','greek','gu','gujarati','ht','haitian creole','ha','hausa','haw','hawaiian',
'iw','hebrew','he','hebrew','hi','hindi','hmn','hmong','hu','hungarian','is','icelandic','ig','igbo','id','indonesian',
'ga','irish','it','italian','ja','japanese','jw','javanese','kn','kannada','kk','kazakh','km','khmer','ko','korean',
'ku','kurdish','ky','kyrgyz','lo','lao','la','latin','lv','latvian','lt','lithuanian','lb','luxembourgish','mk','macedonian',
'mg','malagasy','ms','malay','ml','malayalam','mt','maltese','mi','maori','mr','marathi','mn','mongolian','my','myanmar',
'ne','nepali','no','norwegian','or','odia','ps','pashto','fa','persian','pl','polish','pt','portuguese','pa','punjabi',
'ro','romanian','ru','russian','sm','samoan','gd','scots gaelic','sr','serbian','st','sesotho','sn','shona','sd','sindhi',
'si','sinhala','sk','slovak','sl','slovenian','so','somali','es','spanish','su','sundanese','sw','swahili','sv','swedish',
'tg','tajik','ta','tamil','te','telugu','th','thai','tr','turkish','uk','ukrainian','ur','urdu','ug','uyghur','uz','uzbek','vi',
'vietnamese','cy','welsh','xh','xhosa','yi','yiddish','yo','yoruba','zu','zulu',]
def inp_user():
    global option
    print("To Translate into English: Press 1\nTo Translate into Preferred language: Press 2\nTo Detect the Language: Press 3")
    option = int(input("Enter 1 or 2 or 3 :"))
    print(option)
    if (option==1 or option==2 or option==3):
        return
    else:
        inp_user()
inp_user()

if (option==1):
    translate=translator.translate(text,dest='en')
    print(translate.text)

if (option==2):
    def check_langcode():
        global dest
        dest=str(input("Enter the language code to be translated to: "))
        if dest in language_code:
            return
        else:
            check_langcode()
    check_langcode()
    translate=translator.translate(text,dest=dest)
    print (translate.text)

if (option==3):
    translate=translator.detect(text)
    lang_short=(translate.lang)
    print (language_code[((language_code.index(lang_short))+1)])
