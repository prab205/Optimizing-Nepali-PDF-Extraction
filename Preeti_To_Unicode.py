#https://github.com/globalpolicy/PreetiToUnicode
#added special characters that are caused by “, ”, ;

unicodeatoz=["ब","द","अ","म","भ","ा","न","ज","ष्","व","प","ि","फ","ल","य","उ","त्र","च","क","त","ग","ख","ध","ह","थ","श"]
unicodeAtoZ=["ब्","ध","ऋ","म्","भ्","ँ","न्","ज्","क्ष्","व्","प्","ी","ः","ल्","इ","ए","त्त","च्","क्","त्","ग्","ख्","ध्","ह्","थ्","श्"]
unicode0to9=["ण्","ज्ञ","द्द","घ","द्ध","छ","ट","ठ","ड","ढ"]
symbolsDict=\
{
    "~":"ञ्",
    "`":"ञ",
    "!":"१",
    "@":"२",
    "#":"३",
    "$":"४",
    "%":"५",
    "^":"६",
    "&":"७",
    "*":"८",
    "(":"९",
    ")":"०",
    "-":"(",
    "_":")",
    "+":"ं",
    "[":"ृ",
    "{":"र्",
    "]":"े",
    "}":"ै",
    "\\":"्",
    "|":"्र",
    ";":"स",
    ":":"स्",
    "'":"ु",
    "\"":"ू",
    ",":",",
    "<":"?",
    ".":"।",
    ">":"श्र",
    "/":"र",
    "?":"रु",
    "=":".",
    "ˆ":"फ्",
    "Î":"ङ्ख",
    "Í":"ङ्क",
    "å":"द्व",
    "÷":"/"
}

    #arranging certain characters, symbols for proper output
def normalizePreeti(preetitxt):
    normalized=''
    previoussymbol=''
    preetitxt=preetitxt.replace('qm','s|')
    preetitxt=preetitxt.replace('f]','ो')
    preetitxt=preetitxt.replace('km','फ')
    preetitxt=preetitxt.replace('0f','ण')
    preetitxt=preetitxt.replace('If','क्ष')
    preetitxt=preetitxt.replace('if','ष')
    preetitxt=preetitxt.replace('cf','आ')

    #my changes
    preetitxt=preetitxt.replace('O{', '')
    preetitxt=preetitxt.replace('Í', '')
    preetitxt=preetitxt.replace('æ', '') #opening quotation
    preetitxt=preetitxt.replace('Æ', '') #closing quotation
    preetitxt=preetitxt.replace('Ù', '') #;
    preetitxt=preetitxt.replace('«', '|')
    preetitxt=preetitxt.replace('¿', '?') #dirga ru


    index=-1
    while index+1 < len(preetitxt):
        index+=1
        character=preetitxt[index]
        try:
            #for rearranging र् 
            if preetitxt[index+2] == '{':
                temp=preetitxt[index+1]
                if temp=='f' or temp=='ो' or temp=='}' or temp=='L':
                    normalized+='{'+character+temp
                    index+=2
                    continue
            if preetitxt[index+1] == '{':
                if character!='f':
                    normalized+='{'+character
                    index+=1
                    continue
        except IndexError:
            pass
        if character=='l':
            previoussymbol='l'
            continue
        else:
            normalized+=character+previoussymbol
            previoussymbol=''
    return normalized

def convert(preeti):
    converted=''
    normalizedpreeti=normalizePreeti(preeti)
    for index, character in enumerate(normalizedpreeti):
        try:
            if ord(character) >= 97 and ord(character) <= 122:
                converted+=unicodeatoz[ord(character)-97]
            elif ord(character) >= 65 and ord(character) <= 90:
                converted+=unicodeAtoZ[ord(character)-65]
            elif ord(character) >= 48 and ord(character) <= 57:
                converted+=unicode0to9[ord(character)-48]
            else:
                converted+=symbolsDict[character]
        except KeyError:
            converted+=character
            
    return converted

print(convert("\u200c"))