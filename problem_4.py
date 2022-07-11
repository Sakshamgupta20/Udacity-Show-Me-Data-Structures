class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name




def is_user_in_group(user, group):

    if group is None or user is None:
        return False
        
    if user in group.users:
        return True
    
    for group in group.groups:
        return is_user_in_group(user,group)

    return False




print('''
CASE 1: 
Passing None in method
OUTPUT: {}
'''.format(is_user_in_group(None,None))) # False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user1 = "sub_child_user1"
sub_child.add_user(sub_child_user1)
child.add_group(sub_child)
parent.add_group(child)
print('''
CASE 2: 
Passing sub_child_user1 as user and parent as group
OUTPUT: {}
'''.format(is_user_in_group(sub_child_user1,parent))) # True


parent = Group("parent")
parent.add_user("parent_user1")
parent.add_user("parent_user2")
parent.add_user("parent_user3")

child = Group("child")
child.add_user("child_user1")
child.add_user("child_user2")
child.add_user("child_user3")

sub_child = Group("subchild")
sub_child.add_user("sub_child_user1")
sub_child.add_user("sub_child_user2")
sub_child.add_user("sub_child_user3")
child.add_group(sub_child)
parent.add_group(child)

print('''
CASE 2: 
Passing parent_user_1 and sub_child group
OUTPUT: {}
'''.format(is_user_in_group("parent_user_1",sub_child))) #False
