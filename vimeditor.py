import os

class Command:
    def execute(self, editor):
        pass

    def undo(self, editor):
        pass

class CursorMovement:
    @staticmethod
    def move_left(editor):
        if editor.cursor_pos > 0:
            editor.cursor_pos -= 1

    @staticmethod
    def move_right(editor):
        if editor.cursor_pos < len(editor.paragraph):
            editor.cursor_pos += 1

    @staticmethod
    def move_up(editor):
        current_line = editor.get_current_line()
        if current_line > 0:
            column = editor.cursor_pos - editor.line_indices[current_line][0]
            prev_line_start, prev_line_end = editor.line_indices[current_line - 1]
            editor.cursor_pos = min(prev_line_start + column, prev_line_end)

    @staticmethod
    def move_down(editor):
        current_line = editor.get_current_line()
        if current_line < len(editor.line_indices) - 1:
            column = editor.cursor_pos - editor.line_indices[current_line][0]
            next_line_start, next_line_end = editor.line_indices[current_line + 1]
            editor.cursor_pos = min(next_line_start + column, next_line_end)

    @staticmethod
    def move_to_line_start(editor):
        current_line = editor.get_current_line()
        editor.cursor_pos = editor.line_indices[current_line][0]

    @staticmethod
    def move_to_line_end(editor):
        current_line = editor.get_current_line()
        editor.cursor_pos = editor.line_indices[current_line][1]

    @staticmethod
    def move_to_file_start(editor):
        editor.cursor_pos = 0

    @staticmethod
    def move_to_file_end(editor):
        editor.cursor_pos = len(editor.paragraph)

    @staticmethod
    def move_word_forward(editor):
        next_space = editor.paragraph.find(' ', editor.cursor_pos + 1)
        editor.cursor_pos = len(editor.paragraph) if next_space == -1 else next_space + 1

    @staticmethod
    def move_word_backward(editor):
        prev_space = editor.paragraph.rfind(' ', 0, editor.cursor_pos - 1)
        editor.cursor_pos = 0 if prev_space == -1 else prev_space + 1

    @staticmethod
    def move_to_matching_parenthesis(editor):
        opening, closing = "([{", ")]}"
        char = editor.paragraph[editor.cursor_pos]
        if char in opening + closing:
            stack = [char]
            direction = 1 if char in opening else -1
            for i in range(editor.cursor_pos + direction, -1 if direction == -1 else len(editor.paragraph), direction):
                if editor.paragraph[i] in (opening if direction == 1 else closing):
                    stack.append(editor.paragraph[i])
                elif editor.paragraph[i] in (closing if direction == 1 else opening):
                    if stack and (opening.index(stack[-1]) == closing.index(editor.paragraph[i]) if direction == 1 else closing.index(stack[-1]) == opening.index(editor.paragraph[i])):
                        stack.pop()
                        if not stack:
                            editor.cursor_pos = i
                            return
        print("No matching parenthesis found")

class TextEditing:
    @staticmethod
    def delete_left(editor):
        if editor.cursor_pos > 0:
            editor.paragraph = editor.paragraph[:editor.cursor_pos-1] + editor.paragraph[editor.cursor_pos:]
            editor.cursor_pos -= 1
            editor.update_line_indices()

    @staticmethod
    def delete_right(editor):
        if editor.cursor_pos < len(editor.paragraph):
            editor.paragraph = editor.paragraph[:editor.cursor_pos] + editor.paragraph[editor.cursor_pos+1:]
            editor.update_line_indices()

    @staticmethod
    def delete_line(editor):
        current_line = editor.get_current_line()
        start, end = editor.line_indices[current_line]
        end = editor.line_indices[current_line + 1][0] if current_line < len(editor.line_indices) - 1 else len(editor.paragraph)
        editor.paragraph = editor.paragraph[:start] + editor.paragraph[end:]
        editor.cursor_pos = start
        editor.update_line_indices()

    @staticmethod
    def transpose_lines(editor):
        current_line = editor.get_current_line()
        if current_line < len(editor.line_indices) - 1:
            current_start, current_end = editor.line_indices[current_line]
            next_start, next_end = editor.line_indices[current_line + 1]
            current_line_text = editor.paragraph[current_start:next_start]
            next_line_text = editor.paragraph[next_start:next_end + 1]
            editor.paragraph = editor.paragraph[:current_start] + next_line_text + current_line_text + editor.paragraph[next_end + 1:]
            editor.cursor_pos = next_start
            editor.update_line_indices()

class FileOperations:
    @staticmethod
    def save_file(editor):
        filename = input("Enter filename to save: ")
        try:
            with open(filename, 'w') as file:
                file.write(editor.paragraph)
            print(f"File saved as {filename}")
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")

class Editor:
    def __init__(self):
        self._paragraph = ""
        self._cursor_pos = 0
        self._line_indices = []
        self._clipboard = ""
        self._undo_stack = []
        self._redo_stack = []

    @property
    def paragraph(self):
        return self._paragraph

    @paragraph.setter
    def paragraph(self, value):
        self._paragraph = value
        self.update_line_indices()

    @property
    def cursor_pos(self):
        return self._cursor_pos

    @cursor_pos.setter
    def cursor_pos(self, value):
        if 0 <= value <= len(self._paragraph):
            self._cursor_pos = value
        else:
            raise ValueError("Invalid cursor position")

    @property
    def line_indices(self):
        return self._line_indices

    def update_line_indices(self):
        self._line_indices = []
        lines = self._paragraph.splitlines(True)
        current_index = 0
        for line in lines:
            start_index = current_index
            end_index = current_index + len(line) - 1
            self._line_indices.append([start_index, end_index])
            current_index += len(line)

    def get_current_line(self):
        return next((i for i, (start, end) in enumerate(self._line_indices) if start <= self._cursor_pos <= end), 0)

    def execute_command(self, command):
        command.execute(self)
        self._undo_stack.append(command)
        self._redo_stack.clear()

    def undo(self):
        if self._undo_stack:
            command = self._undo_stack.pop()
            command.undo(self)
            self._redo_stack.append(command)
        else:
            print("Nothing to undo")

    def redo(self):
        if self._redo_stack:
            command = self._redo_stack.pop()
            command.execute(self)
            self._undo_stack.append(command)
        else:
            print("Nothing to redo")

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-" * 50)
        cursor_line = self.get_current_line()
        for i, line in enumerate(self._paragraph.splitlines()):
            if i == cursor_line:
                print(line[:self._cursor_pos - self._line_indices[i][0]] + "|" + line[self._cursor_pos - self._line_indices[i][0]:])
            else:
                print(line)
        print("-" * 50)
        print(f"Cursor position: {self._cursor_pos}")

def main():
    editor = Editor()
    editor.paragraph = input("Enter your text:\n")
    editor.cursor_pos = len(editor.paragraph)

    commands = {
        'h': CursorMovement.move_left,
        'l': CursorMovement.move_right,
        'j': CursorMovement.move_down,
        'k': CursorMovement.move_up,
        '0': CursorMovement.move_to_line_start,
        '$': CursorMovement.move_to_line_end,
        'gg': CursorMovement.move_to_file_start,
        'G': CursorMovement.move_to_file_end,
        'w': CursorMovement.move_word_forward,
        'b': CursorMovement.move_word_backward,
        '%': CursorMovement.move_to_matching_parenthesis,
        'x': TextEditing.delete_right,
        'X': TextEditing.delete_left,
        'dd': TextEditing.delete_line,
        'ddp': TextEditing.transpose_lines,
        ':w': FileOperations.save_file,
    }

    while True:
        editor.display()
        command = input("Enter command (q to quit): ").lower()
        if command == 'q':
            break
        elif command in commands:
            commands[command](editor)
        elif command == 'u':
            editor.undo()
        elif command == 'ctrl+r':
            editor.redo()
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
