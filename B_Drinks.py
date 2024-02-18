n_drink = int(input())

fraction = map(int, input().split())

output = sum(fraction)/n_drink

print("{:.4f}".format(output))