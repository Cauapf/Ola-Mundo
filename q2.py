t = int(input())

h = t // 3600
resto = t % 3600

m = resto // 60
s = resto % 60

print(f"{h}:{m}:{s}")