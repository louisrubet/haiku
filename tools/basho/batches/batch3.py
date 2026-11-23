B3 = """
40|basho-shirauo-nori|白魚や/黒き目をあく/法の網|白魚|Petits poissons blancs/leurs yeux noirs s'ouvrent/dans le filet de la Loi
41|basho-ayu-no-ko|鮎の子の/白魚おくる/別れ哉|白魚|Les jeunes ayus/escortent les poissons blancs/c'est l'adieu
43|basho-okiyo|起きよ起きよ/我友にせん/ぬる胡蝶|胡蝶|Réveille-toi, réveille-toi/je ferai de toi mon ami/papillon endormi
44|basho-cho-no-tobu|蝶のとぶ/ばかり野中の/日影哉|蝶|Rien que des papillons/pour faire de l'ombre/en plein champ
45|basho-kimi-ya-ware|君や我れ/我れや荘子の/夢心|蝶|Toi ou moi/moi ou Zhuangzi/un cœur qui rêve
48|basho-cho-no-ha|蝶の羽の/幾度越ゆる/塀の屋根|蝶|Ailes de papillon/combien de fois franchissent-elles/le faîte du mur
50|basho-okorago|御子良子の/一本ゆかし/梅の花|梅|Chez les jeunes prêtresses/un seul prunier, si touchant/en fleurs
51|basho-ume-wakana|梅若菜/鞠子の宿の/とろゝ汁|梅|Pruniers, jeunes herbes/et à l'étape de Mariko/la soupe d'igname
52|basho-ume-ga-ka-notto|梅が香に/のつと日の出る/山路哉|梅|Parfum de prunier/soudain le soleil surgit/sur le chemin de montagne
53|basho-yamazato-manzai|山里は/万歳遅し/梅の花|梅|Au village de montagne/les chanteurs du Nouvel An tardent/pruniers en fleurs
54|basho-ume-no-ki|梅の木に/尙やどり木や/梅の花|梅|Sur le vieux prunier/encore un rameau greffé/fleurs de prunier
55|basho-kono-ume|この梅に/牛も初音と/なきつべし|梅|Devant ce prunier/même le bœuf lancerait/son premier chant
56|basho-tabigarasu|旅烏/古巢は梅に/なりにけり|梅|Corbeau voyageur/ton vieux nid/est devenu un prunier en fleurs
59|basho-akokuso|あこくその/心は知らず/梅の花|梅|Le cœur d'Akokuso/je l'ignore/fleurs de prunier
60|basho-ume-shiroshi|梅白し/きのふや鶴を/盗まれし|梅|Pruniers blancs/hier donc on vous a volé/votre grue
62|basho-ka-ni-nioe|香に匂へ/雲丹掘る岡の/梅の花|梅|Répands ton parfum/sur la colline de la tourbe/fleur de prunier
63|basho-wasurena-yo|忘れなよ/藪の中なる/梅の花|梅|Ne l'oublie pas/au milieu du fourré/le prunier en fleurs
64|basho-kobai|紅梅や/見ぬ恋つくる/玉簾|紅梅|Prunier rouge/un amour sans visage naît/derrière le store
66|basho-sato-no-ko|里の子よ/梅拆りのこせ/牛の鞭|梅|Enfant du village/pour fouetter ton bœuf/épargne le prunier
67|basho-tsukimachi|月待や/梅かたげゆく/小山伏|梅|Veillée de lune/un jeune ascète passe/un rameau de prunier à l'épaule
68|basho-mukashi-no-ichiji|梅が香に/昔の一字/哀れ也|梅|Parfum de prunier/le seul mot « autrefois »/si poignant
69|basho-haru-mo-yaya|春もやゝ/景色とゝのふ/月と梅|梅|Le printemps/prend forme peu à peu/la lune et les pruniers
70|basho-ume-yanagi|梅柳/さぞ若衆かな/女哉|梅|Prunier et saule/l'un un bel adolescent/l'autre une femme
71|basho-kazoe-kinu|かぞへ来ぬ/屋敷々々の/梅柳|梅|J'ai compté en marchant/demeure après demeure/pruniers et saules
72|basho-furukawa|古川に/こびて芽を張る/柳哉|柳|Faisant les yeux doux/au vieux ruisseau/le saule bourgeonne
73|basho-hakkuken|八九間/空で雨降る/柳哉|柳|Sur huit ou neuf toises/il pleut encore dans les airs/le saule
75|basho-uguisu-kasa|鶯の/笠落したる/椿かな|椿|Le rossignol/a laissé tomber son chapeau/fleur de camélia
76|basho-ryo-no-te|両の手に/桃と桜や/草の餅|桃|Dans mes deux mains/le pêcher et le cerisier/gâteaux d'armoise
77|basho-funaashi|舟足も/休む時あり/浜の桃|桃|Même les bateaux/prennent leur temps/pêchers en fleurs sur la grève
"""

NOTES = {
 "basho-shirauo-nori": "On a painting of the Zen monk Kensu, who fished for shrimp with a net.",
 "basho-ayu-no-ko": "Setting off on the Narrow Road: young disciples see off Bashō and Sora.",
 "basho-okiyo": "Echoes Zhuangzi's dream of being a butterfly.",
 "basho-kimi-ya-ware": "Zhuangzi dreamt he was a butterfly and no longer knew which one was dreaming.",
 "basho-okorago": "At Ise, the only plum tree grew behind the house of the shrine maidens.",
 "basho-ume-wakana": "Farewell to a disciple leaving for Edo along the Tōkaidō.",
 "basho-yamazato-manzai": "Manzai: New Year singers who go from door to door and reach remote villages last.",
 "basho-ume-no-ki": "Greeting to a poet whose father was a famous poet: the old tree and its new branch.",
 "basho-kono-ume": "Plum and ox are emblems of Sugawara no Michizane; the first song is usually the bush warbler's.",
 "basho-tabigarasu": "Bashō back in his home town for New Year.",
 "basho-akokuso": "Akokuso: Ki no Tsurayuki as a child; his poem doubts people's hearts but not the plum's scent.",
 "basho-ume-shiroshi": "The host is compared to Lin Bu, who lived among plum trees with a crane.",
 "basho-ka-ni-nioe": "Peat was dug near Iga and gave off a foul smell.",
 "basho-wasurena-yo": "Farewell to a monk leaving for the north: come back to my hut.",
 "basho-tsukimachi": "Tsukimachi: a gathering to wait for the moonrise.",
 "basho-mukashi-no-ichiji": "Condolences to a disciple whose son had died the previous spring.",
 "basho-hakkuken": "The rain has almost stopped, but it still drips under the wide willow.",
 "basho-uguisu-kasa": "In old poems the bush warbler sews plum blossoms into a hat.",
 "basho-ryo-no-te": "Doll festival with his two leading disciples, Kikaku and Ransetsu.",
}
