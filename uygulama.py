from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    highest_score = db.Column(db.Integer, default=0)
    last_score = db.Column(db.Integer, default=0)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    option_1 = db.Column(db.String(100), nullable=False)
    option_2 = db.Column(db.String(100), nullable=False)
    option_3 = db.Column(db.String(100), nullable=False)
    option_4 = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


    if not Question.query.first():


        q1 = Question(
            question_text="Aşağıdakilerden hangisi discord.py kütüphanesini yüklemek için kullanılan bir komuttur ?",
            option_1="pip install ",
            option_2="import discord.py",
            option_3="<stdio.h> discord.py",
            option_4="Hepsi",
            correct_option="pip install "
        )
        db.session.add(q1)

        q2 = Question(
            question_text="discord.py kütüphanesi ile ilgili aşağıdakilerden hangisi doğrudur? ",
            option_1="Python'da görselleştirme için kullanılır",
            option_2="Python programlama dili için popüler bir kütüphanedir ve Discord API'sini kullanarak botlar oluşturmanıza olanak tanır.",
            option_3="Bir veri setinde istenilen düzeyde analiz yapmak içindir",
            option_4="Pyhton'ın yapay zeka kütüphanesidir",
            correct_option="Python programlama dili için popüler bir kütüphanedir ve Discord API'sini kullanarak botlar oluşturmanıza olanak tanır."
        )
        db.session.add(q2)

        q3 = Question(
            question_text="Python ile web sitesi geliştirmek istiyorsunuz. Buna göre aşağıdaki frameworklerden hangisini kullanmanız uygun olacaktır?",
            option_1="Flask",
            option_2="BeautifulSoup",
            option_3="RoBERTa",
            option_4="XLNET",
            correct_option="Flask"
        )
        db.session.add(q3)

        q4 = Question(
            question_text="Flask ile ilgili aşağıda verilen bilgilerden hangisi yanlıştır",
            option_1="Flask Jinja2 şablonlarını kullanır.",
            option_2="WSGI ile uyumludur.",
            option_3="Birim testi için destek sağlar",
            option_4="Doğal Dil İşleme alanında en çok kullanılan kütüphanedir",
            correct_option="Doğal Dil İşleme alanında en çok kullanılan kütüphanedir"
        )
        db.session.add(q4)

        q5 = Question(
            question_text="Pyhton ile yapay zeka modeli geliştirmek için aşağıdaki kütüphanelerden hangisi kullanılır",
            option_1="Pandas",
            option_2="NumPy",
            option_3="Scikit-learn",
            option_4="Hepsi",
            correct_option="Hepsi"
        )
        db.session.add(q5)

        q6 = Question(
            question_text="Bilgisayarların verilerden öğrenmesini ve daha sonra bu öğrenilen bilgileri kullanarak tahminler yapmasını sağlayan ve Pyhton programlama dili kullanan alanın adı nedir ?",
            option_1="Makine Öğrenmesi",
            option_2="Web Geliştirme",
            option_3="Siber Güvenlik",
            option_4="Yazılım Geliştirme",
            correct_option="Makine Öğrenmesi"
        )
        db.session.add(q6)

        q7 = Question(
            question_text="TensorFlow bilgisayar görüşü uygulamaları geliştirmek için yaygın olarak kullanılan kütüphanedir. Buna göre I. Google tarafından geliştirilen açık kaynaklı bir makine öğrenmesi kütüphanesidir. II.Nesne Tespiti için de kullanılır. III. Genellikle konvolüsyonel sinir ağları (CNN) gibi derin öğrenme modellerini kullanarak görüntü işleme yapar. verilenlerden hangisi doğrudur ?",
            option_1="Yalnız I ",
            option_2="I ve III",
            option_3="I,II,III",
            option_4="Hiçbiri",
            correct_option="I,II,III"
        )
        db.session.add(q7)

        q8 = Question(
            question_text="Videolarda nesne algılama, Özel Tanıma modellerinin eğitimi, video ve kamera besleme analizi ve modellerle nesneleri tanıma ile ilgili birçok gelişmiş özellik içeren Python'un açık kaynak kütüphanesi hangisidir? ",
            option_1="ImageAI  ",
            option_2="Metaspliot",
            option_3="NumPy",
            option_4="Hepsi",
            correct_option="ImageAI"
        )
        db.session.add(q8)

        q9 = Question(
            question_text="Python programlama dili kullanarak bir Doğal Dil İşleme projesi yürüttüğünüzü düşünün. Aşağıdaki frameworklerden hangisini web kazıma aşamasında kullanırsınız?",
            option_1="Matplot",
            option_2="TensorFlow",
            option_3="Flask",
            option_4="BeautifulSoup",
            correct_option="BeautifulSoup"
        )
        db.session.add(q9)

        q10 = Question(
            question_text="Verilen bir metin verisinin duygu analizini yapmayı amaçlar",
            option_1="Metin Özetleme ",
            option_2="Metin Önişleme",
            option_3="Dil Modelleme",
            option_4="Duygu Analizi",
            correct_option="Duygu Analizi"
        )
        db.session.add(q10)

        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

# Sınav sayfası
@app.route('/exam', methods=['GET', 'POST'])
def exam():
    questions = Question.query.all()
    if request.method == 'POST':
        score = 0
        total_questions = len(questions)


        for question in questions:
            answer = request.form.get(f'question_{question.id}')
            if answer == question.correct_option:
                score =score + 1

        # Her bir sorunun değeri 10 puan
        score_percentage = (score / total_questions) * 100


        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if user:
            user.last_score = score_percentage
            if score_percentage > user.highest_score:
                user.highest_score = score_percentage
        else:
            user = User(username=username, last_score=score_percentage, highest_score=score_percentage)
            db.session.add(user)

        db.session.commit()

        return redirect(url_for('result', score=score_percentage))

    return render_template('exam.html', questions=questions)


@app.route('/result')
def result():
    score = request.args.get('score', type=float)
    highest_score = User.query.order_by(User.highest_score.desc()).first().highest_score
    return render_template('result.html', score=score, highest_score=highest_score)

if __name__ == '__main__':
    app.run(debug=True)
