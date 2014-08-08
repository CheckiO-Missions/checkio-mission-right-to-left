"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
TESTS = {
    "Basics": [
        {
            "input": ("left", "right", "left", "stop"),
            "answer": "left,left,left,stop",
        },
        {
            "input": ("bright aright", "ok"),
            "answer": "bleft aleft,ok",
        },
        {
            "input": ("brightness wright",),
            "answer": "bleftness wleft",
        },
        {
            "input": ("enough", "jokes"),
            "answer": "enough,jokes",
        },

    ],
    "Extra": [
        {
            "input": ("r", "i", "g", "h", "t"),
            "answer": "r,i,g,h,t",
        },
        {
            "input": (
            'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit', 'aenean', 'commodo',
            'ligula', 'eget', 'dolor', 'aenean', 'massa', 'cum', 'sociis', 'natoque', 'penatibus', 'et', 'magnis',
            'dis', 'parturient', 'montes', 'nascetur', 'ridiculus', 'mus', 'donec', 'quam', 'felis', 'ultricies', 'nec',
            'pellentesque', 'eu', 'pretium', 'quis', 'sem', 'nulla', 'consequat', 'massa', 'quis'),
            "answer": 'lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,elit,aenean,commodo,ligula,eget,dolor,aenean,massa,cum,sociis,natoque,penatibus,et,magnis,dis,parturient,montes,nascetur,ridiculus,mus,donec,quam,felis,ultricies,nec,pellentesque,eu,pretium,quis,sem,nulla,consequat,massa,quis',

        },
        {
            "input": ("right",) * 20,
            "answer": ",".join(("left",) * 20)
        },
        {
            "input": ("right", "left") * 10,
            "answer": ",".join(("left",) * 20)
        },



    ]
}
