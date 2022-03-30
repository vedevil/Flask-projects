from flask import Flask, session, request
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLARLCHERY_DATABASE_URI']='sqlite:///data.db'
db= SQLAlchemy(app)


class Student(db.Model):
    id=db.Column(db.Integer,unique=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    dob=db.Column(db.String(10),nullable=False)
    pno=db.Column(db.String(10),nullable=False)
    add=db.Column(db.String(200))
    yoj=db.Column(db.Integer,nullable=False)
    dept=db.Column(db.String(20),nullable=False)
x
    def __repr__(self):
        return f'{self.name} {self.dob} {self.pno} {self.yoj} {self.add} {self.dept}'

class Teacher(db.Model):
    id=db.Column(db.Integer,unique=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    dob=db.Column(db.String(10),nullable=False)
    pno=db.Column(db.String(10),nullable=False)
    add=db.Column(db.String(200))
    dept=db.Column(db.String(20),nullable=False)
    course=b.column(db.String(80))
    def __repr__(self):
        return f'{self.name} {self.dob} {self.pno} {self.add} {self.dept} {self.course}'

@app.route('/')
def index():
    return str('Welcome to IIT bhilai')

@app.route('/students')
def get_students(req):
    if len(req)==0:
        studs=Student.query.all()
        output=[]
        for stu in studs:
            data={'Name':stu.name,'Date of birth':stu.dob}
            output.append(data)
        return {"students":output}
    else:
        studs=Student.query.all()
        output=[]
        for stu in studs:
            if 'course' in req:
                if stud.course==req['course']:
                    data={'name':stud.name,'dob':stud.dob,'pno':stud.pno,'add':stud.add,'yoj':stud.yoj,'dept':stud.dept}
            elif 'department' in req:
                {'name':stud.name,'dob':stud.dob,'pno':stud.pno,'add':stud.add,'yoj':stud.yoj,'dept':stud.dept}
            elif 'year' in req:
                {'name':stud.name,'dob':stud.dob,'pno':stud.pno,'add':stud.add,'yoj':stud.yoj,'dept':stud.dept
            output.append(data)
        return {"students":output}

@app.route('/student/<id>')
def get_student(id):
    stud=Student.query.get_or_404(id)
    return {'name':stud.name,'dob':stud.dob,'pno':stud.pno,'add':stud.add,'yoj':stud.yoj,'dept':stud.dept}

@app.route('/students, methods=['POST'])
def add_student():
    stud=Student(name=request.json['name'],dob=request.json['dob'],pno=request.json['pno'],add==request.json['add'],yoj=request.json['yoj'],dept=request.json['dept'])
    db.session.add(stud)
    db.session.commit()
    return {'id': stud.id}

@app.route('/teachers, methods=['POST'])
def add_teacher():
    teach=Teacher(name=request.json['name'],dob=request.json['dob'],pno=request.json['pno'],add==request.json['add'],dept=request.json['dept'],course=request.json['course'])
    db.session.add(teach)
    db.session.commit()
    return {'id': teach.id}