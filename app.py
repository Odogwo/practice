from flask import Flask, render_template

app = Flask(__name__)

# Data for the table
data = [
    ('Alegbeleyem', 'Ctsoa4%5'),
    ('AkintomideE', 'Jyloo4!2'),
    ('Uchenduc', 'Jvnhd1-9'),
    ('solomonJ', 'Lanak3#5'),
    ('Okoliep', 'Trans8+9'),
    ('Nwachip', 'Noona8%4'),
    ('Salami', 'Lxaal3/3'),
    ('Nwaobilorg', 'Kztlg7.8'),
    ('JeremiahH', 'Rsmnl7*5'),
    ('Ekeohao', 'Hocky3+8'),
    ('AsaS', 'Jtpqm7(1'),
    ('AlphaeusC', 'Housa9-8'),
    ('Ajikech', 'Djinn3%9'),
    ('ReubenB', 'Ddbms7%3'),
    ('UbochiG', 'Wklin6%3'),
    ('IgweD', 'Deepa7-3'),
    ('Rosanwok', 'Pkmaf1&3'),
    ('NwaobiloO', 'Bofag6(5'),
    ('OkonkohC', 'Okoly0.9'),
    ('Ekeohao', 'Hocky3+8')
]

@app.route('/')
def index():
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
