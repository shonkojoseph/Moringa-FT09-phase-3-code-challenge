import unittest
from unittest.mock import MagicMock
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_magazine_creation(self):
        # Providing the required 'category' argument
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_creation(self):
        # Corrected 'Author' instantiation without 'field'
        author = Author(1, "Jane Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "Jane Doe")

if __name__ == '__main__':
    unittest.main()
