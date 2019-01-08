#1.connect database
import mlab
from mongoengine import Document,StringField,IntField
mlab.connect()

#2.define model(document)
class Movie(Document):
    title = StringField()
    image = StringField()
    link  = StringField()
    rate = IntField()

movie_list = Movie.objects(rate__gte = 7,title = "Aquaman")   #lazy loading 
for m in movie_list:
    print(m.title,m.rate)
#3.create data
# m = Movie(title = "Aquaman",
#                    image = "https://trainghiemso.vn/wp-content/uploads/2018/04/spider-man-ps4-pro-featured.jpg",
#                    link = "https://www.imdb.com/title/tt0145487/",
#                    rate = 6)
# m.save()