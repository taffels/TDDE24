from books import db
from match import match


def search(lista, db):
    return match(lista, db)


def idiotfunktion():
    pass





input1 = [['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']]

output1 = [[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction',
'to', 'computer', 'science']], ['år', 2010]], [['författare', ['john', 'zelle']], ['titel',
['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år', 2009]]]


input2 = ['--', ['år', 2042], '--']
output2 = []

input3 = ['--', ['titel', ['&', '&']], '--']
output3 = [[['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]]]

