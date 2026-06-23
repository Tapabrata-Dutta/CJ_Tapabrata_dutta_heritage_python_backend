from collections import deque
 
class OfficePrinter:
    def __init__(self, model):
        self.model = model
        self.queue = deque()     # Job queue
        self.done  = []
 
    def submit(self, user, document, pages):
        job = {'user':user, 'doc':document, 'pages':pages}
        self.queue.append(job)
        print(f'  QUEUED: [{user}] "{document}" ({pages}p) | Queue: {len(self.queue)}')
 
    def print_next(self):
        if not self.queue:
            print('  Printer idle — no jobs.')
            return
        job = self.queue.popleft()   # FIFO
        print(f'  PRINTING: [{job["user"]}] "{job["doc"]}" ({job["pages"]}p)')
        self.done.append(job)
 
    def print_all(self):
        print(f'  --- {self.model} processing all jobs ---')
        while self.queue:
            self.print_next()
        print(f'  Done. {len(self.done)} job(s) completed.')
 
 
printer = OfficePrinter('Canon-iR-Adv')
print('Submitting print jobs:')
printer.submit("Arun",    "Budget Report",   15)
printer.submit("Meena",   "Project Slides",  32)
printer.submit("HR Dept", "Leave Policy",     8)
printer.submit("Vikram",  "Client Invoice",   3)
print()
printer.print_all()
