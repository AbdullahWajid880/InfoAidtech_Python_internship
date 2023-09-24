import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QAction, QFileDialog, QMessageBox

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tasks = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.title_input = QLineEdit(self)
        self.description_input = QLineEdit(self)
        self.status_input = QLineEdit(self)

        add_button = QPushButton("Add Task", self)
        add_button.setStyleSheet("background-color: lightgreen;")
        add_button.clicked.connect(self.add_task)

        delete_button = QPushButton("Delete Task", self)
        delete_button.setStyleSheet("background-color: lightcoral;")
        delete_button.clicked.connect(self.delete_task)


        
        save_action = QAction("Save Tasks", self)
        save_action.triggered.connect(self.save_tasks)

        load_action = QAction("Load Tasks", self)
        load_action.triggered.connect(self.load_tasks)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(save_action)
        file_menu.addAction(load_action)

        self.task_list = QListWidget(self)

        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.description_input)
        layout.addWidget(QLabel("Status:"))
        layout.addWidget(self.status_input)
        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(self.task_list)

        central_widget.setLayout(layout)

    def add_task(self):
        title = self.title_input.text()
        description = self.description_input.text()
        status = self.status_input.text()
        
        if title and description:
            task = Task(title, description, status)
            self.tasks.append(task)
            self.update_task_list()
            self.title_input.clear()
            self.description_input.clear()
            self.status_input.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return

        selected_item = selected_items[0].text()
        result = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the task:\n{selected_item}?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.tasks = [task for task in self.tasks if str(task) != selected_item]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.addItem(str(task))

    def save_tasks(self):
       
        filename, _ = QFileDialog.getSaveFileName(self, "Save Tasks", "", "Task Files (*.todo)")
        if filename:
            with open(filename, "wb") as file:
                pickle.dump(self.tasks, file)

    def load_tasks(self):
        
        filename, _ = QFileDialog.getOpenFileName(self, "Load Tasks", "", "Task Files (*.todo)")
        if filename:
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)
            self.update_task_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    window.show()
    sys.exit(app.exec_())
