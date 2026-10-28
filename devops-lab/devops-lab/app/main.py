from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store for now. We replace this with a real database in Layer 7.
notes = {}
next_id = 1


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/notes")
def list_notes():
    return jsonify(list(notes.values())), 200


@app.post("/notes")
def create_note():
    global next_id
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify(error="text is required"), 400
    note = {"id": next_id, "text": text}
    notes[next_id] = note
    next_id += 1
    return jsonify(note), 201


@app.get("/notes/<int:note_id>")
def get_note(note_id):
    note = notes.get(note_id)
    if note is None:
        return jsonify(error="not found"), 404
    return jsonify(note), 200


@app.delete("/notes/<int:note_id>")
def delete_note(note_id):
    if notes.pop(note_id, None) is None:
        return jsonify(error="not found"), 404
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
