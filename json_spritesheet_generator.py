# NOTE: This program assumes the sprites in the spritesheet are organized in uniformly sized
# bounding boxes from left to right, top to bottom in order of animation.

import argparse
import json
from PIL import Image

spritesheet = { 'sub_textures': {} }

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    '-p',
    '--path',
    metavar='PATH',
    type=str,
    help="Path to spritesheet"
)

parser.add_argument(
    '-r',
    '--rows',
    metavar='ROWS',
    type=int,
    help="Number of rows in spritesheet"
)

parser.add_argument(
    '-c',
    '--cols',
    metavar='COLS',
    type=int,
    help="Number of columns in spritesheet"
)

args = parser.parse_args()

img = Image.open(args.path) 

width = img.size[0] / args.cols
height = img.size[1] / args.rows

count = 0
for y in range(args.rows):
  for x in range(args.cols):
    spritesheet['sub_textures'][count] = { 'x': x * width, 'y': y * height, 'width': width, 'height': height }
    count += 1

with open(args.path[:args.path.rfind('.')] + '.json', 'w') as file:
  json.dump(spritesheet, file, indent=4)
