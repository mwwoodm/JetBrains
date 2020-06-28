class Matrix:
    def __init__(self, ordinal):
        self.m = 0
        self.n = 0
        self.values = []
        self.ordinal = ordinal
        self.determinant = 0
        self.cofactors = []
        self.adjoint = []
        self.inverse = []

    def read_matrix(self):
        print(f'Enter size of {self.ordinal} matrix:')
        self.m, self.n = map(int, input().split())
        print(f'Enter {self.ordinal} matrix:')
        self.values = [list(map(float, input().split())) for i in range(self.m)]
        
    def print_matrix(self, result):
        print("The result is:")
        for i in result:
            print(*i)
        
    def add_matrices(self, other):
        result = [[self.values[i][j] + other.values[i][j] for j in range(self.n)] for i in range(self.m)]
        self.print_matrix(result)

    def multiply_constant(self, constant):
        result = [[self.values[i][j] * constant for j in range(self.n)] for i in range(self.m)]
        self.print_matrix(result)

    def multiply_matrices(self, other):
        if len(self.values[0]) != len(other.values):
            print("The operation cannot be performed.")
        else:
            result = [[0 for j in range(len(other.values[0]))] for i in range(len(self.values))]
            for i in range(len(self.values)):
                for j in range(len(other.values[0])):
                    for k in range(len(other.values)):
                        result[i][j] += self.values[i][k] * other.values[k][j]
        self.print_matrix(result)

    def invert_matrix(self):
        determinant = calculate_determinant(self.values)
        if len(self.values) == 2:
            return [[self.values[1][1] / determinant, -1 * self.values[0][1]/determinant],
                    [-1 * self.values[1][0] / determinant, self.values[0][0]/determinant]]
        for r in range(len(self.values)):
            cofactorRow = []
            for c in range(len(self.values)):
                minor = [row[: c] + row[c + 1:] for row in (self.values[: r] + self.values[r + 1:])]
                cofactorRow.append(((-1) ** (r + c)) * calculate_determinant(minor))
            self.inverse.append(cofactorRow)
        self.inverse = transpose_matrix(self.inverse, '1')
        for r in range(len(self.inverse)):
            for c in range(len(self.inverse)):
                self.inverse[r][c] = self.inverse[r][c] / determinant
        self.print_matrix(self.inverse)

def transpose_matrix(matrix, transpose_type):
    rows = len(matrix)
    cols = len(matrix[0])
    if transpose_type == '1':
        result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    if transpose_type == '2':
        temp = [[matrix[rows - 1 - i][cols - 1 - j] for j in range(cols)] for i in range(rows)]
        result = [[temp[j][i] for j in range(len(temp))] for i in range(len(temp[0]))]
    if transpose_type == '3':
        result = [[matrix[i][cols - 1 - j] for j in range(cols)] for i in range(rows)]
    if transpose_type == '4':
        result = [[matrix[rows - 1 - i][j] for j in range(cols)] for i in range(rows)]
    return(result)     

def calculate_determinant(matrix):
    m_rows = len(matrix)
    m_cols = len(matrix[0])
    if m_rows == m_cols:
        if m_rows == 1:
            return matrix[0][0]
        if m_rows == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        sub_m = [[matrix[i][j] for j in range(m_cols)] for i in range(m_rows)]
        del sub_m[0]
        cof_m = (m_rows - 1) * [(m_cols - 1) * [0]]
        determinant = 0
        for j in range(m_cols):
            for i in range(m_rows - 1):
                cof_m[i] = sub_m[i][0:j] + sub_m[i][j + 1:]

            determinant += (-1) ** (j % 2) * matrix[0][j] * calculate_determinant(cof_m)

        return determinant

while True:
    option = input('\n1. Add matrices\n' \
                    '2. Multiply matrix by a constant\n' \
                    '3. Multiply matrices\n' \
                    '4. Transpose matrix\n' \
                    '5. Calculate a determinant\n'
                    '6. Inverse matrix\n'
                    '0. Exit\nYour choice:\n')
    if option == '1':  # Add matrices
        a = Matrix('first')
        a.read_matrix()
        b = Matrix('second')
        b.read_matrix()
        a.add_matrices(b)
    elif option == '2':  # Multiply matrix by a constant
        a = Matrix('only')
        a.read_matrix()
        c = int(input("Enter constant:"))
        a.multiply_constant(c)
    elif option == '3':  # Multiply matrices
        a = Matrix('first')
        a.read_matrix()
        b = Matrix('second')
        b.read_matrix()
        a.multiply_matrices(b)
    elif option == '4':  # Transpose matrix
        transpose_type = input('\n1. Main diagonal\n' \
                                '2. Side diagonal\n' \
                                '3. Vertical line\n' \
                                '4. Horizontal line:\n')        
        a = Matrix('only')
        a.read_matrix()
        result = transpose_matrix(a.values, transpose_type)
        print(f'The result is:')
        for i in result:
            print(*i)
    elif option == '5':  # Calculate a determinant
        a = Matrix('only')
        a.read_matrix()
        a.determinant = calculate_determinant(a.values)
        print(f'The result is:\n{a.determinant}')
    elif option == '6':  # Inverse matrix
        a = Matrix('only')
        a.read_matrix()
        a.invert_matrix()
    elif option == '0':  # Exit
        exit()
