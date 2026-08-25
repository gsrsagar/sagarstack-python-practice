

#I want set for uniqueness , but also I want it to be immutable
# non changable means it is frozenSets

frozenSetExp = frozenset({2,3})
forozenSetExp2 = frozenset({1,4,5,6})
print(frozenSetExp)
print(forozenSetExp2)

print(forozenSetExp2.union(frozenSetExp))
print(forozenSetExp2.intersection(frozenSetExp))
print(frozenSetExp.difference(forozenSetExp2))
print(frozenSetExp.symmetric_difference(forozenSetExp2))
print(forozenSetExp2.issubset({1}))
print(forozenSetExp2.issuperset({1,4,5,6}))
print(frozenSetExp.isdisjoint(forozenSetExp2))
