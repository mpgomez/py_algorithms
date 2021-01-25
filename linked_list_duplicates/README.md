write code to delete duplicates from an unsorted linked list

import unittest
from collections import dequeue
from collection_utils import remove_duplicates

```python
class TestRemoveDuplicates(unittest.TestCase):
	def test_remove_duplicates_positive(self):
		my_list = [“1”, “2”, “2”, “3”]
		my_linked_list = dequeue([my_list])
		remove_duplicates(my_linked_list)
		self.assertIsInstance(my_linked_list, dequeue)
		self.assertEqual(dequeue( [“1”, “2”,, “3”]), my_linked_list)
		
```

ESTE NO VALE
No puedes modificar el deque mientras lo iteras
```python
def remove_duplicates(linked_list):
"""
Function that, given a linked list (dequeue) will remove any duplicates from the list

:param linked_list: list with duplicates. Will be modified.

:return None
"""
	different_elements = {}
	for element in linked_list:
		if element in different_elements:
			linked_list.remove(element)
		else:
			different_elements.add(element)
```

Funcionaria esto:
```python
from collections import Counter

def remove_duplicates(linked_list):
    """
    Function that, given a linked list (dequeue) will remove any duplicates from the list

    :param linked_list: list with duplicates. Will be modified.

    :return None
    """
    different_elements = Counter(linked_list)
    for element in different_elements:
        for i in range(different_elements[element]-1):
            linked_list.remove(element)
```

Itertools?