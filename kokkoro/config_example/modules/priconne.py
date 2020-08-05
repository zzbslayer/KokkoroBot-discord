class arena:
    AUTH_KEY = "YOUR_KEY"

horse_pool = {
    "MIX": {
        "number": [ "01", "02", "03", "04" ],
        "_comment": "other_player填未实装角色",
        "player": [
            "杏奈","真步","璃乃","初音","霞","伊绪",
            "咲恋","望","妮诺","秋乃","镜华","智","真琴",
            "伊莉亚","纯","静流","莫妮卡","流夏","吉塔",
            "亚里莎","安","古蕾娅", "空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜", "流夏(夏日)",
            "伊莉亚(圣诞节)", "优妮", "琪爱儿", "霞(魔法少女)", "杏奈(夏日)",
            "リン(レンジャー)", "マヒル(レンジャー)", "璃乃(奇境)", "祈梨",
            "贪吃佩可(公主)", "优衣(公主)", "可可萝(公主)", "茉莉", "茜里", "宫子", "雪",
            "七七香", "美里", "铃奈", "香织", "美美", "绫音", "铃", "惠理子",
            "忍", "真阳", "栞", "千歌", "空花", "珠希", "美冬", "深月","纺希",
            "日和", "怜", "禊", "胡桃", "依里", "铃莓", "优花梨", "碧", "美咲",
            "莉玛", "步未"
        ],
        "other_player": [   ]
    },
    "TW": {
        "number": [ "01", "02", "03", "04" ],
        "_comment": "other_player填未实装角色",
        "player": [
            "杏奈","真步","璃乃","初音","霞","伊绪",
            "咲恋","望","妮诺","秋乃","镜华","智","真琴",
            "伊莉亚","纯","静流","莫妮卡","流夏","吉塔",
            "亚里莎","安","古蕾娅", "空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜", "优妮",
            "伊莉亚(圣诞节)", "霞(魔法少女)", "贪吃佩可(公主)",
            "茉莉","茜里","宫子","雪","七七香","美里",
            "铃奈","香织","美美","绫音","铃","惠理子",
            "忍","真阳","栞","千歌","空花","珠希","美冬",
            "深月","纺希", "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛","步未"
        ],
        "other_player": [ "琪爱儿", "リン(レンジャー)", "マヒル(レンジャー)", "璃乃(奇境)", "祈梨"]
    },
    "JP": {
        "number": [ "01", "02", "03", "04" ],
        "_comment": "other_player填未实装角色",
        "player": [
            "杏奈","真步","璃乃","初音","霞","伊绪",
            "咲恋","望","妮诺","秋乃","镜华","智","真琴",
            "伊莉亚","纯","静流","莫妮卡","流夏","吉塔",
            "亚里莎","安","古蕾娅", "空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜", "流夏(夏日)",
            "伊莉亚(圣诞节)", "霞(魔法少女)", "优妮", "琪爱儿", "杏奈(夏日)",
            "リン(レンジャー)", "マヒル(レンジャー)", "璃乃(奇境)", "祈梨", "贪吃佩可(公主)",
            "优衣(公主)", "可可萝(公主)", "茉莉","茜里","宫子","雪","七七香","美里",
            "铃奈","香织","美美","绫音","铃","惠理子",
            "忍","真阳","栞","千歌","空花","珠希","美冬",
            "深月","纺希", "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛","步未"
        ],
        "other_player": [  ]
    },
    "BL": {
        "number": [ "01", "02", "03", "04" ],
        "_comment": "other_player填未实装角色",
        "player": [
            "杏奈","璃乃","真步","伊绪",
            "望","妮诺","秋乃", "亚里莎",
            "静流","莫妮卡","吉塔", "纯",
            "镜华","咲恋","真琴", "初音",
            "伊莉亚", "茉莉","茜里","宫子","雪","铃","美里",
            "铃奈","香织","美美","绫音","惠理子",
            "真阳","栞","千歌","空花","珠希","美冬",
            "深月","忍", "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛"
        ],
        "other_player": [
            "霞", "智", "流夏", "安", "古蕾娅","空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜",
            "伊莉亚(圣诞节)", "霞(魔法少女)", "优妮", "琪爱儿"
        ]
    }
}

gacha_pool = {
    "MIX": {
        "up_prob":  14,
        "s3_prob":  50,
        "s2_prob": 180,
        "up": [ "贪吃佩可(公主)", "祈梨" ],
        "_comment": "star3 仅填3星常驻角色。不要填UP角，否则出率会偏高",
        "star3": [
            "杏奈","真步","璃乃","初音","霞","伊绪",
            "咲恋","望","妮诺","秋乃","镜华","智","真琴",
            "伊莉亚","纯","静流","莫妮卡","流夏","吉塔",
            "亚里莎","安","古蕾娅", "空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜",
            "伊莉亚(圣诞节)", "优妮", "琪爱儿", "霞(魔法少女)",
            "リン(レンジャー)", "マヒル(レンジャー)", "璃乃(奇境)"
        ],
        "other_normal_star3": [   ],
        "star2": [
            "茉莉","茜里","宫子","雪","七七香","美里",
            "铃奈","香织","美美","绫音","铃","惠理子",
            "忍","真阳","栞","千歌","空花","珠希","美冬",
            "深月","纺希"
        ],
        "star1" : [
            "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛","步未"
        ]
    },
    "TW": {
        "up_prob":   7,
        "s3_prob":  25,
        "s2_prob": 180,
        "up": [ "贪吃佩可(公主)" ],
        "_comment": "star3 仅填3星常驻角色。不要填UP角，否则出率会偏高",
        "star3": [
            "杏奈","真步","璃乃","初音","霞","伊绪",
            "咲恋","望","妮诺","秋乃","镜华","智","真琴",
            "伊莉亚","纯","静流","莫妮卡","流夏","吉塔",
            "亚里莎","安","古蕾娅", "空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜",
            "伊莉亚(圣诞节)", "霞(魔法少女)"
        ],
        "other_normal_star3": [ "优妮", "琪爱儿", "リン(レンジャー)", "マヒル(レンジャー)", "璃乃(奇境)", "祈梨"],
        "star2": [
            "茉莉","茜里","宫子","雪","七七香","美里",
            "铃奈","香织","美美","绫音","铃","惠理子",
            "忍","真阳","栞","千歌","空花","珠希","美冬",
            "深月","纺希"
        ],
        "star1" : [
            "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛","步未"
        ]
    },
    "JP": {
        "up_prob":   7,
        "s3_prob":  25,
        "s2_prob": 180,
        "up": [ "祈梨" ],
        "_comment": "star3 仅填3星常驻角色。不要填UP角，否则出率会偏高",
        "star3": [
            "杏奈","真步","璃乃","初音","霞","伊绪",
            "咲恋","望","妮诺","秋乃","镜华","智","真琴",
            "伊莉亚","纯","静流","莫妮卡","流夏","吉塔",
            "亚里莎","安","古蕾娅", "空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜",
            "伊莉亚(圣诞节)", "霞(魔法少女)", "优妮", "琪爱儿",
            "リン(レンジャー)", "マヒル(レンジャー)", "璃乃(奇境)"
        ],
        "other_normal_star3": [ "璃乃(奇境)" ],
        "star2": [
            "茉莉","茜里","宫子","雪","七七香","美里",
            "铃奈","香织","美美","绫音","铃","惠理子",
            "忍","真阳","栞","千歌","空花","珠希","美冬",
            "深月","纺希"
        ],
        "star1" : [
            "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛","步未"
        ]
    },
    "BL": {
        "up_prob":   7,
        "s3_prob":  25,
        "s2_prob": 180,
        "up": [ "镜华" ],
        "_comment": "star3 仅填3星常驻角色。不要填UP角，否则出率会偏高",
        "star3": [
            "杏奈","璃乃","初音","伊绪",
            "望","妮诺","秋乃", "亚里莎",
            "静流","莫妮卡","吉塔", "纯"
        ],
        "other_normal_star3": [
            "霞", "智", "伊莉亚", "纯", "流夏", "安", "古蕾娅","空花(大江户)", "妮诺(大江户)",
            "克萝依", "碧(插班生)", "美美(万圣节)", "露娜",
            "伊莉亚(圣诞节)", "霞(魔法少女)", "优妮", "琪爱儿"
        ],
        "star2": [
            "茉莉","茜里","宫子","雪","铃",
            "铃奈","香织","美美","绫音","惠理子",
            "真阳","栞","千歌","空花","珠希","美冬",
            "深月","铃"
        ],
        "star1" : [
            "日和","怜","禊","胡桃","依里","铃莓",
            "优花梨","碧","美咲","莉玛"
        ]
    }
}