unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
copy_unprinted_designs = []


def complete_model(unprinted_designs, completed_models):
    completed_models.append(unprinted_designs.pop())


def copy_list(unprinted_designs):
    copy_unprinted_designs = unprinted_designs.copy()


copy_list(unprinted_designs[:])

while unprinted_designs:
    complete_model(unprinted_designs, completed_models)

print(completed_models)
print(unprinted_designs)
print(copy_unprinted_designs)
