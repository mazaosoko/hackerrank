if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = sorted(list({record[1] for record in records}))
    second_lowest = sorted([
        record[0] for record in records if record[1] == scores[1]
    ])
    for name in second_lowest:
        print(name)
