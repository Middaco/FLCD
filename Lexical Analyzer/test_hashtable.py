from hashtable import HashTable
from scanner import Scanner
from FA import FA

def test_hashtable():
    ht = HashTable()
    ht.add("aa")
    ht.add("bb")
    assert ht.search("aa") == ht.add("aa")
    assert ht.len == 2


def test_scanner():
    sc1 = Scanner("Token.in",
                  "p1.txt",
                  HashTable())

    sc1.scan()
    assert sc1.get_PIF()[0][0] == "--"
    assert sc1.get_PIF()[1] == "let"
    assert sc1.get_PIF()[2] == "a"


# test_hashtable()
# test_scanner()
fa = FA("C:\\Users\\Asus\\OneDrive\\Desktop\\Facultate\\Laboratoare\\An3-Semestu1-Engleza\\FLCD\\Lexical Analyzer\\FA.in")
fa.run()
