from typing import List


def sort_list(values: List[int], reverse: bool = False) -> List[int]:
    """Return a new list containing `values` sorted.

    Uses insertion sort for clarity; set `reverse=True` for descending order.
    """
    sorted_values: List[int] = values[:]
    for i in range(1, len(sorted_values)):
        current_value = sorted_values[i]
        j = i - 1
        while j >= 0 and ((current_value < sorted_values[j]) if not reverse else (current_value > sorted_values[j])):
            sorted_values[j + 1] = sorted_values[j]
            j -= 1
        sorted_values[j + 1] = current_value
    return sorted_values


if __name__ == "__main__":
    raw_input_str = input("Enter numbers separated by spaces: ").strip()
    numbers = [int(x) for x in raw_input_str.split()] if raw_input_str else []
    print("Ascending:", sort_list(numbers))
    print("Descending:", sort_list(numbers, reverse=True))