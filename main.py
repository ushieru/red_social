from src import app
from src.database import engine, Base
import src.models

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(host='0.0.0.0', debug=True)
