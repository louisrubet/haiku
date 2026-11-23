B10 = """
0|basho-hatsuaki-kaya|初秋や/たゝみながらの/蚊帳の𧝒|初秋|Début d'automne/la moustiquaire pliée/sert de couverture
1|basho-hatsuaki-umi|初秋や/海も青田の/一みどり|初秋|Début d'automne/la mer et les rizières/d'un seul vert
2|basho-harinuki|張ぬきの/猫も知るべし/今朝の秋|立秋|Même le chat de papier mâché/doit le savoir/l'automne est là ce matin
5|basho-fumizuki|文月や/六日も常の/夜には似ず|文月|Septième mois/même la nuit du six/n'est pas une nuit comme les autres
6|basho-hiyahiya|ひやひやと/壁をふまひて/昼寝哉|冷|Fraîcheur/les pieds contre le mur/je fais la sieste
7|basho-aki-suzushi|秋凉し/手毎にむけや/瓜茄子|秋凉|Fraîcheur d'automne/que chacun épluche/melons et aubergines
8|basho-nyumen|乳麵の/下焚きつくる/夜寒哉|夜寒|Sous les nouilles/on attise le feu/froid du soir
9|basho-yu-no-nagori|溫泉の名残/今宵は肌の/寒からん|肌寒|Adieu aux sources chaudes/ce soir ma peau/aura froid
10|basho-uchikuzushitaru|秋の夜を/うち崩したる/噺哉|秋の夜|La nuit d'automne/nous l'avons mise en pièces/à force de bavarder
11|basho-hitogoe|人声や/この道かへる/秋の暮|秋の暮|Des voix/on rentre par ce chemin/soir d'automne
13|basho-shinimo-senu|死もせぬ/旅寝の果よ/秋の暮|秋の暮|Je ne suis pas mort/au bout de tant de nuits en voyage/soir d'automne
14|basho-miokuri|見送りの/うしろや淋し/秋の暮|秋の暮|Après l'adieu/mon dos est si seul/soir d'automne
15|basho-kochira-muke|こちら向け/我も淋しき/秋の暮|秋の暮|Tourne-toi vers moi/je suis seul moi aussi/soir d'automne
16|basho-kuri-no-iga|行く秋や/手を広げたる/栗の毬|ゆく秋|L'automne s'en va/elles ouvrent leurs mains/les bogues de châtaigne
17|basho-minobuton|ゆく秋や/身にひきまとふ/三布蒲団|ゆく秋|L'automne s'en va/je m'enroule dans/ma couverture étroite
18|basho-matsukaze-noki|松風の/軒をめぐりて/秋暮れぬ|秋の暮|Le vent dans les pins/fait le tour de l'auvent/l'automne s'achève
21|basho-karikakeshi|刈りかけし/田面の鶴や/里の秋|秋|Dans la rizière à moitié fauchée/une grue/automne au village
22|basho-kono-aki|此秋は/何で年寄る/雲に鳥|秋|Cet automne/pourquoi ai-je tant vieilli/un oiseau dans les nuages
23|basho-okuraretsu|送られつ/送りつ果は/木曽の秋|秋|Raccompagné, raccompagnant/et pour finir/l'automne de Kiso
24|basho-kono-matsu|この松の/実生せし世や/神の秋|秋|Ce pin/en quel âge a-t-il germé/automne des dieux
25|basho-nukamiso|秋の色/糖味噌壺も/なかりけり|秋|Couleurs d'automne/il n'avait même pas/un pot de son fermenté
26|basho-namushi|胡蝶にも/ならで秋経る/菜虫哉|秋|Sans devenir papillon/elle traverse l'automne/la chenille du chou
27|basho-sabishisa-suma|淋しさや/須磨に勝ちたる/浜の秋|秋|Solitude/plus grande encore qu'à Suma/automne sur cette plage
28|basho-aki-ni-soite|秋にそひて/ゆかばや末は/小松川|秋|Suivant l'automne/j'irais bien jusqu'au bout/à Komatsugawa
30|basho-tanabata-sadamuru|七夕や/秋を定むる/はじめの夜|七夕|Tanabata/la première nuit/qui fixe l'automne
31|basho-nemu-no-ki|合歓の木の/葉ごしもいとへ/星の影|七夕|Même à travers les feuilles du mimosa/cachez-vous bien/étoiles des amants
32|basho-takamizu|高水に/ほしも旅寝の/岩の上|七夕|Fleuve en crue/les étoiles aussi dorment en voyage/sur un rocher
34|basho-kazu-naranu|数ならぬ/身とな思ひそ/魂祭|盆|Ne te crois pas/de si peu de compte/fête des âmes
35|basho-kumasaka|熊坂が/ゆかりやいつの/魂祭|盆|Kumasaka/quels parents prient pour lui/à la fête des âmes
36|basho-watayumi|綿弓や/琵琶に慰む/竹の奥|綿弓|L'arc à carder le coton/consolant comme un luth/au fond des bambous
37|basho-saruhiki|猿引は/猿の小袖を/砧かな|砧|Le montreur de singes/bat sur la pierre/la petite robe du singe
38|basho-koe-sumite|声澄みて/北斗に響く/砧哉|砧|Son très clair/jusqu'à la Grande Ourse/le battoir à étoffe
"""

NOTES = {
 "basho-harinuki": "Echoes the Kokinshū: autumn is not seen, it is heard in the wind; the toy cat's head nods.",
 "basho-fumizuki": "The night before Tanabata, when the two star lovers meet; on the Narrow Road.",
 "basho-aki-suzushi": "Thanks for a simple meal at Kanazawa, on the Narrow Road.",
 "basho-nyumen": "Nyūmen: noodles served hot in broth.",
 "basho-yu-no-nagori": "Farewell to his young host at the Yamanaka hot spring, on the Narrow Road.",
 "basho-uchikuzushitaru": "On his last journey, an evening of talk with friends at Osaka.",
 "basho-hitogoe": "Early version of 'This road, no one goes along it, autumn dusk'.",
 "basho-shinimo-senu": "End of the Journey of the Weathered Skeleton, which he began ready to die on the road.",
 "basho-kochira-muke": "On a monk's self-portrait painted with his face turned away.",
 "basho-kuri-no-iga": "Farewell to his home province Iga on his last journey; iga also means chestnut burr.",
 "basho-minobuton": "A three-width quilt: a narrow, poor man's cover.",
 "basho-kono-aki": "One of Bashō's last poems, written a few weeks before his death.",
 "basho-okuraretsu": "On the Sarashina journey through the Kiso mountains.",
 "basho-kono-matsu": "At the Kashima shrine, on the Kashima journey.",
 "basho-nukamiso": "On a portrait of Kenkō, who wrote that a recluse should not even own a pot of pickling bran.",
 "basho-sabishisa-suma": "At Iro beach, on the Narrow Road; Suma is the loneliest shore of the Tale of Genji.",
 "basho-nemu-no-ki": "Tanabata, when the two star lovers meet once a year; the mimosa folds its leaves at night.",
 "basho-takamizu": "Rain on Tanabata: the star lovers cannot cross the swollen River of Heaven.",
 "basho-kazu-naranu": "Festival of the dead after the death of Jutei, a woman close to Bashō.",
 "basho-kumasaka": "Kumasaka Chōhan, a famous bandit killed by the young Yoshitsune; on the Narrow Road.",
 "basho-watayumi": "Greeting to a host in Yamato; the cotton-carding bow twangs like a lute.",
 "basho-koe-sumite": "Echoes Li Bai: women beat cloth under the autumn moon for absent husbands.",
}
