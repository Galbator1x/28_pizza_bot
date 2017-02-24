from server import app, db

with app.app_context():
    db.drop_all() # FIXME DEBUG ONLY!!!!!!!!!
    db.create_all()
