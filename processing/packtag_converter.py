from domain.pack_tag import PackTag
class PackTagConverter:
    def __init__(self):
        self.data = {}


    def convert_node(self, node):
        pack_tag = PackTag()
        pack_tag.add_tag("name", node.name)