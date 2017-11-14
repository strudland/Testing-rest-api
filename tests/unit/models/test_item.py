from tests.unit.unit_base_test import UnitBaseTest #da ne množimo importov v vsakem unit test fajlu
from models.item import ItemModel


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test', 19.30, 1)

        self.assertEqual(item.name,'test', "The name of the item after creation does not equal constructor") #napisemo kaj zelimo videti kot error
        self.assertEqual(item.price, 19.30, "The price of the item after creation does not equal constructor")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test', 19.30, 1)
        expected = {
            'name': 'test',
            'price': 19.30,
        }

        self.assertEqual(item.json(), expected,
                         "The JSON export of the item is incorrect. Received {}")