class MyArithmeticError(ArithmeticError):
    def __init__(self, msg):
        ArithmeticError.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg