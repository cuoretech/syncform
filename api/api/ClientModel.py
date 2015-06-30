Base = neo4j.ext.declarative.declarative_base()
class ResourceOwner(Base):
    __tablename__ = "users"

    id = neo4j.Column(sqlalchemy.Integer, primary_key=True)
    name = neo4j.Column(sqlalchemy.String)
    email = neo4j.Column(sqlalchemy.String)
    password = neo4j.Column(sqlalchemy.String)