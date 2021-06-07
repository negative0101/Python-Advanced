n = [int(i) for i in input().split()]

positive = filter(lambda num: num >= 0, n)
negative = filter(lambda num: num < 0, n)
sum_positive = sum(positive)
sum_negative= sum(negative)

print(sum_negative)
print(sum_positive)
if sum_positive > abs(sum_negative):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')