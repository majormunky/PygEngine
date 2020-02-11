class CycleTimer:
    def __init__(self, cycle_time, amount):
        self.cycle_time = cycle_time
        self.timer = 0
        self.index = 0
        self.max_index = amount

    def add_time(self, dt):
        self.timer += dt
        if self.timer > self.cycle_time:
            self.timer = 0
            self.index += 1
            if self.index > self.max_index:
                self.index = 0

    def get_current(self):
        return self.index
