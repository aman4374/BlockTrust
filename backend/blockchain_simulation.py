import random

class Node:
    def __init__(self, id, initial_trust=100, stake=50):
        self.id = id
        self.trust_score = initial_trust
        self.stake = stake
        self.reputation = 1.0

    def choose_action(self):
        honesty_factor = (self.trust_score / 100) * self.reputation
        return "Honest" if random.random() < honesty_factor else "Dishonest"

    def update_reputation(self, honest_behavior):
        if honest_behavior:
            self.reputation = min(self.reputation + 0.1, 1.0)
        else:
            self.reputation = max(self.reputation - 0.2, 0.1)

def simulate_interaction(node1, node2):
    action1 = node1.choose_action()
    action2 = node2.choose_action()

    if action1 == "Honest" and action2 == "Honest":
        node1.trust_score = min(node1.trust_score + 5, 100)
        node2.trust_score = min(node2.trust_score + 5, 100)
        node1.update_reputation(True)
        node2.update_reputation(True)
    elif action1 == "Dishonest" and action2 == "Dishonest":
        node1.trust_score = max(node1.trust_score - 10, 0)
        node2.trust_score = max(node2.trust_score - 10, 0)
        node1.update_reputation(False)
        node2.update_reputation(False)
    elif action1 == "Honest" and action2 == "Dishonest":
        node1.trust_score = max(node1.trust_score - 5, 0)
        node2.trust_score = min(node2.trust_score + 10, 100)
        node1.update_reputation(True)
        node2.update_reputation(False)
    else:
        node1.trust_score = min(node1.trust_score + 10, 100)
        node2.trust_score = max(node2.trust_score - 5, 0)
        node1.update_reputation(False)
        node2.update_reputation(True)

    return action1, action2

def calculate_penalty(node):
    return max(node.stake * (1 - node.reputation), 0)

def run_simulation():
    nodes = [Node(i, random.randint(70, 100), random.randint(30, 100)) for i in range(10)]
    simulation_result = []

    for _ in range(10):
        node1, node2 = random.sample(nodes, 2)
        action1, action2 = simulate_interaction(node1, node2)
        round_data = []

        for node in nodes:
            penalty = calculate_penalty(node)
            round_data.append({
                "id": node.id,
                "trust_score": node.trust_score,
                "reputation": round(node.reputation, 2),
                "stake": node.stake,
                "penalty": round(penalty, 2),
                "action": action1 if node == node1 else action2 if node == node2 else "None"
            })
        simulation_result.append(round_data)

    return simulation_result
