class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    users = group.get_users() # current group.users set
    if user in users:
        return True
    groups = group.get_groups()
    for current_group in groups:
        if is_user_in_group(user, current_group):
            return True
    return False


if __name__ == '__main__':
    parent = Group("parent")                # {'parent' : None}
    child = Group("child")                  # {'child' : None}
    sub_child = Group("subchild")           # {'subchild' : None}

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)      # {'subchild' : 'sub_child_user'}

    child.add_group(sub_child)              
    parent.add_group(child)

    #          {'parent' : None}
    #               ^-{'child' : None}
    #                     ^-{'subchild' : 'sub_child_user'}

    print(is_user_in_group(sub_child_user, child))  # should return True
    print(is_user_in_group(sub_child_user, parent)) # should return True