from collections import deque
import random
 
class CallCentre:
    def __init__(self, name, agents):
        self.name   = name
        self.agents = agents
        self.queue  = deque()
        self.total_served = 0
 
    def incoming_call(self, caller, issue):
        self.queue.append({'caller': caller, 'issue': issue})
        print(f'  CALL IN: {caller} → "{issue}"  [Queue: {len(self.queue)}]')
 
    def handle_calls(self):
        print(f'  --- {self.agents} agents handling calls ---')
        while self.queue:
            for agent_id in range(1, self.agents + 1):
                if not self.queue:
                    break
                call = self.queue.popleft()   # FIFO
                print(f'  Agent-{agent_id} → {call["caller"]}: "{call["issue"]}"')
                self.total_served += 1
        print(f'  Total calls handled: {self.total_served}')
 
 
cc = CallCentre('TechSupport Ltd', agents=2)
print('Incoming calls:')
cc.incoming_call("Ramesh",  "Cannot login")
cc.incoming_call("Sita",    "Slow internet")
cc.incoming_call("Gopal",   "Billing query")
cc.incoming_call("Lalitha", "App crashing")
cc.incoming_call("Naresh",  "Password reset")
print()
cc.handle_calls()
