import datetime
from flask import Flask, render_template, request, redirect, url_for, abort
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security import Security, SQLAlchemyUserDatastore
import cloudinary.uploader


# initialize app
app = Flask(__name__)
manager = Manager(app)
app.config.from_object('punchstarter.default_settings')

# enable database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from punchstarter.models import *

# flask security
from forms import ExtendedRegisterForm
user_datastore = SQLAlchemyUserDatastore(db, Member, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)


@app.route("/")
def hello():
    projects = db.session.query(Project).order_by(Project.time_created.desc()).limit(15)
    return render_template("index.html", projects=projects)


@app.route("/projects/create/", methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        # handle form
        print request.form
        print request.files
        now = datetime.datetime.now()
        time_end = request.form.get('funding_end_date')
        time_end = datetime.datetime.strptime(time_end, '%Y-%m-%d')

        # upload cover photo
        cover_photo = request.files['cover_photo']
        uploaded_image = cloudinary.uploader.upload(
            cover_photo,
            crop='limit',
            width=680,
            height=550
        )
        image_filename = uploaded_image['public_id']
        new_project = Project(
            member_id=1,  # guest creator
            name=request.form.get("project_name"),
            short_description=request.form.get('short_description'),
            long_description=request.form.get('long_description'),
            goal_amount=request.form.get('funding_goal'),
            image_filename=image_filename,
            time_start=now,
            time_end=time_end,
            time_created=now
        )

        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('project_detail', project_id=new_project.id))


@app.route('/projects/<int:project_id>/')
def project_detail(project_id):
    project = db.session.query(Project).get(project_id)
    if not project:
        abort(404)

    return render_template('project_detail.html', project=project)


@app.route('/projects/<int:project_id>/pledge/', methods=['GET', 'POST'])
def pledge(project_id):
    project = db.session.query(Project).get(project_id)
    if not project:
        abort(404)
    if request.method == "GET":
        return render_template("pledge.html", project=project)
    if request.method == "POST":
        guest_pledgor = db.session.query(Member).filter_by(id=2).one()
        new_pledge = Pledge(
            member_id=guest_pledgor.id,
            project_id=project.id,
            amount=request.form.get('amount'),
            time_created=datetime.datetime.now()
        )
        db.session.add(new_pledge)
        db.session.commit()

        return redirect(url_for('project_detail', project_id=project.id))


@app.route('/search/')
def search():
    query = request.args.get("q") or ""
    projects = db.session.query(Project).filter(
        Project.name.ilike('%' + query + '%') |
        Project.short_description.ilike('%' + query + '%')  |
        Project.long_description.ilike('%' + query + '%')
    ).all()
    project_count = len(projects)
    return render_template('search.html',
                           query_text=query,
                           projects=projects,
                           proejct_count=project_count)