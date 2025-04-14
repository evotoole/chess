import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Dict, Optional, TypedDict
from pieces import *
from server.illegal_match_access_error import IllegalMatchAccessException

from uuid import uuid4

class Player:
    def __init__(self, id: str):
        self.id = id

class Match:
    def __init__(self, session_id: str, p1: str, p2: str):
        self.referee = Referee()
        self.session_id = session_id
        self.p1 = Player(p1)
        self.p2 = Player(p2)

        self.p1_joined = False
        self.p2_joined = False
        self.ready = self.p1_joined and self.p2_joined
        self.current_in_turn = self.p1.id

    def joined(self, id: str) -> None:
        if self.p1.id == id:
            self.p1_joined = True

        if self.p2.id == id:
            self.p2_joined = True

        self.ready  = self.p1_joined and self.p2_joined

    def handle_player_move(self, player_id: str, move: str):
        if self.current_in_turn != player_id:
            return
        return []


MatchesSchema = Dict[ str, Match ]
class MatchMaking:
    def __init__(self):
        self.matches: MatchesSchema = {}

    def create_game(self) -> tuple[ str, str ]:
        session_id, p1, p2 = str(uuid4()), str(uuid4()), str(uuid4())
        M = Match( session_id, p1, p2 )
        self.matches[ M.session_id ] =  M
        return  ( M.session_id, M.p1.id )

    def join_game(self, sesh_id: str) -> str:
        if not self.matches[ sesh_id ]:
            raise IllegalMatchAccessException('Trying to access a non-existent match') 
        return self.matches[ sesh_id ].p2.id

    def get_game(self, sesh_id: str) -> Match:
        if not self.matches[ sesh_id ]:
            raise IllegalMatchAccessException('Trying to access a non-existent match') 
        return self.matches[ sesh_id ]



