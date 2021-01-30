import random

lotto_num = []
while len(lotto_num) < 6:
    random_num = random.randint(1, 45)
    if random_num not in lotto_num:
        lotto_num.append(random_num)
print(sorted(lotto_num))