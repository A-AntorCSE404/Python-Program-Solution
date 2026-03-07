def main():
    students = [('Alice', 85), ('Bob', 92), ('Eve', 78)]
    ranked = sorted(students, key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(ranked, 1):
        print(f"#{i} {name} — {score}")

if __name__=="__main__":
    main()

