"""Print out all the melons in our inventory."""
#Opt 1
from melons import melon_names

for melon, value in melon_names.items():
    print(melon.upper())
    print(f'Price: {value[0]}')
    print(f'Seedless: {value[1]}')
    print(f'flesh_color: {value[2]}')
    print(f'rind_color: {value[3]}')
    print(f'Average_weight: {value[4]}')

#Opt 2
# from melons import melons

# def print_all_melons(melons):
#     """Print each melon with corresponding attribute information."""

#     for melon_name, attributes in melons.items():
#         print(melon_name.upper())

#         for attribute, value in attributes.items():
#             print(f'{attribute}: {value}')


# print_all_melons(melons)