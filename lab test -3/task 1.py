"""Interactive Stack implementation using a Python list.

The script prompts the user to enter 5 elements to push onto the stack.
It then asks whether the user wants to pop elements and offers two modes:
  1) Pop the top N elements
  2) Pop specific values (enter comma-separated values)

Remaining stack is displayed with the top shown first.
"""

class Stack:
	def __init__(self):
		self._items = []

	def push(self, item):
		self._items.append(item)

	def pop(self):
		if not self._items:
			raise IndexError("pop from empty stack")
		return self._items.pop()

	def pop_value(self, value):
		"""Remove the top-most occurrence of `value` from the stack.

		Searches from the top of the stack toward the bottom and removes
		the first matching occurrence.
		"""
		for i in range(len(self._items) - 1, -1, -1):
			if self._items[i] == value:
				return self._items.pop(i)
		raise ValueError(f"value not found in stack: {value}")

	def peek(self):
		if not self._items:
			return None
		return self._items[-1]

	def is_empty(self):
		return not self._items

	def size(self):
		return len(self._items)

	def display(self):
		# Show stack with top first for readability
		print("Stack (top->bottom):", list(reversed(self._items)))


def get_input_elements(count=5):
	"""Prompt the user to enter `count` elements. Returns list of strings."""
	elements = []
	print(f"Please enter {count} elements to push onto the stack (press Enter after each):")
	for i in range(1, count + 1):
		val = input(f"Element {i}: ")
		elements.append(val)
	return elements


def main():
	stack = Stack()

	# Get 5 elements from the user
	entries = get_input_elements(5)
	for e in entries:
		stack.push(e)

	print("\nCurrent stack:")
	stack.display()

	# Ask user if they want to pop elements
	resp = input("\nWould you like to pop elements from the stack? (y/n): ")
	if resp.strip().lower() != 'y':
		print("No pops requested. Final stack:")
		stack.display()
		return

	# Choose pop mode
	print("Choose pop mode:")
	print("  1) Pop top N elements (enter a number)")
	print("  2) Pop specific values by value (enter comma-separated values)")
	mode = input("Enter 1 or 2 [default 1]: ")

	popped = []
	if mode.strip() == '2':
		vals = input("Enter values to pop (comma-separated): ")
		values = [v.strip() for v in vals.split(',') if v.strip() != '']
		for v in values:
			try:
				popped_val = stack.pop_value(v)
				popped.append(popped_val)
			except ValueError:
				print(f"Value not found, skipping: {v}")
	else:
		default_n = 2
		n_resp = input(f"How many elements would you like to pop? [default {default_n}]: ")
		try:
			n = int(n_resp) if n_resp.strip() != '' else default_n
		except ValueError:
			print("Invalid number entered; using default.")
			n = default_n

		n = max(0, n)
		n = min(n, stack.size())
		for _ in range(n):
			popped.append(stack.pop())

	if popped:
		print("\nPopped elements (in pop order):", popped)
	else:
		print("\nNo elements were popped.")

	print("\nRemaining stack:")
	stack.display()


if __name__ == "__main__":
	main()

