from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolvers as r
import os


type_defs = load_schema_from_path('schema.graphql')

query = QueryType()

query.set_field('githubSearchUser', r.resolve_apigithub_search_user)
query.set_field('githubListReposName', r.resolve_apigithub_list_repos)
query.set_field('githubReposInfo', r.resolve_apigithub_repos_info)
query.set_field('githubReposInfoOptions', r.resolve_apigithub_repos_info_options)

# mutation = MutationType()
# mutation.set_field('createRepos', r.resolve_create_repos)

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)

@app.route('/')
def hello():
    return "access /graphql"


@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()