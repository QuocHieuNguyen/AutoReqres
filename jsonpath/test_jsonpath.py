import jsonpath_ng

json_data = {
    'foo':
        [
            {
                'baz': 1
            },
            {
                'baz': 2
            }
        ]
}
jsonpath_expr = jsonpath_ng.parse('foo[*].baz')
# Parsing the values of JSON data
list_val = [match.value for match in jsonpath_expr.find(json_data)]
# print jsonpath_expr
print(dir(jsonpath_expr))
# Printing the parsed values
print(list_val)
# Print find data
# print(*jsonpath_expr.find(json_data), sep = "\n")
# print(jsonpath_expr.find(json_data)[0])
# print(jsonpath_expr.find(json_data)[0].value)
# print(jsonpath_expr.find(json_data)[0].path)
# print(jsonpath_expr.find(json_data)[0].context.value)
print([match.value for match in
       jsonpath_ng
        .parse('$.a.*.b.`parent`')
        .find(
           {
               'a':
                   {
                       'x':
                           {
                               'b': 1,
                               'c': 'number one'
                           },
                       'y':
                           {
                               'b': 2,
                               'c': 'number two'
                           }
                   }
           }
       )
       ]
      )
