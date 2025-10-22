class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, job):
        self.heap.append(job)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)][1] < self.heap[index][1]:
            # Swap with parent if current job priority is greater
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left][1] > self.heap[largest][1]:
            largest = left

        if right < len(self.heap) and self.heap[right][1] > self.heap[largest][1]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        return self.heap[0] if self.heap else None

    def display(self):
        print("Current Heap (Job, Priority):")
        for job in self.heap:
            print(job)


# Example usage:
jobs = MaxHeap()

# Each job is a tuple: (job_name, priority)
jobs.insert(("Job1", 4))
jobs.insert(("Job2", 2))
jobs.insert(("Job3", 5))
jobs.insert(("Job4", 1))

jobs.display()

print("\nPeek highest priority job:", jobs.peek())

print("\nDelete highest priority job:", jobs.delete())

print("\nHeap after deletion:")
jobs.display() 
