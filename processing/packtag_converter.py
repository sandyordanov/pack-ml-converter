from domain.pack_tag import PackTag
class PackTagConverter:
    tag_collection = {}
    def __init__(self):
        pass

    def convert_node(self, node):
        new_tag = PackTag(node.name, node.state)
        self.tag_collection[node.name] = new_tag
        return new_tag

    # def get_tag(self, key):
    #     return self.data.get(key, "Key not found")
    #
    # def update_tag(self, key, value):
    #     """Update the value of an existing key."""
    #     if key in self.data:
    #         self.data[key] = value
    #         print(f"Updated pair: {key} = {value}")
    #     else:
    #         print("Key not found. Use add_pair to add new keys.")
    #
    # def delete_tag(self, key):
    #     """Delete a key-value pair by key."""
    #     if key in self.data:
    #         del self.data[key]
    #         print(f"Deleted pair with key: {key}")
    #     else:
    #         print("Key not found. Nothing to delete.")
    #
    # def display_tag(self):
    #     """Display all key-value pairs in the dictionary."""
    #     if self.data:
    #         for key, value in self.data.items():
    #             print(f"{key}: {value}")
    #     else:
    #         print("No key-value pairs to display.")