def create_earrings(white_gold, yellow_gold):
    pairs_created = 0
    leftover_gold = 0

    for white, yellow in zip(white_gold, yellow_gold):
        while white + yellow >= 10:
            if white + yellow == 10:
                pairs_created += 1
                break
            else:
                yellow -= 2

        if white + yellow < 10:
            leftover_gold += white + yellow

    while leftover_gold >= 10 and pairs_created < 7:
        pairs_created += leftover_gold // 10
        leftover_gold %= 10

    if pairs_created >= 7:
        print(f"Great success, you created {pairs_created} earrings.")
    else:
        needed_earrings = 7 - pairs_created
        print(f"Keep trying, you need {needed_earrings} more earrings.")

white_gold = list(map(int, input().split()))
yellow_gold = list(map(int, input().split()))

create_earrings(white_gold, yellow_gold)
