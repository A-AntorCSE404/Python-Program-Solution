def profile(**kwargs):
    for key, val in kwargs.items():
        # upper method is used for making capital letter of the each Key.
        print(f"{key.upper()}: {val}")

profile(name="Neo", role="hacker", level="elite")
