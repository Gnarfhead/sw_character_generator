def manage_items(item_list, action, item=None):
    """
    Manage a list of items by adding or removing items.

    Parameters:
    item_list (list): The list of items to manage.
    action (str): The action to perform ('add' or 'remove').
    item: The item to add or remove from the list.

    Returns:
    list: The updated list of items.
    """
    if action == 'add':
        if item is not None:
            item_list.append(item)
        else:
            raise ValueError("Item must be provided to add.")
    elif action == 'remove':
        if item in item_list:
            item_list.remove(item)
        else:
            raise ValueError("Item not found in the list.")
    else:
        raise ValueError("Action must be 'add' or 'remove'.")

    return item_list

