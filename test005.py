
# import os

# if __name__ == '__main__':
#     actions = {'create': create_user, 'login': login, 'change_password': change_password,
#                 'help': help}

#     try:
#         action = sys.argv[1]
#         print(action)
#     except IndexError:
#         action = 'help'
#     args = sys.argv[2:]
#     try:
#         actions[action](*args)
#         print(action)
#     except (KeyError, TypeError):
#         help()

actions = {'create': create_user, 'login': login, 'change_password': change_password,
                'help': help}


print(actions.keys())