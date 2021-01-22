

class Matrix:
    def __init__(self, matr):
        self.matr = matr
        self.rows = len(matr)

    def __str__(self):
        st = []
        for ind,row in enumerate(self.matr):
            if ind == 0:
                st.append('\u23A1')
            elif ind == self.rows -1:
                st.append('\u23A3')
            else:
                st.append('\u23A2')
            for el in row:
                st.append("{:3}".format(el))
            if ind == 0:
                st.append('\u23A4')
            elif ind == self.rows -1:
                st.append('\u23A6')
            else:
                st.append('\u23A5')
            st.append('\n')
        return "".join(st)
    
    def __add__(self,other):
        new_matr = []
        for val in zip(self.matr, other.matr):
            new_matr.append([sum([m,n]) for m,n in zip(*val)])
        return Matrix(new_matr)


b = Matrix([[1,2,3],[1,2,3],[1,2,3]])
c = Matrix([[4,4,4],[5,5,5],[6,6,6]])
a = Matrix([[7,8,9,10],[11,12,13,14]])
print(f'Matrix 1: \n-------\n{a}\n')
print(f'Matrix 2: \n-------\n{b}\n')
print(f'Matrix 3: \n-------\n{c}\n')
print(f'Matrix 2 + Matrix 3: \n-------\n{b+c}')
