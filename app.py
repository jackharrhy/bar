import os
import markovify
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import uvicorn

knowledge = open("knowledge.txt", "r")
chain = markovify.Text(knowledge.read())
knowledge.close()

async def get_sentence(request):
    sentence = chain.make_sentence()
    return PlainTextResponse(sentence)

app = Starlette(debug=True, routes=[
    Route('/', get_sentence),
])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
