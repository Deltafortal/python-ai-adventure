import json


class LocalJSONProvider:

    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_start_node(self):
        return self.data['meta']['start_node']

    def get_node(self, node_id):
        return self.data['nodes'].get(node_id)