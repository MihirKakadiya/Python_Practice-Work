for i in range(2,21):
    with open(f"tables/multi{i}.txt", 'w')as f:
        for j in range(11):
            f.write(f"{i}X{j}={i*j}\n")
