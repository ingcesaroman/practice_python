from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]

    current_node = list_at_array.head_node
    while current_node:
      if current_node.get_value()[0] == key:
        current_node.value = [key, value]
        return
      current_node = current_node.get_next_node()

    payload = Node([key, value])
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        return item[1]
    return None

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('rose'))
print(blossom.retrieve('non-existent flower'))