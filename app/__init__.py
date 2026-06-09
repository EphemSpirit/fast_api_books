from fastapi import FastAPI

def create_app():
    app = FastAPI()

    from app.routes import register_routes
    register_routes(app)

    return app