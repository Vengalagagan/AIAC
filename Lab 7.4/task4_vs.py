def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):  # Avoid division by zero and i == j
            denominator = values[j] - values[i]
            if denominator != 0:
                ratio = values[i] / denominator
                results.append((i, j, ratio))
            else:
                results.append((i, j, None))  # Or handle as needed
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
