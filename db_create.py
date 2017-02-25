from models import Base
from server import engine

Base.metadata.create_all(engine)
