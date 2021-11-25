# Resolvi dividir o algoritmo em 3 partes

class TimSort():

    minimum = 32

    # Primeira: calcular o minirun mais eficiente

    def find_minrun(self, n):

        r = 0
        while n >= self.minimum:
            r |= n & 1
            n >>= 1
        return n + r

    # Segundo: implementar o insert sort pra organizar a listas menores

    def insert_sort(self, array, left, right):

        for i in range(left + 1, right + 1):
            element = array[i]
            j = i - 1

            while (element < array[j]) and (j >= left):
                array[j+1] = array[j]
                j -= 1

            array[j+1] = element

        return array

    # Terceiro: Fazer um merge das listas

    def merge_array(self, array, le, m, r):

        array_length = m - le + 1
        array_length2 = r - m
        left = []
        right = []
        for i in range(0, array_length):
            left.append(array[le + i])
        for i in range(0, array_length2):
            right.append(array[m + 1 + i])

        i = 0
        j = 0
        k = le

        while j < array_length2 and i < array_length:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < array_length:
            array[k] = left[i]
            k += 1
            i += 1

        while j < array_length2:
            array[k] = right[j]
            k += 1
            j += 1

    def tim_sort(self, array):
        n = len(array)
        minrun = self.find_minrun(n)

        for start in range(0, n, minrun):
            end = min(start + minrun - 1, n - 1)
            self.insert_sort(array, start, end)

        size = minrun
        while size < n:

            for left in range(0, n, 2 * size):

                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
                self.merge_array(array, left, mid, right)

            size = 2 * size

        return array
