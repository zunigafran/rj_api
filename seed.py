from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="strawberry",
    size="medium",
    rating=10,
    image="https://grandbaby-cakes.com/wp-content/uploads/2019/07/Strawberry-cupcakes-02.jpg"
)

c4 = Cupcake(
    flavor="lemon",
    size="small",
    rating=9,
    image="https://sallysbakingaddiction.com/wp-content/uploads/2013/04/the-best-lemon-cupcakes-2.jpg"
)
db.session.add_all([c1, c2])
db.session.commit()