
def addToInventory(inventory, addedItems):

    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for item, num in inventory.items():
        print(num, item)
        total += num
    print(f'Total number of items: {total}')

if __name__ == '__main__':

    inv = {'gold coin': 42, 'rope': 1}
    loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    newInv = addToInventory(inv, loot)
    displayInventory(newInv)