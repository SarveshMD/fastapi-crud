query = '''
{
  Tasks: [
    '{{repeat(10)}}',
    {
    id: '{{objectId()}}',
    title: '{{lorem(1,"sentences")}}',
    description: '{{lorem(1,"sentences")}}',
    is_completed: '{{bool()}}',
    priority: '{{random("high", "medium", "low")}}',
    created_at: '{{date()}}'
    }
  ]
}


'''

toy_data = {
	"Tasks": [
		{
			"id": "6a89a82c197993b55a2322fc",
			"title": "Adipisicing occaecat excepteur incididunt elit.",
			"description": None,
			"is_completed": True,
			"priority": "low",
			"created_at": "Thu Apr 01 1982 15:07:58 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c4e6f421ee2965fd7",
			"title": "In nulla excepteur qui ea proident fugiat in est est nisi.",
			"description": None,
			"is_completed": False,
			"priority": "high",
			"created_at": "Sun Jul 06 2003 23:23:50 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c0c768467be780ede",
			"title": "Nostrud minim adipisicing ad commodo laborum amet labore laboris et ullamco ea ipsum sit dolor.",
			"description": None,
			"is_completed": True,
			"priority": "medium",
			"created_at": "Tue Oct 14 2003 16:23:40 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c3f26116d77fe701b",
			"title": "Ad ut sunt officia commodo eiusmod.",
			"description": "Ad non nulla proident pariatur ullamco ad proident.",
			"is_completed": True,
			"priority": "high",
			"created_at": "Fri Jan 14 1977 02:08:44 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c5ce5474ac8c5aefd",
			"title": "In cupidatat occaecat consequat laborum mollit cupidatat magna.",
			"description": "Duis cillum qui eu quis ea.",
			"is_completed": False,
			"priority": "low",
			"created_at": "Mon Nov 02 2020 08:28:04 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c853e606cf23cfd4e",
			"title": "Cillum ut sit in aliqua pariatur sit dolore id et occaecat ullamco laborum et.",
			"description": "Culpa excepteur dolor sunt fugiat officia magna officia.",
			"is_completed": False,
			"priority": "high",
			"created_at": "Sun Mar 09 2003 04:32:03 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82cd61b255f58ec0463",
			"title": "Ullamco do proident dolor occaecat quis id.",
			"description": "Mollit magna ullamco laborum consequat labore dolor enim reprehenderit aliquip occaecat in.",
			"is_completed": True,
			"priority": "medium",
			"created_at": "Mon Oct 13 1997 19:02:43 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c4b6d3f0697d10bca",
			"title": "Adipisicing pariatur anim laboris dolor.",
			"description": None,
			"is_completed": False,
			"priority": "high",
			"created_at": "Sat Nov 02 2024 14:23:42 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c34e600aa8a544a33",
			"title": "Anim Lorem incididunt ea ut anim ullamco nulla mollit dolore magna cupidatat.",
			"description": "Consequat incididunt proident nostrud ex eu irure sunt ipsum aliquip.",
			"is_completed": False,
			"priority": "medium",
			"created_at": "Tue Jun 10 2003 06:08:01 GMT+0530 (India Standard Time)"
		},
		{
			"id": "6a89a82c77978a4d63dcdf40",
			"title": "Velit enim occaecat mollit sunt ipsum culpa Lorem aliquip ea enim cillum.",
			"description": None,
			"is_completed": True,
			"priority": "high",
			"created_at": "Tue Aug 21 1990 03:44:53 GMT+0530 (India Standard Time)"
		}
	]
}
