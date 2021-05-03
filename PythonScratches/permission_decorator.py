class User:
    _user_ids = []
    def __init__(self,permissions:list):
        self.permissions = permissions
        User._user_ids.append(self)

User([2,3,4])
User([2,3,4,5,6])

def has_permission(user_id,permission_id):
    def decorator(func):
        user = User._user_ids[user_id]
        def check(*args,**kwargs):
            assert permission_id in user.permissions,"yetki alani disinda"
            process = func(*args,**kwargs)
            return process
        return check
    return decorator


@has_permission(user_id=1, permission_id=6)
def add(db_data):
    print("eklendi")
    return db_data

add(3)