from fastapi import FastAPI, WebSocket, WebSocketException, WebSocketDisconnect
from starlette.websockets import WebSocketClose
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from illegal_match_access_error import IllegalMatchAccessException
from match_making import Match, MatchMaking

app = FastAPI()
mm = MatchMaking()


@app.get('/')
async def root():
    return { 'message': 'hello world' }

'''
    FLOW
        1. Player 1 hits /pvp/create-game, which creates a match instance and returns a session_id and player_id.
        2. Player 1 gets redirected to /pvp/{session_id}.
        3. Player 2 accepts the invite link, which hits /pvp/join-game, passing the session_id and creating a 2nd player_id.
        4. Player 2 gets redirected to /pvp/{session_id}.
        5. /pvp/{session_id} handles the game until the match is over.
'''

@app.post('/pvp/create-game')
async def pvp_create_game():
    session_id, player_id = mm.create_game()
    return { 'session_id': session_id, 'player_id': player_id }

@app.post('/pvp/join-game')
async def pvp_join_game(session_id: str):
    player_id:str = mm.join_game(session_id)
    return { 'player_id': player_id }

@app.websocket('/pvp/{session_id}')
async def pvp(ws: WebSocket, session_id: str):
    try:

        await ws.accept()
        match: Match = mm.get_game(session_id)

        while True:
            player_data = await ws.receive_json()
            player_id = player_data.get('player_id', None)
            player_move = player_data.get('move', None)

            if player_id:
                match.joined(player_id)

            if player_id and player_move and match.ready:
                payload =match.handle_player_move(player_id, player_move)
                await ws.send_json( payload )
            

    except WebSocketException:
            print(f'')

    except IllegalMatchAccessException:
            print(f'')

    except Exception as e:
            print(f'')

@app.get('/pve/{session_id}')
async def pve():
    return { 'message': 'hello world' }

