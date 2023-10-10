import unittest

from laptops import (
    find_laptop_by_price,
    find_laptop_by_specs,
    get_cheapest_laptop,
    get_laptop_colors,
    get_laptop_description,
    get_laptop_ram_options,
    get_most_expensive_laptop,
    list_prices,
)

# Define your laptops here for testing
laptops = [
    {
        "model": "MacBook Pro",
        "screen_size": "13-inch",
        "cpu": ["Intel Core i5", "Intel Core i7"],
        "ram": ["8GB", "16GB"],
        "storage": ["256GB SSD", "512GB SSD"],
        "colors": ["Space Gray", "Silver"],
        "price": [1299, 1499, 1799],
        "url": "https://example.com/macbook-pro",
        "description": "A powerful and sleek laptop from Apple."
    },
    {
        "model": "Dell XPS",
        "screen_size": "15-inch",
        "cpu": ["Intel Core i7", "Intel Core i9"],
        "ram": ["16GB", "32GB"],
        "storage": ["512GB SSD", "1TB SSD"],
        "colors": ["Platinum Silver", "Black"],
        "price": [1699, 1899, 2099],
        "url": "https://example.com/dell-xps",
        "description": "A premium Windows laptop with top-notch performance."
    },
    {
        "model": "Lenovo ThinkPad",
        "screen_size": "14-inch",
        "cpu": ["Intel Core i5", "Intel Core i7"],
        "ram": ["8GB", "16GB"],
        "storage": ["256GB SSD", "512GB SSD"],
        "colors": ["Black", "Silver"],
        "price": [1199, 1399, 1599],
        "url": "https://example.com/lenovo-thinkpad",
        "description": "A reliable business laptop from Lenovo."
    }
]

class TestLaptopFunctions(unittest.TestCase):
    # Solution: Implement the find_laptop_by_price function
    def test_find_laptop_by_price(self):
        self.assertEqual(find_laptop_by_price(1500, laptops), ['MacBook Pro', 'Lenovo ThinkPad'])

    # Solution: Implement the find_laptop_by_specs function
    def test_find_laptop_by_specs(self):
        self.assertEqual(find_laptop_by_specs("Intel Core i7", "16GB", "512GB SSD", laptops), ['MacBook Pro', 'Dell XPS', 'Lenovo ThinkPad'])

    # Solution: Implement the get_cheapest_laptop function
    def test_get_cheapest_laptop(self):
        self.assertEqual(get_cheapest_laptop(laptops), 'Lenovo ThinkPad')

    # Solution: Implement the get_laptop_colors function
    def test_get_laptop_colors(self):
        self.assertEqual(get_laptop_colors("Lenovo ThinkPad", laptops), ['Black', 'Silver'])

    def test_get_laptop_description(self):
        actual_description = get_laptop_description("Lenovo ThinkPad", laptops)
        print("Actual Description:", repr(actual_description))  # Debugging statement
        self.assertEqual(actual_description, 'A reliable business laptop from Lenovo.')

    # Solution: Implement the get_laptop_ram_options function
    def test_get_laptop_ram_options(self):
        self.assertEqual(get_laptop_ram_options("Lenovo ThinkPad", laptops), ['8GB', '16GB'])

    # Solution: Implement the get_most_expensive_laptop function
    def test_get_most_expensive_laptop(self):
        self.assertEqual(get_most_expensive_laptop(laptops), 'Dell XPS')

    # Solution: Implement the list_prices function
    def test_list_prices(self):
        self.assertEqual(list_prices(laptops), [1299, 1499, 1799, 1699, 1899, 2099, 1199, 1399, 1599])

if __name__ == '__main__':
    unittest.main()

