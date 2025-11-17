// Simple To-Do app using localStorage for persistence

const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const list = document.getElementById('task-list');
const counts = document.getElementById('counts');
const clearCompletedBtn = document.getElementById('clear-completed');

let tasks = JSON.parse(localStorage.getItem('todo_tasks') || '[]');

function save() {
  localStorage.setItem('todo_tasks', JSON.stringify(tasks));
}

function render() {
  list.innerHTML = '';
  if (tasks.length === 0) {
    counts.textContent = 'No tasks';
    return;
  }

  tasks.forEach(task => {
    const li = document.createElement('li');
    li.className = 'task-item' + (task.completed ? ' completed' : '');
    li.dataset.id = task.id;

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = !!task.completed;
    checkbox.setAttribute('aria-label', 'Mark task completed');

    const span = document.createElement('span');
    span.className = 'text';
    span.textContent = task.text;

    const del = document.createElement('button');
    del.className = 'delete';
    del.textContent = 'Delete';
    del.setAttribute('aria-label', 'Delete task');

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(del);
    list.appendChild(li);
  });

  const remaining = tasks.filter(t => !t.completed).length;
  counts.textContent = `${remaining} task${remaining !== 1 ? 's' : ''} remaining`;
}

function addTask(text) {
  const task = { id: Date.now().toString(), text: text.trim(), completed: false };
  if (!task.text) return;
  tasks.unshift(task);
  save();
  render();
}

function toggleComplete(id) {
  const t = tasks.find(x => x.id === id);
  if (!t) return;
  t.completed = !t.completed;
  save();
  render();
}

function deleteTask(id) {
  tasks = tasks.filter(x => x.id !== id);
  save();
  render();
}

function clearCompleted() {
  tasks = tasks.filter(t => !t.completed);
  save();
  render();
}

// Event listeners
form.addEventListener('submit', (e) => {
  e.preventDefault();
  addTask(input.value);
  input.value = '';
  input.focus();
});

list.addEventListener('click', (e) => {
  const li = e.target.closest('li');
  if (!li) return;
  const id = li.dataset.id;

  if (e.target.matches('button.delete')) {
    deleteTask(id);
    return;
  }

  if (e.target.matches('input[type=checkbox]')) {
    toggleComplete(id);
    return;
  }
});

clearCompletedBtn.addEventListener('click', () => {
  clearCompleted();
});

// Initial render
render();
