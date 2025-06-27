from flask import Flask
from flask_cors import CORS
from extensions import db
from routes.auth import auth_bp
from routes.posts import posts_bp
from graphql.schema import graphql_schema
from flask_graphql import GraphQLView

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    CORS(app)
    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(posts_bp, url_prefix="/api/posts")

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=graphql_schema, graphiql=True)
    )

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
