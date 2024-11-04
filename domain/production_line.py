from domain.message import Message
from domain.node import Node
from domain.states import State
from processing.packtag_converter import PackTagConverter


class ProductionLine:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        # Method to add nodes to the production line
        self.nodes.append(node)

    def UpdateNode(self, message: Message):
        node_found = False  # Flag to track if a matching node is found
        
        for node in self.nodes:
            if node.name == message.name:
                node_found = True
                try:
                    # Attempt to update the node's state
                    node.UpdateState(message)
                except Exception as e:
                    print(f"Error updating node '{node.name}': {e}")
                    return  # Exit or skip further processing on failure

                try:
                    # Attempt to convert the node to a PackML tag
                    PackTagConverter.ConvertNodeToPacktag(node)
                except Exception as e:
                    print(f"Error converting node '{node.name}' to PackTag: {e}")
                    return  # Exit or log the failure, depending on criticality
                
                # Successfully updated and converted, so break out of loop
                break

        if not node_found:
            print(f"No node found with the name '{message.name}'.")