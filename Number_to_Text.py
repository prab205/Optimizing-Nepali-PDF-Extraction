wordList = ['जिरो','एक','दुइ','तीन','चार','पाँच','छ','सात','आठ','नौ','दश','एघार','बाह्र','तेह्र','चौध','पन्ध्र','सोह्र','सत्र','अठार','उन्नाइस','विस','एक्काइस','बाइस','तेईस','चौविस','पच्चिस','छब्बिस','सत्ताइस','अठ्ठाईस','उनन्तिस','तिस','एकत्तिस','बत्तिस','तेत्तिस','चौँतिस','पैँतिस','छत्तिस','सैँतीस','अठतीस','उनन्चालीस','चालीस','एकचालीस','बयालीस','त्रियालीस','चवालीस','पैँतालीस','छयालीस','सच्चालीस','अठचालीस','उनन्चास','पचास','एकाउन्न','बाउन्न','त्रिपन्न','चउन्न','पचपन्न','छपन्न','सन्ताउन्न','अन्ठाउन्न','उनन्साठी','साठी','एकसट्ठी','बयसट्ठी','त्रिसट्ठी','चौंसट्ठी','पैंसट्ठी','छयसट्ठी','सतसट्ठी','अठसट्ठी','उनन्सत्तरी','सत्तरी','एकहत्तर','बहत्तर','त्रिहत्तर','चौहत्तर','पचहत्तर','छयहत्तर','सतहत्तर','अठहत्तर','उनासी','असी','एकासी','बयासी','त्रियासी','चौरासी','पचासी','छयासी','सतासी','अठासी','उनान्नब्बे','नब्बे','एकान्नब्बे','बयानब्बे','त्रियान्नब्बे','चौरान्नब्बे','पन्चानब्बे','छयान्नब्बे','सन्तान्नब्बे','अन्ठान्नब्बे','उनान्सय','सय']
numbers = list(range(0,101))
higher = ["सय","हज़ार","लाख","करोड़","अरब"]
numList = ['०','१','२','३','४','५','६','७','८','९','१०','११','१२','१३','१४','१५','१६','१७','१८','१९','२०','२१','२२','२३','२४','२५','२६','२७','२८','२९','३०','३१','३२','३३','३४','३५','३६','३७','३८','३९','४०','४१','४२','४३','४४','४५','४६','४७','४८','४९','५०','५१','५२','५३','५४','५५','५६','५७','५८','५९','६०','६१','६२','६३','६४','६५','६६','६७','६८','६९','७०','७१','७२','७३','७४','७५','७६','७७','७८','७९','८०','८१','८२','८३','८४','८५','८६','८७','८८','८९','९०','९१','९२','९३','९४','९५','९६','९७','९८','९९','१००']
def convert_to_words(num):
  newList = []
  l = len(str(num))

  # Base cases
  if (l == 0):
      print("empty string")
      return ''

  # if (l > 5):
  #     print("Length more than 4 is not supported")
  #     return
  crore = num//10000000
  if crore!=0:
    newList.append(wordList[crore])
    newList.append(higher[3])

  num = num % 10000000
  lakh = num//100000
  if lakh!=0:
    newList.append(wordList[lakh])
    newList.append(higher[2])

  num = num % 100000
  th = num//1000
  if th!=0:
    d = (num % 1000)//100
    if th>=10 or d==0 or l>5:
      newList.append(wordList[th])
      newList.append(higher[1])
      num = num % 1000

  hd = num//100
  if hd!=0:
    newList.append(wordList[hd])
    newList.append(higher[0])
  
  ones = num % 100
  if ones!=0:
    newList.append(wordList[ones])

  return newList

def convertToInt(input):
  l = list(input)
  num = 0
  newList = []
  power = len(l)-1
  ind = 0
  new = []
  for i in l:
    if i in numList:
      if l[ind] == numList[0]:
        newList.append(wordList[0])
        ind+=1
        power-=1
        continue
      else:
        num+=numbers[numList.index(i)] * pow(10,power)
        power-=1
        new = convert_to_words(num)
  return (newList+new)

def extractNum(input):
  l = list(input)
  a =''
  for i in l:
    if i in numList:
      input=input[1:]
      a+=i
    else:
      break
  ret = convertToInt(a)
  if input!='':
    ret.append(input)
  return ret

def getWords(A):
  A = A.split()
  output = []
  for i in A:
    for j in list(i):
      if j in numList:
        output+=extractNum(i)
        break
      else:
        output.append(i)
        break
  return " ".join(output)

A = "०३६ देखि नै राजनीतिमा लाग्नुभएका गुरुङ ०४२ मा अखिल छैठौँको अध्यक्ष हुनुभएको थियो।"
print(getWords(A))