#!/usr/local/bin/python3
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
xpos = pos.x + 10
ypos = pos.y
zpos = pos.z

# Put 20 Glass Boxes into this list (Block ID 20)
blocks = [20] * 20

barBlock = 22 # Lapis Lazuli Block

count = 0
# Keep looping until we have been through the whole blocks list
while count < len(blocks):

    # Loop through the block list and place the blocks
    for i in range(0,len(blocks)):
        mc.setBlock(xpos, ypos + i, zpos, blocks[i])

    count += 1


    # Delete the last block in the list
    blocks.remove(len(blocks))

    # Add a Lapis Lazuli Block to the front of the list
    blocks.insert(0,22)

    time.sleep(2)
