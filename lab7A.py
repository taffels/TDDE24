from books import *
from match import *

def search(pattern, db):
    """ Function that returns matching results from a pattern in a database """
    if not db:
        return []
    
    if match(db[0], pattern):
        return [db[0] + search(pattern, db[1:])]
    else:
        return search(pattern, db[1:])
                

if __name__ == "__main__":
    assert search(['--', ['titel', ['&', '&']], '--'], db) == [[['foerfattare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['aar', 2012]]]
    
    assert search([['foerfattare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['aar', '&']], db) == [[['foerfattare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], ['aar', 2010], 
                                                                                                            [['foerfattare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['aar', 2009]]]]
    
    assert search([['foerfattare', ['&', '&', '&']], '--', '--'], db) == [[['foerfattare', ['j', 'glenn', 'brookshear']], 
                                                                        ['titel', ['computer', 'science', 'an', 'overview']], ['aar', 2011]]]
    
    assert search(['--', '--', ['aar', 2042]], db) == []
    
    assert search(['--', '--', '--'], db) == [[['foerfattare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                                             ['aar', 2010], [['foerfattare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['aar', 2012], [['foerfattare', ['j', 'glenn', 'brookshear']], ['titel', ['computer', 'science', 'an', 'overview']], ['aar', 2011],
                                             [['foerfattare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['aar', 2009], 
                                            [['foerfattare', ['anders', 'haraldsson']], ['titel', ['programmering', 'i', 'lisp']], ['aar', 1993]]]]]]]
    
    assert search([['foerfattare', ['&', '&']], '--', '--'], db) == [[['foerfattare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], ['aar', 2010],
                                                                    [['foerfattare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['aar', 2012], 
                                                                    [['foerfattare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['aar', 2009], 
                                                                    [['foerfattare', ['anders', 'haraldsson']], ['titel', ['programmering', 'i', 'lisp']], ['aar', 1993]]]]]]
       
    assert search(['--', ['aar', 2042], '--'], db) == []

    assert search(['--'], db) ==  [[['foerfattare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                                             ['aar', 2010], [['foerfattare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['aar', 2012], [['foerfattare', ['j', 'glenn', 'brookshear']], ['titel', ['computer', 'science', 'an', 'overview']], ['aar', 2011],
                                             [['foerfattare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['aar', 2009], 
                                            [['foerfattare', ['anders', 'haraldsson']], ['titel', ['programmering', 'i', 'lisp']], ['aar', 1993]]]]]]]

    assert search([['&', ['anders', 'haraldsson']], '--'], db) == [[['foerfattare', ['anders', 'haraldsson']], ['titel', ['programmering', 'i', 'lisp']], ['aar', 1993]]]

    assert search([], db) == [] # No pattern
    assert search([],[]) == [] # No pattern
    assert search(['--', '--', '--'], []) == [] # No database
    assert search([['foerfattare', ['&', 'Larsson']], '--'], db) == [] # Not an author in database
    assert search((1, 2), db) == [] # Not a correct input

    print("The code passed all the tests")