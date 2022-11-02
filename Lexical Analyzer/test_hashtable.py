from hashtable import HashTable

def test_hashtable():
    ht = HashTable(10)
    print(ht.add("aa"))
    print(ht.add("bb"))
    print(ht.add("aa"))

test_hashtable()