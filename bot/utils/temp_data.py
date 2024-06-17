from utils.singleton import Singleton


class UserState:

    __userState = {}


    # User state
    @classmethod    
    def getUserState(cls, chat_id):
        return cls.__userState.get(chat_id, "")

    @classmethod    
    def updateUserState(cls, chat_id, state):
        cls.__userState.update({chat_id: state})

    @classmethod    
    def dropUserState(cls, chat_id):
        try:
            cls.__userState.pop(chat_id)
        except Exception as e:
            print(e)
