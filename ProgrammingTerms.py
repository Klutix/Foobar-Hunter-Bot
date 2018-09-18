import random

def GeneratePhrase(KeywordQuanity):
    KeywordsA = ['Python','Javascript','Haskell','C#','C++','java','CSharp','kotlin']
                
    KeywordsB =['permutate','mutex','monad','lamda','api','service APIs','stack','dictionary','functions','reverse','algorithm','branch list','database connection'
                'Go (programming language)','client-side','Sawzall','regex','natural expressions','chrome','SQL','query','Latebind','upperbound','lowerbound','break','garbage collection','doEvenmts','yeild',
                'cryptographically','cipher','extensions','thread','safe','Programming','coding','Hex','Byte','Binary','Tuple','Android','Git','exclude','inlclude'
                'loop','automate','declare','server','decrypt','program','script','scripting','expressions','multithreading','objects','lists','append','array','pointer','reference','cascading','failures','comprehensive list']
                                  
    phrase =  random.choice(KeywordsA) + " "
    for i in range(0,KeywordQuanity):
        phrase += random.choice(KeywordsB)+ " "
    return phrase

def get_from_winning_list():
    key_words = ["mutex lock","headless chrome","array list java","mutual exclusion","angular javascript directive","python command line arguments"]
    return random.choice(key_words)
