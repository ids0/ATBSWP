stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1, 'arrow':12}
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    # print(inventory.keys())
    # for i in inventory.keys():
    #     print(str(inventory[i]) + ' ' + i)
    #     item_total = item_total + inventory[i]
    # ####
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total numer of items: ' + str(item_total))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory,addedItems):
    for loot in addedItems:
        if loot in inventory:
            inventory[loot] += 1
        # else:    
        inventory.setdefault(loot,1)
    # return inventory

addToInventory(stuff,dragonLoot)
print(stuff)
displayInventory(stuff)
input()
