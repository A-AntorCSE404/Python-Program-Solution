cipher = 'KHOOR ZRUOG'
for shift in range(26):
    decoded = ''
    for ch in cipher:
        if ch.isalpha():
            # ord() function return character to ascii value. eg --> ord('A') = 65
            decoded += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        else:
            decoded += ch
    print(f"Shift {shift:>2}: {decoded}")
                                                
