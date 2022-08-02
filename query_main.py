import requests
import json

def get_weather_information(city):
    """
    query weather api
    :param city: city - Chinese
    :return: weather detail [city,date,weather,low-high]
    """
    target_url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city={}&needMoreData=true&pageNo=1&pageSize=7".format(city)
    try:
        result = requests.get(target_url)
        result = json.loads(result.text)
        if result["code"] == 0:
            weather_result = result["data"]["list"]
            if weather_result:
                weather_result = weather_result[0]
                weather_result_detail = [weather_result["city"],weather_result["date"],weather_result["weather"],"{}°-{}°".format(weather_result["low"],weather_result["high"])]
                print(weather_result_detail)
                return weather_result_detail
            else:
                return 0
    except Exception as e:
        print(e)
        return 0


if __name__ == '__main__':
    get_weather_information("北京")
    get_weather_information("上海")
    get_weather_information("广州")
    get_weather_information("深圳")