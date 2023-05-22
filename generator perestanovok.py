import itertools

def generate_permutations(items):
    permutations = list(itertools.permutations(items))
    return permutations

elements = input("Введите элементы через пробел: ").split()

result = generate_permutations(elements)

print("Все перестановки:", result)
