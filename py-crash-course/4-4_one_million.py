# milly = list(range(1, 1_000_001))

# print(milly)

milly = []

for mill in range(1, 1_000_001):
    milly.append(mill)
    print(mill)
    # print(f"\n The sum so far is: {sum(milly)}")

print(f"\nThe minimum is {min(milly)}, the maximum is {max(milly)}")
print(f"\nAlso, the sum of all these numbers is:\n\n {sum(milly)}")

# min(mill)