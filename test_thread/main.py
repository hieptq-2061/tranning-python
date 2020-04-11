from countThread import CountThread


try:
    t1 = CountThread('thread1')
    t2 = CountThread('thread2')
    t1.start()
    t2.start()
except Exception as e:
    print(e)
