from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.30)

        self.assertEqual(item.name,'test', "The name of the item after creation does not equal constructor") #napisemo kaj zelimo videti kot error
        self.assertEqual(item.price, 19.30, "The price of the item after creation does not equal constructor")

    def test_item_json(self):
        item = ItemModel('test', 19.30)
        expected = {
            'name': 'test',
            'price': 19.30,
        }

        self.assertEqual(item.json(), expected,
                         "The JSON export of the item is incorrect. Received {}")