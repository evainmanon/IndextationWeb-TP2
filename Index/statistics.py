import Index.tokenize_func as tkn

#Function which return the number of document in a list of document 
def number_docs(liste):
    return len(liste)

#Function which return the number of token in an index
def number_token(token):
    list_word = tkn.dico_keys(token)
    return len(list_word)

#Function which return de mean of token per document
def mean_token(token, liste):
    if number_docs(liste) == 0 :
        mean = 0
    else:
        mean = number_token(token)/number_docs(liste)
    return mean

#Function which create a dictionary which coutains the statistics of a list of document and his index
def create_dico_stat(token, liste): 
    stat = {}
    stat["Number of doc"] = number_docs(liste)
    stat["Number of token"] = number_token(token)
    stat["Mean of token per document"] = mean_token(token, liste)
    return stat

