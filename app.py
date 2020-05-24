from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify, escape
import resolvers as r
import os


type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
studentType = ObjectType('Student')
classType = ObjectType('Class')
userType = ObjectType('User')

mutation = MutationType()
mutation.set_field('createStudent', r.resolve_student_create)
mutation.set_field('createClass', r.resolve_class_create)
mutation.set_field('addStudentToClass', r.resolve_add_student_to_class)
mutation.set_field('createUser', r.resolve_user_create)


query.set_field('studentById', r.resolve_student_by_id)
query.set_field('classById', r.resolve_class_by_id)
query.set_field('students', r.resolve_students)
query.set_field('classes', r.resolve_classes)
query.set_field('users', r.resolve_users)
classType.set_field('students', r.resolve_students_in_classes)

schema = make_executable_schema(type_defs, [studentType, classType, query, mutation])

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


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