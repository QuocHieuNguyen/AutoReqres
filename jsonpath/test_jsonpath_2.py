# # List
#
# data = ["car", "bus", "truck"]
# import jsonpath_ng
# x = jsonpath_ng.parse('$[0]').find(data)
# print(str(x[0].value))
import jsonpath_ng

data = {
    "car": {
        "color": "blue",
        "price": "$20000",
        "wheels": [
            {
                "model": "X23",
                "location": "front-right"
            },
            {
                "model": "X24",
                "location": "front-back"
            }
        ]
    }
}
x = jsonpath_ng.parse('$.car.wheels[0]').find(data)
print(x[0].value)
# Working with expression
y = jsonpath_ng.parse('$.car.wheels[?(@.location == "front-back")]').find(data)
print(y[0])