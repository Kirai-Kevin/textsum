import asyncio

class Flow:
    def __init__(self):
        self.actions = {}

    def add_action(self, name, action):
        self.actions[name] = action

    async def execute_action(self, name, data):
        action = self.actions.get(name)
        if action:
            return await action.execute(data)  # Ensure 'await' is used correctly
        else:
            raise ValueError(f"Action '{name}' not found.")
