from domain.event_handler import EventHandler, FightEventType


class FightLoggerInMemory(EventHandler):
    def __init__(self):
        self.messages = []

    def update(self, fight_action, fight):
        if fight_action.fight_action_type == FightEventType.USER_ACTION:
            for receiver in fight_action.receivers:
                self.messages.append(f'{fight.player.name} has attack {receiver.name}')
        elif fight_action.fight_action_type == FightEventType.MONSTER_ACTION:
            for receiver in fight_action.receivers:
                self.messages.append(f'{fight_action.fighter.name} has attack {receiver.name}')
        else:
            self.messages.append(f'New action: {fight_action.fight_action_type.value}')

    def last_message(self):
        if len(self.messages) > 0:
            return f'[Message {len(self.messages) - 1}] {self.messages[len(self.messages) - 1]}'
        return ''

    def get_messages_from(self, index: int):
        messages = []
        for msg in self.messages[index:]:
            messages.append(f'[Message] {msg}')
        return messages
