from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database.db_connection import get_session, model
from models.movie_model import Movie
from chatbot.recommendation import get_chatbot_recommendation
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MovieRequest(BaseModel):
    query: str

class MovieResponse(BaseModel):
    movie: str
    description: str

@app.post("/chat/")
async def get_recommendations(request: MovieRequest):
    try:
        # Get chatbot response
        print('called')
        model_input = get_chatbot_recommendation(request.query)
        
        # Generate embedding
        print(f'query: {model_input}')
        query_embedding = model.encode(model_input, batch_size=12, max_length=8192)['dense_vecs']

        print('embedding done')
        
        # Get session and query database
        session = get_session()
        try:
            movies = session.execute(
                select(Movie)
                .order_by(Movie.embedding.cosine_distance(query_embedding))
                .limit(5)
            ).scalars().all()
            
            return {
                "recommendations": [
                    {"movie": movie.movie, "description": movie.description}
                    for movie in movies
                ]
            }
        finally:
            session.close()
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
