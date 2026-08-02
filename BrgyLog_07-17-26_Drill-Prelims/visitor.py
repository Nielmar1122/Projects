from datetime import datetime

class Visitor:
    """Class representing a visitor"""
    
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose
        self.timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    def __str__(self):
        return f"{self.name} - {self.purpose} ({self.timestamp})"

# Optional: If you prefer a simple function-based log manager
def add_visitor(log, name, purpose):
    log.append((name, purpose))
    print(f"\n✓ Si {name} ay naitala na sa logbook.")