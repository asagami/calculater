from PyQt4 import QtCore, QtGui, uic
import sys
import operator as op
from plyplus import Grammar, STransformer
from tkinter import *
calc_grammar = Grammar("""
    start: add;
    ?add: (add add_symbol)? mul;
    ?mul: (mul mul_symbol)? atom;
    @atom: neg | number | '\(' add '\)';
    neg: '-' atom;
    number: '[\d.]+';
    mul_symbol: '\*' | '/';
    add_symbol: '\+' | '-';
    WS: '[ \t]+' (%ignore);
""")

class Calc(STransformer):

    def _bin_operator(self, exp):
        arg1, operator_symbol, arg2 = exp.tail

        operator_func = { '+': op.__add__, '-': op.__sub__, '*': op.__mul__, '/': op.__truediv__ }[operator_symbol]

        return operator_func(arg1, arg2)

    number      = lambda self, exp: float(exp.tail[0])
    neg         = lambda self, exp: -exp.tail[0]
    __default__ = lambda self, exp: exp.tail[0]

    add = _bin_operator
    mul = _bin_operator

qtCreatorFile = "CALCULATER.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.one.clicked.connect(self.on)
        self.two.clicked.connect(self.tw)
        self.three.clicked.connect(self.th)
        self.four.clicked.connect(self.fo)
        self.five.clicked.connect(self.fi)
        self.six.clicked.connect(self.si)
        self.seven.clicked.connect(self.se)
        self.eight.clicked.connect(self.ei)
        self.nine.clicked.connect(self.ni)
        self.zero.clicked.connect(self.ze)
        self.jia.clicked.connect(self.plus)
        self.jian.clicked.connect(self.ji)
        self.cheng.clicked.connect(self.ch)
        self.chu.clicked.connect(self.cu)
        self.point.clicked.connect(self.pi)
        self.kuohao1.clicked.connect(self.k1)
        self.kuohao2.clicked.connect(self.k2)
        self.delete_2 .clicked.connect(self.de)
        self.clear.clicked.connect(self.cle)
        self.equal.clicked.connect(self.cal)
    def on (self):
           self.textEdit_2.insertPlainText('1')
    def tw (self):
           self.textEdit_2.insertPlainText('2')
    def th (self):
           self.textEdit_2.insertPlainText('3')
    def fo (self):
           self.textEdit_2.insertPlainText('4')
    def fi (self):
           self.textEdit_2.insertPlainText('5')
    def si (self):
           self.textEdit_2.insertPlainText('6')
    def se (self):
           self.textEdit_2.insertPlainText('7')
    def ei (self):
           self.textEdit_2.insertPlainText('8')
    def ni (self):
           self.textEdit_2.insertPlainText('9')
    def ze (self):
           self.textEdit_2.inputPlainText('0')
    def plus (self):
           self.textEdit_2.insertPlainText('+')
    def ji (self):
           self.textEdit_2.insertPlainText('-')
    def ch (self):
           self.textEdit_2.insertPlainText('*')
    def cu (self):
           self.textEdit_2.insertPlainText('/')
    def k1 (self):
           self.textEdit_2.insertPlainText('(')
    def k2 (self):
           self.textEdit_2.insertPlainText(')')
    def pi (self):
           self.textEdit_2.insertPlainText('.')
    def cle (self):
           self.textEdit_2.clear()
           self.label.setText('')
    def de (self):
           self.textEdit_2.undo()
    def cal(self):
         s=(self.textEdit_2.toPlainText())
         calc = Calc()
         tree = calc_grammar.parse(s)
         t=calc.transform(tree)
         self.label.setText('='+str (t))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
