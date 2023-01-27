import requests

from bs4 import BeautifulSoup

#Function which take a title in the html.parser with the url  
def get_title(url):
    try : 
        site = requests.get(url)
        site_html = BeautifulSoup(site.text, 'html.parser')
        return site_html.title.string
    except  : 
        return None

#Function which return a list of title with a list of url
def list_title(liste):
    list_title = []
    for url in liste : 
        list_title.append(get_title(url))
    return list_title

#Function which return a list with words which are countains in a title
def list_word(title) : 
    liste_word = []
    if title == None or title == '403 Forbidden' :
        return liste_word
    else:
        i = 0
        list_esp = [0]
        for i in range (0, len(title)): 
            if title[i] == " ":
                list_esp.append(i)
        list_esp.append(len(title))

        liste_word.append(title[list_esp[0]:list_esp[1]])
        for k in range(1, len(list_esp)-1): 
            if title[list_esp[k]+1:list_esp[k+1]] != '':
                liste_word.append(title[list_esp[k]+1:list_esp[k+1]])
        return liste_word

#Function which return the indice of a word in a list of list of word and number, if the word is not in the list, the function return -1
def search_word(word, list): 
    ind = -1 
    if list == []:
        return -1
    else:
        for i in range (0, len(list)):
            if list[i][0] == word:
                ind = i 
        return ind 

#Function which return the indice of a word in a list of word, if the word is not in the list, the function return -1
def search_word_1(word, list): 
    ind = -1 
    if list == []:
        return -1
    else:
        for i in range (0, len(list)):
            if list[i] == word:
                ind = i 
        return ind 

#Function which return the index for one document with a title
def token_title(title):
    list_token = []
    list_word_title = list_word(title)
    for word in list_word_title : 
        if search_word(word, list_token)==-1:
            list_token.append([word, 1])
        else:
            list_token[search_word(word, list_token)][1] += 1
    return list_token

#Function which return the list of keys of a dico
def dico_keys(dico):
    keys = []
    for key in dico.keys():
        keys.append(key)
    return keys

#Function which return the list of ind of apparition of a word in a title
def list_ind(title, word):
    liste_ind = []
    liste_word = list_word(title)
    for i in range(0, len(liste_word)): 
        if liste_word[i] == word:
            liste_ind.append(i)
    return liste_ind

#Function which return an non-positional index
def index_non_pos(liste): 
    token_list = {}
    for i in range (0,len(liste)) : 
        token_title_liste = token_title(liste[i])
        for j in range (0,len(token_title_liste)):
            if search_word_1(token_title_liste[j][0], dico_keys(token_list)) == -1 : 
                token_list[token_title_liste[j][0]] = [[i, token_title_liste[j][1]]]
            else :
                token_list[token_title_liste[j][0]].append([i, token_title_liste[j][1]])
    return token_list

#Function which return a positional index
def index_pos(liste):
    token_list = {}
    for i in range (0,len(liste)) : 
        token_title_liste = token_title(liste[i])
        for j in range (0,len(token_title_liste)):
            liste_ind = list_ind(liste[i],token_title_liste[j][0])
            if search_word_1(token_title_liste[j][0], dico_keys(token_list)) == -1 : 
                token_list[token_title_liste[j][0]] = [[i, token_title_liste[j][1], liste_ind]]
            else :
                token_list[token_title_liste[j][0]].append([i, token_title_liste[j][1], liste_ind])
    return token_list