"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for i in items_to_add:
        if i not in current_cart:
            current_cart[i] = 1
        else:
            current_cart[i] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    
    return {}.fromkeys(notes, 1)
    


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    recipe_updates = dict(recipe_updates)
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    holder = cart.items()
    holder = sorted(holder)
    y = []
    for i in holder:
        y.append(i)
    
    return dict(y)

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    result = {}

    for item in sorted(cart, reverse=True):
        result[item] = [
            cart[item],
            aisle_mapping[item][0],
            aisle_mapping[item][1]
        ]

    return result

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """


    res = store_inventory.copy()
    for item in fulfillment_cart:
        res[item] = [
        store_inventory[item][0] - fulfillment_cart[item][0],
store_inventory[item][1],
store_inventory[item][2]
        ]
    for i in res:
        if res[i][0] <= 0:
            res[i][0] = 'Out of Stock'
    return res
    
