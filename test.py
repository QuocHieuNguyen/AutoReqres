import requests

print("Xin chào!")


def sd():
    print("something")


sd()
import re


def remove_html(txt):
    return re.sub(r'<[^>]*>', '', txt)


txt = "<p class=\"par\">This is an example</p>"
print(remove_html(txt))

response = requests.get("http://api.open-notify.org/astros.json")
print(response)


def calc_addition(a, b):
    return a + b


def test_calc_addition():
    # Verify the output of `calc_addition` function
    output = calc_addition(2, 4)
    assert output == 6
# print(response.content()) # Return the raw bytes of the data payload
# test = response.text()
# print(test+ "")  # Return a string representation of the data payload
# print(response.json())  # This method is convenient when the API returns JSON
