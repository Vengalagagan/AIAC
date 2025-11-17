# To-Do List App

Simple interactive To-Do list implemented with HTML, CSS and JavaScript.

Features
- Add task
- Delete task
- Mark task as completed (checkbox)
- Persist tasks in `localStorage`

How to run
1. Open `todo-app/index.html` in a web browser (double-click or open from browser File → Open).
2. Add tasks using the input and `Add` button.
3. Mark tasks complete with the checkbox or delete them with the `Delete` button.

Notes on AI assistance
- **Modularity:** Functions (`addTask`, `toggleComplete`, `deleteTask`, `render`) separate concerns for clarity and testability.
- **Usability:** Clear, accessible controls and labels were added (aria-labels, keyboard-friendly form submit).
- **Persistence:** `localStorage` added so tasks remain across page loads.
- **Maintainability:** Simple data model (`{id, text, completed}`) makes future features (edit, sorting) easy to add.

If you'd like, I can add editing, filtering (all/active/completed), or keyboard shortcuts next.
