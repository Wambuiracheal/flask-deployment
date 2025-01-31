# from random import randint, choice as c
# from faker import Faker
# from models import User, Artwork, Exhibition,db
# from app import app

# fake = Faker()
# with app.app_context():
#     User.query.delete()
#     Artwork.query.delete()
#     Exhibition.query.delete()

#     users = []
#     for _ in range(10):
#         user = User(
#             name=fake.name(),
#             email=fake.email(),
#         )

#         users.append(user)
#         db.session.add(user)

#     artworks = []
#     for _ in range(10):
#         artwork = Artwork(
#             artist = fake.name(),
#             title = fake.catch_phrase(),
#             image = fake.url(),
#             price = randint(10000, 100000),
#             category = c(['painting','sculpture','photography'])
#         )

#         artworks.append(artwork)
#         db.session.add(artwork)

#     exhibitions = []
#     for _ in range(10):
#         exhibition = Exhibition(
#             user_id = c(range(10)),
#             artwork_id = c(range(10)),
#         )
        
#         exhibitions.append(exhibition)
#         db.session.add(exhibition)

#         db.session.commit()