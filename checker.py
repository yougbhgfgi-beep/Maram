import sys

def check_balance(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Bracket matching
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for i, char in enumerate(content):
        if char in brackets.keys():
            stack.append((char, i))
        elif char in brackets.values():
            if not stack:
                print(f"Excess closing bracket '{char}' at index {i}")
                return
            top, pos = stack.pop()
            if brackets[top] != char:
                print(f"Mismatched bracket '{top}' at {pos} with '{char}' at {i}")
                return
    
    if stack:
        for char, pos in stack:
            print(f"Unclosed bracket '{char}' at index {pos}")
        return

    print("Brackets are balanced.")

    # Simple HTML tag matching (rough)
    import re
    tags = re.findall(r'<(/?\w+)', content)
    tag_stack = []
    void_tags = {'img', 'br', 'hr', 'input', 'link', 'meta', 'source', 'video', 'audio'} # source/video/audio are not void but often behave similarly in rough regex
    
    for tag in tags:
        if tag.startswith('/'):
            if not tag_stack:
                print(f"Excess closing tag </{tag[1:]}>")
                continue
            top = tag_stack.pop()
            if top != tag[1:]:
                print(f"Mismatched tag <{top}> with </{tag[1:]}>")
        else:
            if tag.lower() not in void_tags:
                tag_stack.append(tag)
    
    if tag_stack:
        print(f"Unclosed tags: {tag_stack}")
    else:
        print("Simple HTML tag check passed (ignoring void tags).")

if __name__ == "__main__":
    check_balance(sys.argv[1])
