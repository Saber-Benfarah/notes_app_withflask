from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
notes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def note_list():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        notes.append({'title': title, 'content': content})
        return redirect(url_for('note_list'))
    return render_template('notes.html', notes=notes)

@app.route('/delete/<int:index>')
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for('note_list'))

if __name__ == '__main__':
    app.run(debug=True)
