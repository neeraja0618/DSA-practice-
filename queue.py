queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)
queue.pop(0)
print("After dequeue:", queue)

#peek front element 
queue = [10, 20, 30]
if queue:
    print("Front element:", queue[0])
else:
    print("Queue is empty")
