IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
LAYER_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT

def solve():
  f = open("input/day08.txt", "r")
  pixel_data = f.read().strip('\n')
  f.close()

  layer_count = int(len(pixel_data) / LAYER_SIZE)
  layer_starts = [i * LAYER_SIZE for i in range(layer_count)]
  layers_data = [pixel_data[i:i+LAYER_SIZE] for i in layer_starts]
  check_layer = min(layers_data, key = lambda x: x.count('0'))

  print("Part 1")
  print(f"  1s and 2s product: {check_layer.count('1') * check_layer.count('2')}")

  print()
  print("Part 2")

  def pixel_at(x, y, layer):
    return layers_data[layer][x + y * IMAGE_WIDTH]

  for y in range(IMAGE_HEIGHT):
    print()
    print('  ', end='')

    for x in range(IMAGE_WIDTH):
      layer = 0
      while (pixel := pixel_at(x, y, layer)) == '2':
        layer += 1

      if pixel == '0':
        pixel_char = '⬛️'
      else:
        pixel_char = '⬜️'

      print(pixel_char, end='')

  print('\n')
