from problems.lru_cache import LRUCache

def test_lru_cache():
    cache = LRUCache(5)

    cache.put(10,3)
    cache.put(20,10)
    cache.put(30,50)
    cache.put(40,100) 

    assert cache.get(40) == 100

    cache.put(40,300)
    
    assert cache.get(40) == 300
    
    cache.put(50,400)  
    cache.put(60,1000)  
          
    assert cache.get(10) == 3
