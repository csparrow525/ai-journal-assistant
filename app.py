from flask import Flask, render_template, request

app = Flask(__name__)

journals = []

@app.route("/", methods=["GET", "POST"])
def home():
    ai_response = ""
    if request.method == "POST":
        user_input = request.form["journal"]
        ai_response = f"[AI placeholder] You wrote: {user_input}"
        journals.append({"text": user_input, "ai_response": ai_response})
    return render_template("index.html", ai_response=ai_response, journals=journals)

@app.route("/view", methods=["GET"])
def display_journals():
    selected = request.args.get("selected_journal")
    entry = None
    entry_ai_response = None

    for journal in journals:
        if journal["text"] == selected:
            entry = journal["text"]
            entry_ai_response = journal["ai_response"]
            break

    return render_template("index.html", entry=selected, entry_ai_response=entry_ai_response, journals=journals)

if __name__ == "__main__":
    app.run(debug=True)