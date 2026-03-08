def register_user(username, age, email):
    assert isinstance(username, str) and 3 <= len(username) <= 20,         f"Invalid username: '{username}'"
    
    assert isinstance(age, int) and 18 <= age <= 99,         f"Invalid age: {age}"
    
    assert "@" in email and "." in email,         f"Invalid email: '{email}'"
    print(f"'{username}' registered successfully!")


if __name__=="__main__":

    tests = [
        ("Neo", 25, "neo@matrix.com"),
        ("X",   25, "neo@matrix.com"),
        ("Neo", 15, "neo@matrix.com"),
        ("Neo", 25, "notanemail"),
    ]   

    for u, a, e in tests:
        try:
            register_user(u, a, e)
        except AssertionError as e:
            print(f"FAILED: {e}")
                                        
