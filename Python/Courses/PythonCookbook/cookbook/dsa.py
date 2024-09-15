"""
This is the data structures and algorithms package
"""

from collections import deque

class DSA:
    def __init__(self):
        self.tutorial_name = "Data Structure and Algorithms"

    def get_historial_data(self,lst: list[str], history: int = 5):
        """
        This function takes a list and a along with the current value, returns the past history
        of to size of history
        """
        def get_history():
            """
            Note: this is a internal function
            """
            queue = deque(maxlen=history)
            for line in lst:
                yield line, queue
                queue.append(line)
        
        for line, hist in get_history():
            yield line, hist
            


