import numpy as np

def get_random_vote():
    coinflip = np.random.uniform()
    if coinflip < 0.52:
        return 1
    return -1

def get_voter_majority(n_voters):
    votes = np.array([get_random_vote() for _ in range(n_voters)])
    one_count = len(np.where(votes == 1)[0])
    negative_one_count = len(np.where(votes == -1)[0])
    if one_count > negative_one_count:
        return 1
    return -1

if __name__ == "__main__":
    # parts a, b, and c
    for sample_size in [20, 100, 400]:
        times_1_was_majority = 0
        for i in range(100):
            if get_voter_majority(sample_size) == 1:
                times_1_was_majority += 1
        print(f"probability that 1 was the majority with sample size = {sample_size}: {times_1_was_majority / 100}")

    # last part
    times_1_was_majority = 0
    sample_size_to_get_0_9 = 1000
    for i in range(100):
        if get_voter_majority(sample_size_to_get_0_9) == 1:
            times_1_was_majority += 1
    print(f"probability that 1 was the majority with sample size = {sample_size_to_get_0_9}: {times_1_was_majority / 100}")


