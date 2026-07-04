def fun():
    x=300
    def fun2():
        nonlocal x
        def fun3():
            nonlocal x
            x=200
            print(x)
        fun3()
    print(x)
    fun2()
    print(x)
fun()