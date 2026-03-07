def require_admin(func):
    
    def wrapper(user, *args, **kwargs):
        if user.get('role') != 'admin':
            print("Access denied!")
            return     
        return func(user, *args, **kwargs)
    
    return wrapper

@require_admin
def delete_user(user, target):
    print(f"{user['name']} deleted user: {target}")
  
if __name__=="__main__":
    admin = {'name': 'root', 'role': 'admin'}
    guest = {'name': 'guest', 'role': 'user'}

    #call delete user function for admin validation
    delete_user(admin, "alice")

    #call delete_user function for the guest user
    delete_user(guest,"bob")

