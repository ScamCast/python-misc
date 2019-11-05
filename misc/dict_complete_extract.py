from pprint import pprint as pp

test = {
   "Name": "John",
   "Scores": [
      87,
      90,
      95,
      47,
      98,
      {
         "special_Key": "special_value",
         "secret_numbers": [
            11,
            22,
            33,
            44,
            {
               "hidden_key": "You are here"
            }
         ]
      }
   ]
}

def traverseDict(d, depth):
    if depth == 0:
        return []
    else:
        data = []
        for i in d.keys():
            if isinstance(d[i], dict):
                data += traverseDict(d[i], depth -1)
            elif isinstance(d[i], list):
                for li in d[i]:
                    if isinstance(li, dict):
                        data += traverseDict(li, depth-1)
                    else:
                        data.append((f'List Item', li))
            else:
                data.append((i, d[i]))
        return data


pp(traverseDict(test, 10))

#### OUTPUT ####
"""
[('Name', 'John'),
 ('List Item', 87),
 ('List Item', 90),
 ('List Item', 95),
 ('List Item', 47),
 ('List Item', 98),
 ('special_Key', 'special_value'),
 ('List Item', 11),
 ('List Item', 22),
 ('List Item', 33),
 ('List Item', 44),
 ('hidden_key', 'You are here')]
 """
