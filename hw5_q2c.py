import numpy as np

def get_random_movement():
    coin_flip = np.random.uniform()
    movement = 1
    if coin_flip < 0.5:
        movement = -1
    return movement

def get_times_crossed_origin(n_steps):
    pos = 0
    prev_pos = 0
    origin_cross_counter = 0

    for _ in range(n_steps):
        movement = get_random_movement()
        next_pos = pos + movement
        if (prev_pos < 0 and next_pos > 0) or (prev_pos > 0 and next_pos < 0):
            origin_cross_counter += 1
        prev_pos = pos
        pos = next_pos

    return origin_cross_counter

if __name__ == "__main__":
    for t in [4 * 10**4, 9 * 10**4, 16 * 10**4]:
        origin_cross_counts = []
        for i in range(50):
            origin_cross_counts.append(get_times_crossed_origin(t))
        print(f"average times the particle crossed the origin for t={t}: {np.mean(origin_cross_counts)}")
        print(f"\tstd dev: {np.std(origin_cross_counts)}")
