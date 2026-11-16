import random

def f(x): return x ** 2
BITS, POP, GEN, PC, PM = 5, 6, 20, 0.8, 0.05    # x in 0..31

def decode(c):  return int(''.join(map(str, c)), 2)
def fitness(c): return f(decode(c))

def select(pop):
    a, b = random.sample(pop, 2)
    return max(a, b, key=fitness)

def crossover(p1, p2):
    if random.random() < PC:
        pt = random.randint(1, BITS-1)
        return p1[:pt]+p2[pt:], p2[:pt]+p1[pt:]
    return p1[:], p2[:]

def mutate(c):
    return [1-b if random.random() < PM else b for b in c]

pop = [[random.randint(0,1) for _ in range(BITS)] for _ in range(POP)]
for g in range(GEN):
    new = []
    while len(new) < POP:
        c1, c2 = crossover(select(pop), select(pop))
        new += [mutate(c1), mutate(c2)]
    pop = new[:POP]
    best = max(pop, key=fitness)
    print(f"Gen {g+1}: best x = {decode(best)}, f(x) = {fitness(best)}")
