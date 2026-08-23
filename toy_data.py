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
            "id": "be14de07-8fb5-42f6-873a-b7e406c7bf3d",
            "title": "Adipisicing occaecat excepteur incididunt elit.",
            "description": None,
            "is_completed": True,
            "priority": "low",
            "created_at": "1982-04-01T09:37:58+00:00"
        },
        {
            "id": "15d7ee97-b355-499a-827f-2eca89f312be",
            "title": "In nulla excepteur qui ea proident fugiat in est est nisi.",
            "description": None,
            "is_completed": False,
            "priority": "high",
            "created_at": "2003-07-06T17:53:50+00:00"
        },
        {
            "id": "5804e3ae-adc6-4ebf-a966-d76b355f6fa1",
            "title": "Nostrud minim adipisicing ad commodo laborum amet labore laboris et ullamco ea ipsum sit dolor.",
            "description": None,
            "is_completed": True,
            "priority": "medium",
            "created_at": "2003-10-14T10:53:40+00:00"
        },
        {
            "id": "b2a4606d-ecd3-4504-afe3-4987ae7f228a",
            "title": "Ad ut sunt officia commodo eiusmod.",
            "description": "Ad non nulla proident pariatur ullamco ad proident.",
            "is_completed": True,
            "priority": "high",
            "created_at": "1977-01-13T20:38:44+00:00"
        },
        {
            "id": "9aa51b30-8c9a-45e2-adef-d7f5acf35848",
            "title": "In cupidatat occaecat consequat laborum mollit cupidatat magna.",
            "description": "Duis cillum qui eu quis ea.",
            "is_completed": False,
            "priority": "low",
            "created_at": "2020-11-02T02:58:04+00:00"
        },
        {
            "id": "3c64b6ed-17bf-4fb7-a891-da600f9a4f3e",
            "title": "Cillum ut sit in aliqua pariatur sit dolore id et occaecat ullamco laborum et.",
            "description": "Culpa excepteur dolor sunt fugiat officia magna officia.",
            "is_completed": False,
            "priority": "high",
            "created_at": "2003-03-08T23:02:03+00:00"
        },
        {
            "id": "a32c4d33-fe2d-4378-88b6-bb7d669eef7e",
            "title": "Ullamco do proident dolor occaecat quis id.",
            "description": "Mollit magna ullamco laborum consequat labore dolor enim reprehenderit aliquip occaecat in.",
            "is_completed": True,
            "priority": "medium",
            "created_at": "1997-10-13T13:32:43+00:00"
        },
        {
            "id": "fd0c33c2-645e-4adb-8539-82b0c5b2f7c9",
            "title": "Adipisicing pariatur anim laboris dolor.",
            "description": None,
            "is_completed": False,
            "priority": "high",
            "created_at": "2024-11-02T08:53:42+00:00"
        },
        {
            "id": "d6791d33-0563-4666-be64-9f48ab5b40fe",
            "title": "Anim Lorem incididunt ea ut anim ullamco nulla mollit dolore magna cupidatat.",
            "description": "Consequat incididunt proident nostrud ex eu irure sunt ipsum aliquip.",
            "is_completed": False,
            "priority": "medium",
            "created_at": "2003-06-10T00:38:01+00:00"
        },
        {
            "id": "56c22975-cffb-4806-ab1e-e71fca81d870",
            "title": "Velit enim occaecat mollit sunt ipsum culpa Lorem aliquip ea enim cillum.",
            "description": None,
            "is_completed": True,
            "priority": "high",
            "created_at": "1990-08-20T22:14:53+00:00"
        }
    ]
}