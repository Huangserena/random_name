from random import randrange
from random import sample

#read the files    
infile = open('femalenames.txt', 'r')
content_female = infile.readlines()
infile.close()

infile = open('malenames.txt', 'r')
content_male = infile.readlines()
infile.close()

infile = open('surnames.txt', 'r')
content_surname = infile.readlines()
infile.close()

def name_only(x:list)->list:
    #only return the name as a list
    result =[]
    for i in x:
        result = result +[(i.split()[0])]
    return result

femalenames = name_only(content_female)
malenames = name_only(content_male)
surnames= name_only(content_surname)
  
def single_random_name(L:list)->str:
    #randomly return one name
    x = sample(L, 1)
    return x[0].capitalize()

def single_random_fullname()->str:
    surname = single_random_name(surnames)
    x =randint(1,2)
    if (x == 1):
        firstname = single_random_name(malenames)
    else:
        firstname = single_random_name(femalenames)
    return firstname +' '+ surname
    
def random_names(x:int)->list:
    result =[]
    for i in range(x):
        result.append(single_random_fullname())
    return result

random_names(5)