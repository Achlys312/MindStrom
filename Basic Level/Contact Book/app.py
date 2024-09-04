from flask import Flask, request, jsonify
app = Flask(__name__)

contacts = []

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    contacts.append(data)
    return jsonify({'message': 'Contact added successfully'})

@app.route('/contacts/<int:index>', methods=['PUT'])
def update_contact(index):
    data = request.get_json()
    contacts[index] = data
    return jsonify({'message': 'Contact updated successfully'})

@app.route('/contacts/<int:index>', methods=['DELETE'])
def delete_contact(index):
    del contacts[index]
    return jsonify({'message': 'Contact deleted successfully'})

@app.route('/contacts/search', methods=['GET'])
def search_contact():
    name = request.args.get('name')
    result = [contact for contact in contacts if contact['name'] == name]
    return jsonify(result)

if __name__ == '__main__':
    app.run()