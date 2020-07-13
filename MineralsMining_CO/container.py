#!/usr/bin/env python3
"""
Container Module
"""

from datetime import datetime
import uuid

class Container:
    """Container Class"""
    def __init__(self, c_id, slot_number, mineral_type, weight_stored,
                storage_manager_id, next_container=None,
                previous_container=None, date_removed=None):
        self.capacity = 2.0
        if c_id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = c_id
        self.slot_number = slot_number
        self.mineral_type = mineral_type
        self.weight_stored = weight_stored
        self.date_received = datetime.now()
        self.next_container = next_container
        if next_container:
            self.next_container_slot = next_container.slot_number
            self.next_container_id = next_container
        else:
            self.next_container_slot = None
            self.next_container_id = None
        self.previous_container = previous_container
        if previous_container:
            self.previous_container_slot = previous_container.slot_number
            self.previous_container_id = previous_container
        else:
            self.previous_container_slot = None
            self.previous_container_id = None
        self.storage_manager_id = storage_manager_id
        self.date_removed = date_removed
        

# cont = Container(1, "oro", "200kg", "12345")
# print(dir(cont))
# print(cont.__dict__)