from exercise3 import Counter

# increment, decrement, reset, get_count

def test_increment():
    count = Counter()

    count.increment()
    count.increment() 

    assert count.get_count() == 2

def test_decrement():
    count = Counter()

    count.decrement()
    count.decrement()

    assert count.get_count() == -2

def test_reset():
    count = Counter()

    count.decrement()
    count.decrement()
    count.decrement()
    count.decrement()
    count.decrement()
    count.decrement()

    assert count.get_count() == -6

    count.reset()

    count.get_count == 0 
     
