s = input().strip()

stack = []
pairs = {')': '(', ']': '[', '}': '{'}

valid = True

for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs.get(ch, ''):
            valid = False
            break
        stack.pop()

if valid and not stack:
    print("VALID")
else:
    print("INVALID")
