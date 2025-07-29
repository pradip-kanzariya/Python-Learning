import threading
import time
# 2. Concurrency and Parallelism

# Practice Task : 2 | Write a multi-threaded program to simulate a ticket booking system.
class TicketBookingSystem:
    """Ticket booking class using threading for parallel threads."""
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.lock = threading.Lock()

    def book_ticket(self, name, tickets):
        print("Wait for the process...")
        time.sleep(1)
        with self.lock:
            if name and tickets <= self.total_tickets:
                self.total_tickets -= tickets
                print(f"{name} successfully booked {tickets} tickets.")
            else:
                print("Booking Failed.")
                print(f"Sorry, We have {self.total_tickets} tickets left.")

booking_system = TicketBookingSystem(total_tickets=5)

def user_book(name, tickets):
    booking_system.book_ticket(name, tickets)

users = [
    ("Alice", 2),
    ("Bob", 1),
    ("Charlie", 2),
    ("Diana", 1),
]

start_time = time.time()
threads = []
for name, ticket in users:
    t = threading.Thread(target=user_book, args=(name, ticket))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Total time: {end_time - start_time:.2f} seconds")
