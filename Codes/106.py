def generate_matrix():
    matrix = []
    for _ in range(5):
        row = [0] * 5
        matrix.append(row)
    return matrix
        
if __name__ == '__main__':
    matrix = generate_matrix()
    print(matrix)
