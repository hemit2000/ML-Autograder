def calculateMean(array):
    mean = 0
    for i in range(len(array)):
        mean += array[i]
    mean /= len(array)
    return mean

array = [4, 9, 3, 5]
mean = calculateMean(array)
print(mean)
