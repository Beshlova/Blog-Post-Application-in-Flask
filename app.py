from website import create_app,db
from flask_migrate import init,migrate,upgrade,stamp

app = create_app()
app.app_context().push()#Pushes the application context of create_app 

# db.create_all()

# init()
# migrate()
# upgrade()
# stamp()



if __name__=='__main__':
 app.run(debug=True)