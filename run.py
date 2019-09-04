
from app import create_app,db
from app.models import Customer, Order


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Customer': Customer, 'Order': Order}


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)



