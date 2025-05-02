francisco = 1.50
sara = 1.10
anos = 0
while True:
    francisco += 0.02
    sara += 0.03
    anos += 1
    if francisco < sara:
        break

print(f"Foram necessários {anos} anos para que Sara seja mais alta que Francisco.")