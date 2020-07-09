unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while  unconfirmed_users:
    confirmed_users.append(unconfirmed_users.pop())

print(confirmed_users)