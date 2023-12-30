from flask import Flask, jsonify, request

import model.hobby
import model.school
import model.task_type

app = Flask(__name__)

tasks = [
    model.school.School('1', 'this is a title', 'this is a body', 'not started'),
    model.hobby.Hobby('2', 'this is another title', 'this is another body', 'started')
    ]

###
# To make a successful post request to the school endpoint using cURL in a Windows environment, use the following syntax
# being sure to escape the double quotes in the data section:
# curl -X POST -H "Content-Type: application/json" -d "{\"id\":3, \"title\":\"third\", \"body\":\"bodybodybody\", \"status\": \"not started\"}" localhost:5000/school
###


@app.route('/school')
def get_schools():
    schema = model.school.SchoolSchema(many=True)
    schools = schema.dump(
        filter(lambda t: t.type == model.task_type.TaskType.SCHOOL, tasks)
    )
    return jsonify(schools)


@app.route('/school', methods=['POST'])
def add_school():
    school = model.school.SchoolSchema().load(request.get_json())
    tasks.append(school)
    return "", 204


@app.route('/hobby')
def get_hobbies():
    schema = model.hobby.HobbySchema(many=True)
    hobbies = schema.dump(
        filter(lambda t: t.type == model.task_type.TaskType.HOBBY, tasks)
    )
    return jsonify(hobbies)


@app.route('/hobby', methods=['POST'])
def add_hobby():
    hobby = model.hobby.HobbySchema().load(request.get_json())
    tasks.append(hobby)
    return "", 204


if __name__ == "__main__":
    app.run()
