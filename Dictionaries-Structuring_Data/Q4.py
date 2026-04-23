from collections import deque

def main():

    n = int(input().strip())
    q = deque()

    for _ in range(n):
        cmd = input().strip()

        if cmd.startswith("IN"):
            _, pkt = cmd.split()
            q.append(pkt)

        elif cmd == "OUT":
            if q:
                print(q.popleft())
            else:
                print("DROP")

if __name__=="__main__":
    main()
