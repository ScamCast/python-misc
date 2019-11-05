from pprint import pprint as pp

########################### TEST 2 ###########################

A = {
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
        if isinstance(d, dict):
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
        elif isinstance(d, list):
            for li in d:
                if isinstance(li, dict):
                    data += traverseDict(li, depth-1)
                else:
                    data.append((f'List Item', li))
        return data

pp(traverseDict(A, 20))
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


########################### TEST 2 ###########################

B = [
  {
    "_id": "5dc1a709da54e5ccda8c9015",
    "index": 0,
    "guid": "fa18c296-1159-447a-806f-f4feb67f6997",
    "isActive": True,
    "balance": "$2,609.32",
    "picture": "http://placehold.it/32x32",
    "age": 30,
    "eyeColor": "brown",
    "name": "Bowen Gregory",
    "gender": "male",
    "company": "GENMOM",
    "email": "bowengregory@genmom.com",
    "phone": "+1 (972) 412-3146",
    "address": "115 Miami Court, Galesville, New Hampshire, 1450",
    "about": "Laborum et laborum esse duis laboris mollit. Sint ut labore duis non pariatur adipisicing sit. Ipsum qui cupidatat ea fugiat in sunt ut irure elit non laboris.\r\n",
    "registered": "2015-03-30T05:10:22 +06:00",
    "latitude": -57.579483,
    "longitude": 14.921173,
    "tags": [
      "occaecat",
      "nisi",
      "fugiat",
      "sit",
      "aliquip",
      "ad",
      "incididunt"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Vazquez Luna"
      },
      {
        "id": 1,
        "name": "Madelyn Le"
      },
      {
        "id": 2,
        "name": "Ginger Vega"
      }
    ],
    "greeting": "Hello, Bowen Gregory! You have 4 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": "5dc1a709e81b9d9792b77941",
    "index": 1,
    "guid": "47438313-6ef3-4de6-9325-c1694b1e4627",
    "isActive": True,
    "balance": "$3,119.60",
    "picture": "http://placehold.it/32x32",
    "age": 26,
    "eyeColor": "blue",
    "name": "Audra Irwin",
    "gender": "female",
    "company": "FLYBOYZ",
    "email": "audrairwin@flyboyz.com",
    "phone": "+1 (898) 467-2703",
    "address": "844 Sharon Street, Kapowsin, Georgia, 7954",
    "about": "Amet magna pariatur eu cupidatat laboris est voluptate dolor aliqua irure enim. Commodo veniam qui officia quis exercitation veniam ut veniam nisi non est deserunt cillum. Veniam anim ut et anim dolore amet aute irure eu duis cillum. Aliquip ex est in enim anim do incididunt culpa Lorem excepteur.\r\n",
    "registered": "2015-11-22T10:29:06 +07:00",
    "latitude": -53.249513,
    "longitude": 21.141102,
    "tags": [
      "do",
      "eiusmod",
      "laborum",
      "velit",
      "cillum",
      "anim",
      "excepteur"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Young Ellis"
      },
      {
        "id": 1,
        "name": "Perkins Cantrell"
      },
      {
        "id": 2,
        "name": "Sweeney Hahn"
      }
    ],
    "greeting": "Hello, Audra Irwin! You have 6 unread messages.",
    "favoriteFruit": "apple"
  },
  {
    "_id": "5dc1a7096940e2b49092baa0",
    "index": 2,
    "guid": "893972c8-c546-4771-82ca-2f7b73941c57",
    "isActive": True,
    "balance": "$1,019.82",
    "picture": "http://placehold.it/32x32",
    "age": 33,
    "eyeColor": "brown",
    "name": "Tommie Rodgers",
    "gender": "female",
    "company": "SLOGANAUT",
    "email": "tommierodgers@sloganaut.com",
    "phone": "+1 (894) 463-2012",
    "address": "653 Oliver Street, Tecolotito, Utah, 2804",
    "about": "Irure mollit exercitation mollit nulla. Eu aute nisi quis in aute non veniam. Consequat eiusmod sint aute irure do ullamco. Esse culpa duis elit veniam enim veniam aliquip deserunt et fugiat qui. Nostrud minim sunt velit velit laboris fugiat adipisicing. In reprehenderit duis quis amet excepteur laboris aute voluptate amet enim est occaecat minim.\r\n",
    "registered": "2016-02-24T05:14:43 +07:00",
    "latitude": -52.415589,
    "longitude": 41.968213,
    "tags": [
      "laboris",
      "non",
      "labore",
      "est",
      "ex",
      "consectetur",
      "nostrud"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Danielle Bradshaw"
      },
      {
        "id": 1,
        "name": "Dolores Parker"
      },
      {
        "id": 2,
        "name": "Peggy Thornton"
      }
    ],
    "greeting": "Hello, Tommie Rodgers! You have 6 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": "5dc1a709c55ab828338b8982",
    "index": 3,
    "guid": "3559810e-e74f-43cd-99f3-c6c3f2eedebe",
    "isActive": True,
    "balance": "$1,332.99",
    "picture": "http://placehold.it/32x32",
    "age": 27,
    "eyeColor": "blue",
    "name": "Adele Cleveland",
    "gender": "female",
    "company": "COMVERGES",
    "email": "adelecleveland@comverges.com",
    "phone": "+1 (984) 400-2091",
    "address": "231 Norman Avenue, Corriganville, Virgin Islands, 1288",
    "about": "Magna dolore labore elit irure adipisicing. Anim culpa dolor aliqua ullamco id ea adipisicing Lorem consequat tempor consequat et irure. Est incididunt ex dolor occaecat pariatur veniam esse consectetur dolor occaecat magna sint ea velit. Consectetur anim ullamco mollit ut. Elit elit labore mollit veniam dolor reprehenderit aute in incididunt officia elit. Do et deserunt nulla et aute incididunt enim minim enim. Dolore ullamco veniam cillum mollit consectetur dolor laboris.\r\n",
    "registered": "2018-11-09T03:39:17 +07:00",
    "latitude": 73.176088,
    "longitude": 120.638843,
    "tags": [
      "aliquip",
      "in",
      "ad",
      "incididunt",
      "aute",
      "commodo",
      "aliquip"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Conner Curry"
      },
      {
        "id": 1,
        "name": "Brandie Estes"
      },
      {
        "id": 2,
        "name": "Lang Shaw"
      }
    ],
    "greeting": "Hello, Adele Cleveland! You have 7 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": "5dc1a7091fb5a7b14fcbd640",
    "index": 4,
    "guid": "c73228c2-de3f-4d3b-9b86-d3ac7f11d080",
    "isActive": True,
    "balance": "$1,301.44",
    "picture": "http://placehold.it/32x32",
    "age": 38,
    "eyeColor": "green",
    "name": "Dalton Blake",
    "gender": "male",
    "company": "ISOSTREAM",
    "email": "daltonblake@isostream.com",
    "phone": "+1 (959) 533-2065",
    "address": "242 Pilling Street, Gordon, Connecticut, 321",
    "about": "Magna minim consectetur adipisicing nostrud nisi elit magna. Irure duis nisi deserunt nulla cillum ullamco deserunt amet Lorem mollit. Occaecat pariatur ipsum in officia duis tempor cillum officia fugiat nostrud. Cupidatat excepteur ullamco laboris exercitation voluptate sint anim sint tempor Lorem. Laboris ullamco cupidatat Lorem culpa. Eu Lorem incididunt cillum nisi. Qui aliqua aliquip in enim voluptate officia.\r\n",
    "registered": "2019-05-23T07:44:11 +06:00",
    "latitude": 0.249086,
    "longitude": -39.520767,
    "tags": [
      "minim",
      "minim",
      "tempor",
      "culpa",
      "laboris",
      "consequat",
      "quis"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Terry Hodge"
      },
      {
        "id": 1,
        "name": "Marshall Pierce"
      },
      {
        "id": 2,
        "name": "Karin Harrison"
      }
    ],
    "greeting": "Hello, Dalton Blake! You have 1 unread messages.",
    "favoriteFruit": "apple"
  }
]




pp(traverseDict(B, 20))

"""
[('_id', '5dc1a709da54e5ccda8c9015'),
 ('index', 0),
 ('guid', 'fa18c296-1159-447a-806f-f4feb67f6997'),
 ('isActive', True),
 ('balance', '$2,609.32'),
 ('picture', 'http://placehold.it/32x32'),
 ('age', 30),
 ('eyeColor', 'brown'),
 ('name', 'Bowen Gregory'),
 ('gender', 'male'),
 ('company', 'GENMOM'),
 ('email', 'bowengregory@genmom.com'),
 ('phone', '+1 (972) 412-3146'),
 ('address', '115 Miami Court, Galesville, New Hampshire, 1450'),
 ('about',
  'Laborum et laborum esse duis laboris mollit. Sint ut labore duis non '
  'pariatur adipisicing sit. Ipsum qui cupidatat ea fugiat in sunt ut irure '
  'elit non laboris.\r\n'),
 ('registered', '2015-03-30T05:10:22 +06:00'),
 ('latitude', -57.579483),
 ('longitude', 14.921173),
 ('List Item', 'occaecat'),
 ('List Item', 'nisi'),
 ('List Item', 'fugiat'),
 ('List Item', 'sit'),
 ('List Item', 'aliquip'),
 ('List Item', 'ad'),
 ('List Item', 'incididunt'),
 ('id', 0),
 ('name', 'Vazquez Luna'),
 ('id', 1),
 ('name', 'Madelyn Le'),
 ('id', 2),
 ('name', 'Ginger Vega'),
 ('greeting', 'Hello, Bowen Gregory! You have 4 unread messages.'),
 ('favoriteFruit', 'strawberry'),
 ('_id', '5dc1a709e81b9d9792b77941'),
 ('index', 1),
 ('guid', '47438313-6ef3-4de6-9325-c1694b1e4627'),
 ('isActive', True),
 ('balance', '$3,119.60'),
 ('picture', 'http://placehold.it/32x32'),
 ('age', 26),
 ('eyeColor', 'blue'),
 ('name', 'Audra Irwin'),
 ('gender', 'female'),
 ('company', 'FLYBOYZ'),
 ('email', 'audrairwin@flyboyz.com'),
 ('phone', '+1 (898) 467-2703'),
 ('address', '844 Sharon Street, Kapowsin, Georgia, 7954'),
 ('about',
  'Amet magna pariatur eu cupidatat laboris est voluptate dolor aliqua irure '
  'enim. Commodo veniam qui officia quis exercitation veniam ut veniam nisi '
  'non est deserunt cillum. Veniam anim ut et anim dolore amet aute irure eu '
  'duis cillum. Aliquip ex est in enim anim do incididunt culpa Lorem '
  'excepteur.\r\n'),
 ('registered', '2015-11-22T10:29:06 +07:00'),
 ('latitude', -53.249513),
 ('longitude', 21.141102),
 ('List Item', 'do'),
 ('List Item', 'eiusmod'),
 ('List Item', 'laborum'),
 ('List Item', 'velit'),
 ('List Item', 'cillum'),
 ('List Item', 'anim'),
 ('List Item', 'excepteur'),
 ('id', 0),
 ('name', 'Young Ellis'),
 ('id', 1),
 ('name', 'Perkins Cantrell'),
 ('id', 2),
 ('name', 'Sweeney Hahn'),
 ('greeting', 'Hello, Audra Irwin! You have 6 unread messages.'),
 ('favoriteFruit', 'apple'),
 ('_id', '5dc1a7096940e2b49092baa0'),
 ('index', 2),
 ('guid', '893972c8-c546-4771-82ca-2f7b73941c57'),
 ('isActive', True),
 ('balance', '$1,019.82'),
 ('picture', 'http://placehold.it/32x32'),
 ('age', 33),
 ('eyeColor', 'brown'),
 ('name', 'Tommie Rodgers'),
 ('gender', 'female'),
 ('company', 'SLOGANAUT'),
 ('email', 'tommierodgers@sloganaut.com'),
 ('phone', '+1 (894) 463-2012'),
 ('address', '653 Oliver Street, Tecolotito, Utah, 2804'),
 ('about',
  'Irure mollit exercitation mollit nulla. Eu aute nisi quis in aute non '
  'veniam. Consequat eiusmod sint aute irure do ullamco. Esse culpa duis elit '
  'veniam enim veniam aliquip deserunt et fugiat qui. Nostrud minim sunt velit '
  'velit laboris fugiat adipisicing. In reprehenderit duis quis amet excepteur '
  'laboris aute voluptate amet enim est occaecat minim.\r\n'),
 ('registered', '2016-02-24T05:14:43 +07:00'),
 ('latitude', -52.415589),
 ('longitude', 41.968213),
 ('List Item', 'laboris'),
 ('List Item', 'non'),
 ('List Item', 'labore'),
 ('List Item', 'est'),
 ('List Item', 'ex'),
 ('List Item', 'consectetur'),
 ('List Item', 'nostrud'),
 ('id', 0),
 ('name', 'Danielle Bradshaw'),
 ('id', 1),
 ('name', 'Dolores Parker'),
 ('id', 2),
 ('name', 'Peggy Thornton'),
 ('greeting', 'Hello, Tommie Rodgers! You have 6 unread messages.'),
 ('favoriteFruit', 'banana'),
 ('_id', '5dc1a709c55ab828338b8982'),
 ('index', 3),
 ('guid', '3559810e-e74f-43cd-99f3-c6c3f2eedebe'),
 ('isActive', True),
 ('balance', '$1,332.99'),
 ('picture', 'http://placehold.it/32x32'),
 ('age', 27),
 ('eyeColor', 'blue'),
 ('name', 'Adele Cleveland'),
 ('gender', 'female'),
 ('company', 'COMVERGES'),
 ('email', 'adelecleveland@comverges.com'),
 ('phone', '+1 (984) 400-2091'),
 ('address', '231 Norman Avenue, Corriganville, Virgin Islands, 1288'),
 ('about',
  'Magna dolore labore elit irure adipisicing. Anim culpa dolor aliqua ullamco '
  'id ea adipisicing Lorem consequat tempor consequat et irure. Est incididunt '
  'ex dolor occaecat pariatur veniam esse consectetur dolor occaecat magna '
  'sint ea velit. Consectetur anim ullamco mollit ut. Elit elit labore mollit '
  'veniam dolor reprehenderit aute in incididunt officia elit. Do et deserunt '
  'nulla et aute incididunt enim minim enim. Dolore ullamco veniam cillum '
  'mollit consectetur dolor laboris.\r\n'),
 ('registered', '2018-11-09T03:39:17 +07:00'),
 ('latitude', 73.176088),
 ('longitude', 120.638843),
 ('List Item', 'aliquip'),
 ('List Item', 'in'),
 ('List Item', 'ad'),
 ('List Item', 'incididunt'),
 ('List Item', 'aute'),
 ('List Item', 'commodo'),
 ('List Item', 'aliquip'),
 ('id', 0),
 ('name', 'Conner Curry'),
 ('id', 1),
 ('name', 'Brandie Estes'),
 ('id', 2),
 ('name', 'Lang Shaw'),
 ('greeting', 'Hello, Adele Cleveland! You have 7 unread messages.'),
 ('favoriteFruit', 'banana'),
 ('_id', '5dc1a7091fb5a7b14fcbd640'),
 ('index', 4),
 ('guid', 'c73228c2-de3f-4d3b-9b86-d3ac7f11d080'),
 ('isActive', True),
 ('balance', '$1,301.44'),
 ('picture', 'http://placehold.it/32x32'),
 ('age', 38),
 ('eyeColor', 'green'),
 ('name', 'Dalton Blake'),
 ('gender', 'male'),
 ('company', 'ISOSTREAM'),
 ('email', 'daltonblake@isostream.com'),
 ('phone', '+1 (959) 533-2065'),
 ('address', '242 Pilling Street, Gordon, Connecticut, 321'),
 ('about',
  'Magna minim consectetur adipisicing nostrud nisi elit magna. Irure duis '
  'nisi deserunt nulla cillum ullamco deserunt amet Lorem mollit. Occaecat '
  'pariatur ipsum in officia duis tempor cillum officia fugiat nostrud. '
  'Cupidatat excepteur ullamco laboris exercitation voluptate sint anim sint '
  'tempor Lorem. Laboris ullamco cupidatat Lorem culpa. Eu Lorem incididunt '
  'cillum nisi. Qui aliqua aliquip in enim voluptate officia.\r\n'),
 ('registered', '2019-05-23T07:44:11 +06:00'),
 ('latitude', 0.249086),
 ('longitude', -39.520767),
 ('List Item', 'minim'),
 ('List Item', 'minim'),
 ('List Item', 'tempor'),
 ('List Item', 'culpa'),
 ('List Item', 'laboris'),
 ('List Item', 'consequat'),
 ('List Item', 'quis'),
 ('id', 0),
 ('name', 'Terry Hodge'),
 ('id', 1),
 ('name', 'Marshall Pierce'),
 ('id', 2),
 ('name', 'Karin Harrison'),
 ('greeting', 'Hello, Dalton Blake! You have 1 unread messages.'),
 ('favoriteFruit', 'apple')]
"""
