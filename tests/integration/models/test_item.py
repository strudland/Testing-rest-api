from models.item import ItemModel
from tests.base_test import BaseTest
from app import app

class ItemTest(BaseTest):
    def test_crud(self):  #testing if item can be save to or retrieved from database
        with self.app_context():
            item = ItemModel('test', 19.30)
            self.assertIsNone(ItemModel.find_by_name('test'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))
