# TheBlockheadsTools
Tools for manipulating save files of the mobile game 'the blockheads' 

# How to use

## Modify blocks and chunks

### Read a world

```python
>>> from gameSave import GameSave
>>> gs = GameSave.load("./test_data/saves/c8185...a9229/")
```

### Modify a block

For example, if you want to change block at 12384, 372:

```python
>>> b = gs.get_block(12384, 372)
```

And you would like to change it to time crystal:

```python
>>> from blockType import BlockType
>>> b.set("first_layer_id", BlockType.TIME_CRYSTAL)
```

### Modify a chunk

First, get the chunk you want to change:

```python
>>> info = gs.get_info()
>>> start_chunk_pos = [_ >> 5 for _ in info["start_portal_pos"]]
>>> start_chunk_pos[1] += 1
>>> c = gs.get_chunk(*start_chunk_pos)
```

Then modify blocks in it!

```python
>>> for x in range(32):
...     for y in range(32):
...         b = c.get_block(x, y)
...         b.set("first_layer_id", BlockType.LUMINOUS_PLASTER)
```

The code above would set every block in that chunk to luminous plaster.

### Save the modified world

```python
>>> gs.save("./test_data/saves/out/")
```

## Manipulating Inventories

### Get blockheads' inventory

```python
>>> bh = gs.get_blockheads()
>>> inv = gs.get_inventory(bh[0])
>>> print(inv)
[
            0: 'item 1' * 1
            1: 'item 12' * 1
            2: 'item 12' * 1
            3: ['item 12': {'s': [[], [], [], 'item 1049' * 28]}]
            4: ['item 1043': {'d': {'pos_x': 14914, 'pos_y': 537, 'chestType': 0, 'flipped': False, 'interactionObjectType': 2, 'saveItemSlots': [['item 12': {'s': [[], 'item 4' * 3, 'item 3' * 3, 'item 12' 
* 1]}], 'item 6' * 1, 'item 3' * 1, 'item 12' * 1, 'item 53' * 9, ['item 12': {'s': [[], [], 'item 25' * 1, 'item 6' * 1]}], 'item 16' * 1, 'item 1' * 1, 'item 2' * 1, 'item 4' * 1, 'item 5' * 1, 'item 0' * 
1, [], [], [], 'item 12' * 1], 'uniqueID': 3523, 'floatPos': [14914.5, 537.0], 'ownerID': 'server', 'paintColor': 0, 'saveTime': 3463.5894579589367, 'isInUse': False}}]
            5: empty
            6: empty
            7: empty
]
```

*The result looks scary, because there are containers that are inside another container.*

#### Why not `bh[0].get_inventory()`?

The basic information of a blockhead and its corresponding inventory are splitted, and their LCA is `world_db.main`, so you have to call `GameSave.get_inventory(Blockhead)` to get inventory.

It is possible to implement `bh[0].get_inventory()` by passing the reference of `GameSave._data["world_db"]["main"]` to the `Blockhead` object, but I don't think it is that worthy.

### Modify blockhead's inventory

```python
>>> inv[1].set_id(1049)
>>> inv[1].set_count(1919)
>>> print(inv[1])
'item 1049' * 1919
```

Note that it is possible to set the count **over 99**, and the game will not crash.

### Get item from containers

Getting item from containers is hard, since the amount of item in the blockheads is not stored in bytes. Instead, it is stored in a list.

For example, if there are 3 dirts stacked in one slot, that slot would look like this:

```python
['\x18\x04\x00\x00\x00\x00\x00\x0c', '\x18\x04\x00\x00\x00\x00\x00\x00', 
'\x18\x04\x00\x00\x00\x00\x00\x00']
```

When several tools or containers are stacked, where each item's damage or container information is different, this kind of storage is necessary.

But this makes getting items from containers obfuscating. If you want to get the *first* item in a basket, you have to use command like this:

```python
item = inv[basket_index][0]['s'][-1][0]
```

Here, the `inv[basket_index][0]` means the first item in `inv[basket_index]`. If there are several baskets stacked in this slot, then you can use `inv[basket_index][i]` to get i-th basket.

The basket is described by a dictionary, where the key `s` in it stores a list of base64-encoded items. The equivalent key in chest is `saveItemSlot`. So we have to use `['s']` to get the storage part in the basket.

Though we are getting the *first* item, however, the storage order is reversed. Therefore, you have to use `[-1]` to get the *first* item list in the basket. Finally, `[0]` returns the first item in that list.
