from collections import NodeQueue
import time

class PlayList(NodeQueue):

    def __init__(self):
        NodeQueue.__init__(self)
        self.current = None
    

    def __iter__(self):
        probe = self.head
        while probe:
            element = probe.data
            probe = probe.next
            yield element


    def play_songs(self):
        for song in self:
            print(f'Playing: {song} ...')
            time.sleep(5)
