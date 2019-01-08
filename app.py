from flask import Flask,render_template
app = Flask(__name__)

@app.route('/character')
def character():


    c_list = [
        {
        "name":"brucelee",
        "image":  "https://pbs.twimg.com/media/Du36t7JVsAAHUnm.jpg",
        "link" : "https://www.google.com/search?q=bruce+lee&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiT_trX29bfAhWHQd4KHcZ4DHgQ_AUIDigB&biw=1366&bih=626#imgrc=lUroLupCmJQOsM:"              
    },
    {
        "name":"thanos",
        "image":  "https://terrigen-cdn-dev.marvel.com/content/prod/1x/019tha_ons_crd_02.jpg",
        "link" : "https://www.google.com/search?q=thanos&source=lnms&tbm=isch&sa=X&ved=0ahUKEwilybPe3dbfAhUDFYgKHT9bCIYQ_AUIDigB&biw=1366&bih=626#imgrc=Z8zvphx2lKABvM:"              
    },
    {
        "name":"captain marvel",
        "image":  "https://pbs.twimg.com/media/Du36t7JVsAAHUnm.jpg",
        "link" : "https://www.google.com/search?q=bruce+lee&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiT_trX29bfAhWHQd4KHcZ4DHgQ_AUIDigB&biw=1366&bih=626#imgrc=lUroLupCmJQOsM:"              
    }
    ]
    return render_template("characters_list.html",
                             character_list = c_list)
@app.route("/names")
def Name():
    name_list = [ "Hung","Quan","Huy","Son","Tuan","Khanh"] 
    return render_template("name.html",
                            name_list = name_list)
f_items = [
        {
            "name" : "Bun cha",
            "image": "http://via.placeholder.com/200x200",
            "link": "http://google.com?q=bun+cha",
            "ytid" : "xUumKYLf6fs"
        },
        {
            "name" : "Bun ca",
            "image": "http://via.placeholder.com/200x200",
            "link": "http://google.com?q=bun+cha",
            "ytid": "w_6Rk_23-y0"

        },
        {
            "name" : "Bun bo",
            "image": "http://via.placeholder.com/200x200",
            "link": "http://google.com?q=bun+cha",
            "ytid": "vHICg8y2NbQ"
        },
    ]

@app.route("/food_items")
def food():
    return render_template("food.html",
                            food_items = f_items)


@app.route("/food_detail/<int:index>")
def food_detail(index): #tren co j thi duoi phai co cai y
    f_item = f_items[index]
    return render_template("food_detail.html", food_item = f_item)



if __name__ == '__main__':
  app.run(debug=True)