"""Shared helpers: kanji modernisation, comparison key, paths, displayable glyphs."""
import difflib, json, re, unicodedata

OLD_NEW = dict(zip(
    "戀聲雜餠齒萬歲惠萊瀨淚櫻舊佛曉鄕黑靑淸晝澤雙盡氣歸來樂實寢寶參圓團國學擧覺讀賣變戶髮傳廣兩竝價濱邊邉驛鐵靜錢燈爐稻穗蟲螢鷄狀曾增嶋龜鹽豐醉戲碎拂拔收隱險驗縣對將黃廢發權歡觀聽應惡假僞從徑經輕莖壽晚步每卷乘亞惱繪會靈獵嚴巖餘圍窗甁旣姬渴揭禪祕鄰郞瓣辯辨畫晝擇譯纖續綠緣蠅總聰橫濕顯擊條槪狹壓髙隣曆歷團蘆藏莊裝壯薰勳殘淺錢踐將奬樣險檢劍儉臟髓體豫與譽舉兒嶺稱彈圖廳縱獨觸屬醫澁搖謠遙遞齋齊濟劑淨爭靜囑卽",
    "恋声雑餅歯万歳恵莱瀬涙桜旧仏暁郷黒青清昼沢双尽気帰来楽実寝宝参円団国学挙覚読売変戸髪伝広両並価浜辺辺駅鉄静銭灯炉稲穂虫蛍鶏状曽増島亀塩豊酔戯砕払抜収隠険験県対将黄廃発権歓観聴応悪仮偽従径経軽茎寿晩歩毎巻乗亜悩絵会霊猟厳巌余囲窓瓶既姫渇掲禅秘隣郎弁弁弁画昼択訳繊続緑縁蝿総聡横湿顕撃条概狭圧高隣暦歴団芦蔵荘装壮薫勲残浅銭践将奨様険検剣倹臓髄体予与誉挙児嶺称弾図庁縦独触属医渋揺謡遥逓斎斉済剤浄争静嘱即"))


def modern(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return "".join(OLD_NEW.get(c, c) for c in s)


def key(s: str) -> str:
    """Comparison key: modern kanji, no iteration marks or punctuation."""
    s = modern(s)
    out = []
    for c in s:
        if c in "ゝヽ" and out:
            out.append(out[-1])
        elif c in "ゞヾ" and out:
            out.append(chr(ord(out[-1]) + 1))
        elif c == "々" and out:
            out.append(out[-1])
        elif re.match(r"[\u3040-\u30ff\u4e00-\u9fff]", c):
            out.append(c)
    return "".join(out)



import pathlib

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parents[1]
WORKS = REPO / "works"
DATA = TOOLS / "data"
CACHE = TOOLS / "cache"
ITO_BASE = "https://www2.yamanashi-ken.ac.jp/~itoyo/basho/haikusyu/"
USER_AGENT = "HaikuResearch/0.1 (https://haiku.rubet.fr)"

# Glyph ranges of the GaggiMate standby font.
GLYPHS = [(0x20, 0x7E), (0xA0, 0xFF), (0x14C, 0x14D), (0x152, 0x153), (0x16A, 0x16B), (0x178, 0x178),
          (0x2013, 0x2014), (0x2018, 0x2019), (0x201C, 0x201D), (0x2026, 0x2026), (0x20AC, 0x20AC)]


def glyph_ok(s: str) -> bool:
    return all(c == "\n" or any(a <= ord(c) <= b for a, b in GLYPHS) for c in s)


def matched(seasons):
    """1903 collection entries of the given seasons, in the order used by lot indexes."""
    rows = json.load(open(DATA / "matched.json"))
    return [r for r in rows if r["season"] in seasons and not r.get("dup")]
