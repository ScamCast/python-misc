from pprint import pprint as pp


def traverseDict(d, depth, keys_=[]):

    if depth == 0:
        return []
    else:
        data = []
        if isinstance(d, dict):
            for i in d.keys():
                if isinstance(d[i], dict):
                    keys = keys_ + [i]
                    data += traverseDict(d[i], depth -1, keys)
                elif isinstance(d[i], list):
                    keys = keys_ + [i]
                    for li in d[i]:
                        if isinstance(li, dict):
                            data += traverseDict(li, depth-1, keys)
                        else:
                            data.append([[list]+keys, li])
                else:
                    keys = keys_ + [i]
                    data.append((keys, d[i]))
        elif isinstance(d, list):
            root_list = 0
            for li in d:
                root_list+=1
                if isinstance(li, dict):
                    data += traverseDict(li, depth-1, [root_list])
                else:
                    data.append((f'List Item---------->', li))
        return data


########################### TEST 1 ###########################
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
            [9,99,999,999,9999],
            33,
            {'dict_inside_list': {'deep_dict': [555, 666, 777, 888], 'deep': 'hey', 'deeeep': {'even_deeper': ['l1', 'l2', 'l3']}}},
            {
               "hidden_key": "You are here"
            }
         ]
      }
   ]
}

print('\n\n'+'#'*20+' TEST_1 '+'#'*20)
pp(traverseDict(A, 40), width=100 )


# OUTPUT #
"""
[(['Name'], 'John'),
 ("List Item ['Scores']", 87),
 ("List Item ['Scores']", 90),
 ("List Item ['Scores']", 95),
 ("List Item ['Scores']", 47),
 ("List Item ['Scores']", 98),
 (['Scores', 'special_Key'], 'special_value'),
 ("List Item ['Scores', 'secret_numbers']", 11),
 ("List Item ['Scores', 'secret_numbers']", [9, 99, 999, 999, 9999]),
 ("List Item ['Scores', 'secret_numbers']", 33),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deep_dict']", 555),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deep_dict']", 666),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deep_dict']", 777),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deep_dict']", 888),
 (['Scores', 'secret_numbers', 'dict_inside_list', 'deep'], 'hey'),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deeeep', 'even_deeper']", 'l1'),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deeeep', 'even_deeper']", 'l2'),
 ("List Item ['Scores', 'secret_numbers', 'dict_inside_list', 'deeeep', 'even_deeper']", 'l3'),
 (['Scores', 'secret_numbers', 'hidden_key'], 'You are here')]
 """
# END OUTPUT #



########################### TEST 2 ###########################
B = [
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0002",
		"type": "donut",
		"name": "Raised",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0003",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}
]

print('\n\n'+'#'*20+' TEST_2 '+'#'*20)
pp(traverseDict(B, 20), width=100)

# OUTPUT #
"""
[([1, 'id'], '0001'),
 ([1, 'type'], 'donut'),
 ([1, 'name'], 'Cake'),
 ([1, 'ppu'], 0.55),
 ([1, 'batters', 'batter', 'id'], '1001'),
 ([1, 'batters', 'batter', 'type'], 'Regular'),
 ([1, 'batters', 'batter', 'id'], '1002'),
 ([1, 'batters', 'batter', 'type'], 'Chocolate'),
 ([1, 'batters', 'batter', 'id'], '1003'),
 ([1, 'batters', 'batter', 'type'], 'Blueberry'),
 ([1, 'batters', 'batter', 'id'], '1004'),
 ([1, 'batters', 'batter', 'type'], "Devil's Food"),
 ([1, 'topping', 'id'], '5001'),
 ([1, 'topping', 'type'], 'None'),
 ([1, 'topping', 'id'], '5002'),
 ([1, 'topping', 'type'], 'Glazed'),
 ([1, 'topping', 'id'], '5005'),
 ([1, 'topping', 'type'], 'Sugar'),
 ([1, 'topping', 'id'], '5007'),
 ([1, 'topping', 'type'], 'Powdered Sugar'),
 ([1, 'topping', 'id'], '5006'),
 ([1, 'topping', 'type'], 'Chocolate with Sprinkles'),
 ([1, 'topping', 'id'], '5003'),
 ([1, 'topping', 'type'], 'Chocolate'),
 ([1, 'topping', 'id'], '5004'),
 ([1, 'topping', 'type'], 'Maple'),
 ([2, 'id'], '0002'),
 ([2, 'type'], 'donut'),
 ([2, 'name'], 'Raised'),
 ([2, 'ppu'], 0.55),
 ([2, 'batters', 'batter', 'id'], '1001'),
 ([2, 'batters', 'batter', 'type'], 'Regular'),
 ([2, 'topping', 'id'], '5001'),
 ([2, 'topping', 'type'], 'None'),
 ([2, 'topping', 'id'], '5002'),
 ([2, 'topping', 'type'], 'Glazed'),
 ([2, 'topping', 'id'], '5005'),
 ([2, 'topping', 'type'], 'Sugar'),
 ([2, 'topping', 'id'], '5003'),
 ([2, 'topping', 'type'], 'Chocolate'),
 ([2, 'topping', 'id'], '5004'),
 ([2, 'topping', 'type'], 'Maple'),
 ([3, 'id'], '0003'),
 ([3, 'type'], 'donut'),
 ([3, 'name'], 'Old Fashioned'),
 ([3, 'ppu'], 0.55),
 ([3, 'batters', 'batter', 'id'], '1001'),
 ([3, 'batters', 'batter', 'type'], 'Regular'),
 ([3, 'batters', 'batter', 'id'], '1002'),
 ([3, 'batters', 'batter', 'type'], 'Chocolate'),
 ([3, 'topping', 'id'], '5001'),
 ([3, 'topping', 'type'], 'None'),
 ([3, 'topping', 'id'], '5002'),
 ([3, 'topping', 'type'], 'Glazed'),
 ([3, 'topping', 'id'], '5003'),
 ([3, 'topping', 'type'], 'Chocolate'),
 ([3, 'topping', 'id'], '5004'),
 ([3, 'topping', 'type'], 'Maple')]
"""
# END OUTPUT #



########################### TEST 2 ###########################
C = [
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

print('\n\n'+'#'*20+' TEST_3 '+'#'*20)
pp(traverseDict(C, 20), width=100)

# OUTPUT #
"""
[([1, '_id'], '5dc1a709da54e5ccda8c9015'),
 ([1, 'index'], 0),
 ([1, 'guid'], 'fa18c296-1159-447a-806f-f4feb67f6997'),
 ([1, 'isActive'], True),
 ([1, 'balance'], '$2,609.32'),
 ([1, 'picture'], 'http://placehold.it/32x32'),
 ([1, 'age'], 30),
 ([1, 'eyeColor'], 'brown'),
 ([1, 'name'], 'Bowen Gregory'),
 ([1, 'gender'], 'male'),
 ([1, 'company'], 'GENMOM'),
 ([1, 'email'], 'bowengregory@genmom.com'),
 ([1, 'phone'], '+1 (972) 412-3146'),
 ([1, 'address'], '115 Miami Court, Galesville, New Hampshire, 1450'),
 ([1, 'about'],
  'Laborum et laborum esse duis laboris mollit. Sint ut labore duis non '
  'pariatur adipisicing sit. Ipsum qui cupidatat ea fugiat in sunt ut irure '
  'elit non laboris.\r\n'),
 ([1, 'registered'], '2015-03-30T05:10:22 +06:00'),
 ([1, 'latitude'], -57.579483),
 ([1, 'longitude'], 14.921173),
 ("List Item [1, 'tags']", 'occaecat'),
 ("List Item [1, 'tags']", 'nisi'),
 ("List Item [1, 'tags']", 'fugiat'),
 ("List Item [1, 'tags']", 'sit'),
 ("List Item [1, 'tags']", 'aliquip'),
 ("List Item [1, 'tags']", 'ad'),
 ("List Item [1, 'tags']", 'incididunt'),
 ([1, 'friends', 'id'], 0),
 ([1, 'friends', 'name'], 'Vazquez Luna'),
 ([1, 'friends', 'id'], 1),
 ([1, 'friends', 'name'], 'Madelyn Le'),
 ([1, 'friends', 'id'], 2),
 ([1, 'friends', 'name'], 'Ginger Vega'),
 ([1, 'greeting'], 'Hello, Bowen Gregory! You have 4 unread messages.'),
 ([1, 'favoriteFruit'], 'strawberry'),
 ([2, '_id'], '5dc1a709e81b9d9792b77941'),
 ([2, 'index'], 1),
 ([2, 'guid'], '47438313-6ef3-4de6-9325-c1694b1e4627'),
 ([2, 'isActive'], True),
 ([2, 'balance'], '$3,119.60'),
 ([2, 'picture'], 'http://placehold.it/32x32'),
 ([2, 'age'], 26),
 ([2, 'eyeColor'], 'blue'),
 ([2, 'name'], 'Audra Irwin'),
 ([2, 'gender'], 'female'),
 ([2, 'company'], 'FLYBOYZ'),
 ([2, 'email'], 'audrairwin@flyboyz.com'),
 ([2, 'phone'], '+1 (898) 467-2703'),
 ([2, 'address'], '844 Sharon Street, Kapowsin, Georgia, 7954'),
 ([2, 'about'],
  'Amet magna pariatur eu cupidatat laboris est voluptate dolor aliqua irure '
  'enim. Commodo veniam qui officia quis exercitation veniam ut veniam nisi '
  'non est deserunt cillum. Veniam anim ut et anim dolore amet aute irure eu '
  'duis cillum. Aliquip ex est in enim anim do incididunt culpa Lorem '
  'excepteur.\r\n'),
 ([2, 'registered'], '2015-11-22T10:29:06 +07:00'),
 ([2, 'latitude'], -53.249513),
 ([2, 'longitude'], 21.141102),
 ("List Item [2, 'tags']", 'do'),
 ("List Item [2, 'tags']", 'eiusmod'),
 ("List Item [2, 'tags']", 'laborum'),
 ("List Item [2, 'tags']", 'velit'),
 ("List Item [2, 'tags']", 'cillum'),
 ("List Item [2, 'tags']", 'anim'),
 ("List Item [2, 'tags']", 'excepteur'),
 ([2, 'friends', 'id'], 0),
 ([2, 'friends', 'name'], 'Young Ellis'),
 ([2, 'friends', 'id'], 1),
 ([2, 'friends', 'name'], 'Perkins Cantrell'),
 ([2, 'friends', 'id'], 2),
 ([2, 'friends', 'name'], 'Sweeney Hahn'),
 ([2, 'greeting'], 'Hello, Audra Irwin! You have 6 unread messages.'),
 ([2, 'favoriteFruit'], 'apple'),
 ([3, '_id'], '5dc1a7096940e2b49092baa0'),
 ([3, 'index'], 2),
 ([3, 'guid'], '893972c8-c546-4771-82ca-2f7b73941c57'),
 ([3, 'isActive'], True),
 ([3, 'balance'], '$1,019.82'),
 ([3, 'picture'], 'http://placehold.it/32x32'),
 ([3, 'age'], 33),
 ([3, 'eyeColor'], 'brown'),
 ([3, 'name'], 'Tommie Rodgers'),
 ([3, 'gender'], 'female'),
 ([3, 'company'], 'SLOGANAUT'),
 ([3, 'email'], 'tommierodgers@sloganaut.com'),
 ([3, 'phone'], '+1 (894) 463-2012'),
 ([3, 'address'], '653 Oliver Street, Tecolotito, Utah, 2804'),
 ([3, 'about'],
  'Irure mollit exercitation mollit nulla. Eu aute nisi quis in aute non '
  'veniam. Consequat eiusmod sint aute irure do ullamco. Esse culpa duis elit '
  'veniam enim veniam aliquip deserunt et fugiat qui. Nostrud minim sunt velit '
  'velit laboris fugiat adipisicing. In reprehenderit duis quis amet excepteur '
  'laboris aute voluptate amet enim est occaecat minim.\r\n'),
 ([3, 'registered'], '2016-02-24T05:14:43 +07:00'),
 ([3, 'latitude'], -52.415589),
 ([3, 'longitude'], 41.968213),
 ("List Item [3, 'tags']", 'laboris'),
 ("List Item [3, 'tags']", 'non'),
 ("List Item [3, 'tags']", 'labore'),
 ("List Item [3, 'tags']", 'est'),
 ("List Item [3, 'tags']", 'ex'),
 ("List Item [3, 'tags']", 'consectetur'),
 ("List Item [3, 'tags']", 'nostrud'),
 ([3, 'friends', 'id'], 0),
 ([3, 'friends', 'name'], 'Danielle Bradshaw'),
 ([3, 'friends', 'id'], 1),
 ([3, 'friends', 'name'], 'Dolores Parker'),
 ([3, 'friends', 'id'], 2),
 ([3, 'friends', 'name'], 'Peggy Thornton'),
 ([3, 'greeting'], 'Hello, Tommie Rodgers! You have 6 unread messages.'),
 ([3, 'favoriteFruit'], 'banana'),
 ([4, '_id'], '5dc1a709c55ab828338b8982'),
 ([4, 'index'], 3),
 ([4, 'guid'], '3559810e-e74f-43cd-99f3-c6c3f2eedebe'),
 ([4, 'isActive'], True),
 ([4, 'balance'], '$1,332.99'),
 ([4, 'picture'], 'http://placehold.it/32x32'),
 ([4, 'age'], 27),
 ([4, 'eyeColor'], 'blue'),
 ([4, 'name'], 'Adele Cleveland'),
 ([4, 'gender'], 'female'),
 ([4, 'company'], 'COMVERGES'),
 ([4, 'email'], 'adelecleveland@comverges.com'),
 ([4, 'phone'], '+1 (984) 400-2091'),
 ([4, 'address'], '231 Norman Avenue, Corriganville, Virgin Islands, 1288'),
 ([4, 'about'],
  'Magna dolore labore elit irure adipisicing. Anim culpa dolor aliqua ullamco '
  'id ea adipisicing Lorem consequat tempor consequat et irure. Est incididunt '
  'ex dolor occaecat pariatur veniam esse consectetur dolor occaecat magna '
  'sint ea velit. Consectetur anim ullamco mollit ut. Elit elit labore mollit '
  'veniam dolor reprehenderit aute in incididunt officia elit. Do et deserunt '
  'nulla et aute incididunt enim minim enim. Dolore ullamco veniam cillum '
  'mollit consectetur dolor laboris.\r\n'),
 ([4, 'registered'], '2018-11-09T03:39:17 +07:00'),
 ([4, 'latitude'], 73.176088),
 ([4, 'longitude'], 120.638843),
 ("List Item [4, 'tags']", 'aliquip'),
 ("List Item [4, 'tags']", 'in'),
 ("List Item [4, 'tags']", 'ad'),
 ("List Item [4, 'tags']", 'incididunt'),
 ("List Item [4, 'tags']", 'aute'),
 ("List Item [4, 'tags']", 'commodo'),
 ("List Item [4, 'tags']", 'aliquip'),
 ([4, 'friends', 'id'], 0),
 ([4, 'friends', 'name'], 'Conner Curry'),
 ([4, 'friends', 'id'], 1),
 ([4, 'friends', 'name'], 'Brandie Estes'),
 ([4, 'friends', 'id'], 2),
 ([4, 'friends', 'name'], 'Lang Shaw'),
 ([4, 'greeting'], 'Hello, Adele Cleveland! You have 7 unread messages.'),
 ([4, 'favoriteFruit'], 'banana'),
 ([5, '_id'], '5dc1a7091fb5a7b14fcbd640'),
 ([5, 'index'], 4),
 ([5, 'guid'], 'c73228c2-de3f-4d3b-9b86-d3ac7f11d080'),
 ([5, 'isActive'], True),
 ([5, 'balance'], '$1,301.44'),
 ([5, 'picture'], 'http://placehold.it/32x32'),
 ([5, 'age'], 38),
 ([5, 'eyeColor'], 'green'),
 ([5, 'name'], 'Dalton Blake'),
 ([5, 'gender'], 'male'),
 ([5, 'company'], 'ISOSTREAM'),
 ([5, 'email'], 'daltonblake@isostream.com'),
 ([5, 'phone'], '+1 (959) 533-2065'),
 ([5, 'address'], '242 Pilling Street, Gordon, Connecticut, 321'),
 ([5, 'about'],
  'Magna minim consectetur adipisicing nostrud nisi elit magna. Irure duis '
  'nisi deserunt nulla cillum ullamco deserunt amet Lorem mollit. Occaecat '
  'pariatur ipsum in officia duis tempor cillum officia fugiat nostrud. '
  'Cupidatat excepteur ullamco laboris exercitation voluptate sint anim sint '
  'tempor Lorem. Laboris ullamco cupidatat Lorem culpa. Eu Lorem incididunt '
  'cillum nisi. Qui aliqua aliquip in enim voluptate officia.\r\n'),
 ([5, 'registered'], '2019-05-23T07:44:11 +06:00'),
 ([5, 'latitude'], 0.249086),
 ([5, 'longitude'], -39.520767),
 ("List Item [5, 'tags']", 'minim'),
 ("List Item [5, 'tags']", 'minim'),
 ("List Item [5, 'tags']", 'tempor'),
 ("List Item [5, 'tags']", 'culpa'),
 ("List Item [5, 'tags']", 'laboris'),
 ("List Item [5, 'tags']", 'consequat'),
 ("List Item [5, 'tags']", 'quis'),
 ([5, 'friends', 'id'], 0),
 ([5, 'friends', 'name'], 'Terry Hodge'),
 ([5, 'friends', 'id'], 1),
 ([5, 'friends', 'name'], 'Marshall Pierce'),
 ([5, 'friends', 'id'], 2),
 ([5, 'friends', 'name'], 'Karin Harrison'),
 ([5, 'greeting'], 'Hello, Dalton Blake! You have 1 unread messages.'),
 ([5, 'favoriteFruit'], 'apple')]
"""
# END OUTPUT #
