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

# 1.1: Define the function find_laptop_by_price function, take in parameters (max_price, laptops), Return a list of laptop models priced below or equal to max_price

def find_laptop_by_price(max_price, laptops):
    budget = []
    for lap in laptops:
        if min(lap["price"])<=max_price:
            budget.append(lap["model"])
    return budget
# print(find_laptop_by_price(1500, laptops))

# 1.2: Define the function find_laptop_by_specs function, take in parameters (cpu, ram, storage, laptops), return a list of laptop models matching the specified specifications as passed in as the arguments.

def find_laptop_by_specs(cpu, ram, storage, laptops):
    SIW = [] # Specs I Want
    for lap in laptops:
        if cpu in lap["cpu"] and ram in lap["ram"] and storage in lap["storage"]:
            SIW.append(lap["model"])    
    return SIW
        
# print(find_laptop_by_specs("Intel Core i7", "16GB", "512GB SSD", laptops))

# 1.3 Define the function get_cheapest_laptop function, take in parameter (laptops), return the model of the cheapest laptop

def get_cheapest_laptop(laptops):
    LEL = " " # Least expensive laptop
    look = 3000
    for lap in laptops:
        if min(lap["price"])<look:
            LEL = (lap["model"])
            look = min(lap["price"])
    return LEL

# print(get_cheapest_laptop(laptops))

# 1.4 Define the function get_laptop_colors function, take in parameter (model, laptops). Return the available colors for the specified laptop model

def get_laptop_colors(model, laptops):
    avaco = [] # available colors
    for lap in laptops:
        if model in lap["model"]:
            avaco.append(lap["colors"])    
    
    flat_list = [item for sublist in avaco for item in sublist]
    return flat_list

# print(get_laptop_colors("Lenovo ThinkPad", laptops))

# 1.5: Define the function get_laptop_description function, take in parameter (model, laptops), Return the description of the specified laptop model

def get_laptop_description(model, laptops):
    Desmy = [] # Describe my laptop
    for lap in laptops:
        if model in lap["model"]:
            Desmy.append(lap["description"])   
    return "\n".join(Desmy)

# print(get_laptop_description("Lenovo ThinkPad", laptops))

# 1.6: Define the function get_laptop_ram_options function, take in parameter (model, laptops), Return the available RAM options for the specified laptop model

def get_laptop_ram_options(model, laptops):
    rams = [] # rams
    for lap in laptops:
        if model in lap["model"]:
            rams.append(lap["ram"])    
    flat_list = [item for sublist in rams for item in sublist]
    return flat_list

# print(get_laptop_ram_options("Lenovo ThinkPad", laptops))

# 1.7: Define the function get_most_expensive_laptop function, take in parameter (laptops), Return the model of the most expensive laptop

def get_most_expensive_laptop(laptops):
    MEL = " " # most expensive laptop
    high = 2098
    for lap in laptops:
        if max(lap["price"])>high:
            MEL = (lap["model"])
            high = max(lap["price"])
    return MEL

# print(get_most_expensive_laptop(laptops))

# 1.8: Define the function list_prices function, take in parameter (laptops), return a list of all available laptop prices

def list_prices(laptops):
    all_prices=[]
    for lap in laptops:
        all_prices.append(lap["price"])
    flat_list = [item for sublist in all_prices for item in sublist]
    return flat_list

# print(list_prices(laptops))

# Test functions
# print(find_laptop_by_price(1500, laptops))
# print(find_laptop_by_specs("Intel Core i7", "16GB", "512GB SSD", laptops))
# print(get_cheapest_laptop(laptops))
# print(get_laptop_colors("Lenovo ThinkPad", laptops))
# print(get_laptop_description("Lenovo ThinkPad", laptops))
# print(get_laptop_ram_options("Lenovo ThinkPad", laptops))
# print(get_most_expensive_laptop(laptops))
# print(list_prices(laptops))
   
