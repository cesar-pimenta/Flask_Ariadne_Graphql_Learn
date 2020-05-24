import os
from flask_cors import CORS
from ariadne import QueryType, graphql_sync, make_executable_schema, ObjectType, gql
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import requests, json

type_defs = gql("""

    type Query {
        hello: String
        username: String
    }
""")

query = ObjectType("Query")

@query.field("hello")
def resolve_hello(*_):
    return 'hello'

@query.field("username")
def resolve_username(obj,*_):
    field_json = jsonify({
        'name':'cesar',
        'name':'cesar'
    })
    print(dir(field_json))
    print(json(field_json))
    return 'text'

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

cors = CORS(app, resource={r"/*":{"origins": "*"}})

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()

