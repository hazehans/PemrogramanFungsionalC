# kegiatan 1

# bentuk fungsi biasa :
# fungsi pengurangan
#def minus (firstNum, secondNum) :
#    print (firstNum - secondNum)

# fungsi perkalian
#def mult (firstNum, secondNUm) :
#    print (firstNum * secondNUm)

# fungsi pembagian
#def div (firstNum, secondNum) :
#    print (firstNum / secondNum)

# minus (5, 2)
# mult (17, 23)
# div (3, 31)

# bentuk fungsi tree :
def tree(node) :
    if type (node) in (int, float) :
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)

#ekspresi sesuai modul (2+3) * (5-1), maka :
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))

result = tree(expression_tree)

print("hasil : ", result)




