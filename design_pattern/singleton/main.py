from sub1 import sub1_func
from sub2 import sub2_func
from singleton import Singleton

if __name__ == '__main__':
    sub1_func()
    sub2_func()
    s = Singleton()
    print(s.__dict__)