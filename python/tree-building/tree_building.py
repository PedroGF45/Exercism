class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda x: x.record_id)
    root = Node(records[0].record_id)

    if root.node_id != 0 or records[-1].record_id != len(records) - 1:
        raise ValueError('Record id is invalid or out of order.')
    if records[0].parent_id != records[0].record_id:
        raise ValueError("Node parent_id should be smaller than it's record_id.")
            
    nodes = {0: root}

    for record in records[1:]:
        if record.parent_id > record.record_id:
            raise ValueError('Node parent_id should be smaller than it\'s record_id.')
        if record.parent_id == record.record_id:
            raise ValueError('Only root should have equal record and parent id.')
        new_node = Node(record.record_id)
        nodes[record.record_id] = new_node
        nodes[record.parent_id].children.append(new_node)
    
    return root
