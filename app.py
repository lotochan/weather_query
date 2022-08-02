from flask import Flask
from flask import render_template
from flask import request
from query_main import get_weather_information

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    """
    main function about the weather query
    :return:
    """
    if request.method == "GET": # show the template index.html
        return render_template("index.html")

    if request.method == "POST": # query weather
        result_dict = {
            "success":1,
        }

        if request.form: # if query success
            city = request.form.get("city")
            if city:
                result = get_weather_information(city)
                if result:
                    result_dict["result"] = result
                    return result_dict

        else: # if query fail
            result_dict["success"] = 0
            return result_dict


@app.errorhandler(Exception)
def page_not_found(error):
    return render_template("error.html",data=error)




if __name__ == '__main__':
    app.run()
