
def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for item, num in inventory.items:
        print(num, item)
        total += num
    print(f'Total number of items: {total}')

if __name__ == '__main__':
    print('Enter the inventory in dictionary format:')
    inv = eval(input())

    displayInventory(inv)