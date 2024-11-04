''' 
READ ME:
TO USE PLS UNDO THE DOCSTRINGS BEFORE EACH FUNCTION. 
IT IS ABSOLUTELY MANDATORY FOR U TO USE FUNCTIONS 1 AND 2 BEFORE U CAN UTILIZE THE PROGRAM AT ALL

# Vim-like Text Editor Functions

1. `begin_program()`: Initializes the text editor and displays the initial text.
2. `adjust_cursor()`: Moves the cursor to a user-specified position.
3. `cmd_h()`: Moves the cursor one character to the left.
4. `cmd_I()`: Moves the cursor one character to the right.
5. `cmd_j()`: Moves the cursor one line down.
6. `cmd_k()`: Moves the cursor one line up.
7. `cmd_X()`: Deletes the character to the left of the cursor.
8. `cmd_D()`: Removes text from the cursor to the end of the line.
9. `cmd_dd()`: Deletes the current line.
10. `cmd_ddp()`: Transposes the current line with the next line.
11. `cmd_n()`: Searches for the next occurrence of a specified string.
12. `cmd_wq()`: Saves the file and (theoretically) quits the editor.
13. `cmd_gg()`: Moves the cursor to the beginning of the file.
14. `cmd_G()`: Moves the cursor to the end of the file.
15. `cmd_0()`: Moves the cursor to the beginning of the current line.
16. `cmd_dollar()`: Moves the cursor to the end of the current line.
17. `cmd_w()`: Moves the cursor forward one word.
18. `cmd_b()`: Moves the cursor backward one word.
19. `cmd_yy()`: Yanks (copies) the current line.
20. `cmd_p()`: Pastes text after the cursor.
21. `cmd_u()`: Undoes the last change.
22. `cmd_percent()`: Jumps to the matching parenthesis.
23. `cmd_O()`: Opens a new line above the current line and enters insert mode.
24. `cmd_o()`: Opens a new line below the current line and enters insert mode.
25. `cmd_r()`: Replaces the character under the cursor with a user-specified character.
26. `cmd_x()`: Deletes the character under the cursor.
27. `cmd_yw()`: Yanks (copies) from the cursor to the end of the word.
28. `cmd_dw()`: Deletes from the cursor to the end of the word.
29. `cmd_J()`: Joins the current line with the line below it.
30. `cmd_cc()`: Changes (deletes and enters insert mode) the entire current line.
31. `cmd_gt()`: Goes to the next paragraph (simulated as next 'tab').
32. `cmd_gT()`: Goes to the previous paragraph (simulated as previous 'tab').

These descriptions provide a concise explanation of what each new function does in your Vim-like text editor implementation.
Note: The `display()` function is called after most operations to show the updated text and cursor position.
'''


def begin_program():
    global text_lines, cursor_line, cursor_pos
    print("This is a representation of a text editor. \nIn order to use this, feel free to type below and you will see the dollar sign ($) as a representation of the cursor")
    print("Type your text here (press Enter twice to finish):")
    print("-----------------------------------------------------------------------------------------------------")
    
    text_lines = get_multiline_input()
    cursor_line = len(text_lines) - 1  # Set cursor at the last line initially
    cursor_pos = len(text_lines[-1])   # Set cursor at the end of the last line

def get_multiline_input():
    lines = []
    print("$", end="")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

def cursor_implementation():
    global text_lines, cursor_line, cursor_pos
    # Create a copy of the lines to modify
    displayed_lines = text_lines.copy()
    
    # Insert cursor in the appropriate line
    current_line = displayed_lines[cursor_line]
    displayed_lines[cursor_line] = current_line[:cursor_pos] + "$" + current_line[cursor_pos:]
    
    return "\n".join(displayed_lines)

def adjust_cursor():
    global cursor_line, cursor_pos
    print("\nEnter the line number and position (format: line_number position):")
    try:
        line_num, pos = map(int, input().split())
        
        if 0 <= line_num < len(text_lines) and 0 <= pos <= len(text_lines[line_num]):
            cursor_line = line_num
            cursor_pos = pos
        else:
            print("Invalid cursor position!")
    except ValueError:
        print("Invalid input format! Please enter two numbers separated by space.")

# Helper function to clear the screen (for better display)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display():
    print("\n" + line_separator)
    print(cursor_implementation())
    print(f"Cursor position: Line {cursor_line}, Position {cursor_pos}")
    print(line_separator + "\n")



#1.) cmd_h: command to move left
def cmd_h():
    global cursor_pos, cursor_line
    if cursor_pos > 0:
        cursor_pos -= 1
    elif cursor_line > 0:
        # Move to end of previous line
        cursor_line -= 1
        cursor_pos = len(text_lines[cursor_line])
    else:
        print("Already at the beginning of the text")

#2.) cmd_l: command to move right
def cmd_l():
    global cursor_pos, cursor_line
    current_line_length = len(text_lines[cursor_line])
    
    if cursor_pos < current_line_length:
        cursor_pos += 1
    elif cursor_line < len(text_lines) - 1:
        # Move to beginning of next line
        cursor_line += 1
        cursor_pos = 0
    else:
        print("Already at the end of the text")

#3.) cmd_j: move cursor vertically one line (down)
def cmd_j():
    global cursor_pos, cursor_line
    
    if cursor_line < len(text_lines) - 1:
        # Move to next line
        cursor_line += 1
        # Adjust cursor position if it exceeds the new line's length
        cursor_pos = min(cursor_pos, len(text_lines[cursor_line]))
    else:
        print("Already at the last line")

#4.) cmd_k: move cursor vertically one line (up)
def cmd_k():
    global cursor_pos, cursor_line
    
    if cursor_line > 0:
        # Move to previous line
        cursor_line -= 1
        # Adjust cursor position if it exceeds the new line's length
        cursor_pos = min(cursor_pos, len(text_lines[cursor_line]))
    else:
        print("Already at the first line")

#5.) cmd_X: delete the character to the left of the cursor
def cmd_X():
    global text_lines, cursor_pos, cursor_line
    
    if cursor_pos > 0:
        # Remove character from current line
        current_line = text_lines[cursor_line]
        text_lines[cursor_line] = current_line[:cursor_pos-1] + current_line[cursor_pos:]
        cursor_pos -= 1
    elif cursor_line > 0:
        # At beginning of line, merge with previous line
        previous_line = text_lines[cursor_line - 1]
        current_line = text_lines[cursor_line]
        cursor_pos = len(previous_line)
        text_lines[cursor_line - 1] = previous_line + current_line
        text_lines.pop(cursor_line)
        cursor_line -= 1
    else:
        print("Nothing to delete")

#6.) cmd_D: remove on current line from cursor to the end
def cmd_D():
    global text_lines, cursor_pos, cursor_line
    
    # Check if we're on a valid line
    if cursor_line < len(text_lines):
        # Get the current line text
        current_line = text_lines[cursor_line]
        # Remove from cursor to the end of the current line
        text_lines[cursor_line] = current_line[:cursor_pos]
    else:
        print("Cursor position error")[1]

#7.) cmd_dd: delete current line and move cursor to the beginning of next line 
def cmd_dd():
    global text_lines, cursor_pos, cursor_line
    
    # Check if we're on a valid line
    if cursor_line < len(text_lines):
        # Remove the current line
        text_lines.pop(cursor_line)
        
        # If we deleted the last line, move cursor up one line
        if cursor_line >= len(text_lines):
            cursor_line = max(0, len(text_lines) - 1)
        
        # Reset cursor position to start of line
        cursor_pos = 0
    else:
        print("Cursor position error")[2]

#8.) cmd_ddp: transpose two adjacent lines
def cmd_ddp():
    global text_lines, cursor_pos, cursor_line
    
    # Check if we're on a valid line and not the last line
    if cursor_line < len(text_lines) - 1:
        # Swap the current line with the next line
        text_lines[cursor_line], text_lines[cursor_line + 1] = \
            text_lines[cursor_line + 1], text_lines[cursor_line]
        
        # Move cursor to the beginning of the next line
        cursor_line += 1
        cursor_pos = 0
    else:
        print("Cannot transpose: already at last line")[3]

#9.) cmd_n: search for next occurrence of a string
last_search = ''

def cmd_n():
    global text_lines, cursor_line, cursor_pos, last_search
    
    # If there's no previous search, prompt for a search string
    if not last_search:
        last_search = input("Enter search string: ")
    
    # Search from current position to end
    for line_num in range(cursor_line, len(text_lines)):
        current_line = text_lines[line_num]
        start_pos = cursor_pos if line_num == cursor_line else 0
        
        found_pos = current_line.find(last_search, start_pos)
        if found_pos != -1:
            cursor_line = line_num
            cursor_pos = found_pos
            print(f"Found '{last_search}' at line {cursor_line + 1}, position {cursor_pos}")
            return
    
    # If not found, wrap around to beginning
    for line_num in range(cursor_line):
        found_pos = text_lines[line_num].find(last_search)
        if found_pos != -1:
            cursor_line = line_num
            cursor_pos = found_pos
            print(f"Found '{last_search}' at line {cursor_line + 1}, position {cursor_pos} (wrapped search)")
            return
    
    print(f"String '{last_search}' not found")[4]

#10.) cmd_wq: write representation as text file and save it
def cmd_wq():
    global text_lines
    
    filename = input("Enter filename to save: ")
    
    try:
        with open(filename, 'w') as file:
            for line in text_lines:
                file.write(line + '\n')  # Write each line with a newline
        print(f"File saved as {filename}")
    except IOError as e:
        print(f"An error occurred while saving the file: {e}")[5]

#11.) cmd_gg: Move cursor to the beginning of the file
def cmd_gg():
    global cursor_line, cursor_pos
    cursor_line = 0
    cursor_pos = 0

#12.) cmd_G: Move cursor to the end of the file
def cmd_G():
    global cursor_line, cursor_pos, text_lines
    cursor_line = len(text_lines) - 1
    cursor_pos = len(text_lines[cursor_line])

#13.) cmd_0: Move cursor to beginning of current line
def cmd_0():
    global cursor_pos
    cursor_pos = 0

#14.) cmd_dollar: move cursor to the end of the current line
def cmd_dollar():
    global cursor_pos, text_lines, cursor_line
    cursor_pos = len(text_lines[cursor_line])

#15.) cmd_w: move cursor forward one word
def cmd_w():
    global cursor_pos, cursor_line, text_lines
    current_line = text_lines[cursor_line]
    
    # Search for next word in current line
    next_space = current_line.find(' ', cursor_pos + 1)
    
    if next_space == -1:
        # If no more words in current line, move to next line
        if cursor_line < len(text_lines) - 1:
            cursor_line += 1
            cursor_pos = 0
        else:
            cursor_pos = len(current_line)
    else:
        # Skip spaces to get to the start of the next word
        cursor_pos = next_space + 1
        while cursor_pos < len(current_line) and current_line[cursor_pos] == ' ':
            cursor_pos += 1

#16.) cmd_b: move cursor backward one word
def cmd_b():
    global cursor_pos, cursor_line, text_lines
    current_line = text_lines[cursor_line]
    
    # Search for previous word in current line
    prev_space = current_line.rfind(' ', 0, max(0, cursor_pos - 1))
    
    if prev_space == -1:
        if cursor_line > 0:
            # Move to end of previous line
            cursor_line -= 1
            cursor_pos = len(text_lines[cursor_line])
        else:
            cursor_pos = 0
    else:
        # Find start of the word
        cursor_pos = prev_space + 1

#17.) cmd_yy: yank the current line
clipboard = ""
def cmd_yy():
    global clipboard, cursor_line, text_lines
    clipboard = text_lines[cursor_line]
    print(f"Copied line: {clipboard}")

#18.) cmd_p: paste after the cursor
def cmd_p():
    global cursor_pos, cursor_line, text_lines, clipboard
    save_state()
    
    # Insert clipboard content after current line
    text_lines.insert(cursor_line + 1, clipboard)
    cursor_line += 1
    cursor_pos = 0

#19.) cmd_u: undo last change
undo_stack = []

def save_state():
    global text_lines, cursor_line, cursor_pos
    undo_stack.append((text_lines.copy(), cursor_line, cursor_pos))

def cmd_u():
    global text_lines, cursor_line, cursor_pos
    if undo_stack:
        text_lines, cursor_line, cursor_pos = undo_stack.pop()

#20.) cmd_percent: jump to matching parenthesis
def cmd_percent():
    global cursor_pos, cursor_line, text_lines
    opening = "([{"
    closing = ")]}"
    current_line = text_lines[cursor_line]
    
    if cursor_pos < len(current_line):
        char = current_line[cursor_pos]
        
        if char in opening:
            # Search forward
            stack = [char]
            # Search through current line and subsequent lines
            for line_idx in range(cursor_line, len(text_lines)):
                search_line = text_lines[line_idx]
                start_pos = cursor_pos if line_idx == cursor_line else 0
                
                for pos in range(start_pos + 1, len(search_line)):
                    if search_line[pos] in opening:
                        stack.append(search_line[pos])
                    elif search_line[pos] in closing:
                        if stack and opening.index(stack[-1]) == closing.index(search_line[pos]):
                            stack.pop()
                            if not stack:
                                cursor_line = line_idx
                                cursor_pos = pos
                                return
                                
        elif char in closing:
            # Search backward
            stack = [char]
            # Search through current line and previous lines
            for line_idx in range(cursor_line, -1, -1):
                search_line = text_lines[line_idx]
                end_pos = cursor_pos if line_idx == cursor_line else len(search_line)
                
                for pos in range(end_pos - 1, -1, -1):
                    if search_line[pos] in closing:
                        stack.append(search_line[pos])
                    elif search_line[pos] in opening:
                        if stack and closing.index(stack[-1]) == opening.index(search_line[pos]):
                            stack.pop()
                            if not stack:
                                cursor_line = line_idx
                                cursor_pos = pos
                                return

#21. cmd_O(): Opens a new line above the current line
def cmd_O():
    global text_lines, cursor_pos, cursor_line
    # Insert a new line above the current line
    text_lines.insert(cursor_line, '')
    cursor_pos = 0

#22. cmd_o(): Opens a new line below the current line
def cmd_o():
    global text_lines, cursor_pos, cursor_line
    # Insert a new line below the current line
    text_lines.insert(cursor_line + 1, '')
    cursor_pos = 0
    cursor_line += 1

#23. cmd_r(): Replaces the character under the cursor
def cmd_r():
    global text_lines, cursor_pos, cursor_line
    char = input('Enter replacement character: ')
    current_line = text_lines[cursor_line]
    if char and cursor_pos < len(current_line):
        text_lines[cursor_line] = current_line[:cursor_pos] + char + current_line[cursor_pos + 1:]

#24. cmd_x(): Deletes the character under the cursor
def cmd_x():
    global text_lines, cursor_pos, cursor_line
    current_line = text_lines[cursor_line]
    if cursor_pos < len(current_line):
        text_lines[cursor_line] = current_line[:cursor_pos] + current_line[cursor_pos + 1:]

#25. cmd_yw(): Yanks (copies) from cursor to end of word
def cmd_yw():
    global text_lines, cursor_pos, clipboard, cursor_line
    current_line = text_lines[cursor_line]
    end = current_line.find(' ', cursor_pos)
    if end == -1:
        end = len(current_line)
    clipboard = current_line[cursor_pos:end]
    print(f'Yanked: {clipboard}')

#26. cmd_dw(): Deletes from cursor to end of word
def cmd_dw():
    global text_lines, cursor_pos, cursor_line
    current_line = text_lines[cursor_line]
    end = current_line.find(' ', cursor_pos)
    if end == -1:
        end = len(current_line)
    text_lines[cursor_line] = current_line[:cursor_pos] + current_line[end:]

#27. cmd_J(): Joins current line with the line below
def cmd_J():
    global text_lines, cursor_line
    if cursor_line < len(text_lines) - 1:
        # Join the current line with the line below it
        text_lines[cursor_line] += ' ' + text_lines[cursor_line + 1].lstrip()
        # Remove the next line
        text_lines.pop(cursor_line + 1)

#28. cmd_cc(): Changes the entire current line
def cmd_cc():
    global text_lines, cursor_pos, cursor_line
    cmd_dd()  # Delete the current line
    cmd_O()   # Open a new line and enter insert mode

#29. cmd_gt(): Goes to next paragraph
def cmd_gt():
    global cursor_pos, cursor_line, text_lines
    # Go to the next paragraph (simulated by going to the next empty line)
    next_para = cursor_line + 1
    while next_para < len(text_lines) and text_lines[next_para] != '':
        next_para += 1
    if next_para < len(text_lines):
        cursor_line = next_para
        cursor_pos = 0
    else:
        print("No next paragraph")

#30. cmd_gT(): Goes to previous paragraph
def cmd_gT():
    global cursor_pos, cursor_line, text_lines
    # Go to the previous paragraph (simulated by moving to the previous empty line)
    prev_para = cursor_line - 1
    while prev_para >= 0 and text_lines[prev_para] != '':
        prev_para -= 1
    if prev_para >= 0:
        cursor_line = prev_para
        cursor_pos = 0
    else:
        print("No previous paragraph")

''' Implementation'''



#For Testing
def test_commands():
    global text_lines, cursor_line, cursor_pos
    
    while True:
        display()
        command = input("Enter command (h/l/j/k/x/D/dd/ddp/n/wq/gg/G/0/$$/w/b/yy/p/u/%/O/o/r/x/yw/dw/J/cc/gt/gT/q): ").lower()
        
        commands = {
            'h': cmd_h,
            'l': cmd_l,
            'j': cmd_j,
            'k': cmd_k,
            'x': cmd_x,
            'd': cmd_D,
            'dd': cmd_dd,
            'ddp': cmd_ddp,
            'n': cmd_n,
            'wq': cmd_wq,
            'gg': cmd_gg,
            'g': cmd_G,
            '0': cmd_0,
            '$': cmd_dollar,
            'w': cmd_w,
            'b': cmd_b,
            'yy': cmd_yy,
            'p': cmd_p,
            'u': cmd_u,
            '%': cmd_percent,
            'o': cmd_o,
            'O': cmd_O,
            'r': cmd_r,
            'yw': cmd_yw,
            'dw': cmd_dw,
            'J': cmd_J,
            'cc': cmd_cc,
            'gt': cmd_gt,
            'gT': cmd_gT,
            'q': lambda: None
        }
        
        if command in commands:
            commands[command]()
            if command == 'q':
                break
        else:
            print("Invalid command")

# Initialize global variables
text_lines = []
cursor_line = 0
cursor_pos = 0
line_separator = "------------------------------------------------------"


begin_program()
print()
print("After adjusting the cursor to the end")
display()


adjust_cursor()
display()

test_commands()
