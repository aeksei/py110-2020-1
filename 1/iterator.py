import itertools

START = 100
STEP = 7

# for i in itertools.count(START, STEP):
#     print(i)

users = [
    'Вася',
    'Петя',
    'Ваня'
]

counter = ['Чики', 'брики', 'пальчик', 'выкинь', 'test']
iter_users = itertools.cycle(users)

current_user = users[0]
for _ in counter:
    current_user = next(iter_users)

print(current_user)


print(users[len(counter) % len(users) - 1])