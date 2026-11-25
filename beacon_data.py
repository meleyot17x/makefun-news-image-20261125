# THE BEACON POST - content for Tuesday 25 November 2026.
# Every fact, figure and claim below comes from the locked NI25 pool.
# Claims are labelled as claims; the PCE card carries no figure because
# the report is only due today and no number has been published.

MASTHEAD = "THE BEACON POST"
DATE_LINE = "TUESDAY 25 NOVEMBER 2026"
KICKER_LEFT = "37 DATED STORIES - 9 REGIONS - EVERY STORY SOURCED & CHECKED"
KICKER_RIGHT = "ONE DAY - ONE PAGE"
SUBLINE = "The whole day on one page - every story dated, sourced and checked."

# Lead trio (pool cards 4, 3, 5 - matrix order for this account).
LEADS = [
    {
        "no": 1, "region": "MIDDLE EAST", "place": "Gaza", "scene": "gaza",
        "head": "Drone strikes kill Hamas security chief",
        "deck": ("Israeli drone strikes across Gaza killed a senior Hamas "
                 "security official, three policemen and three siblings - "
                 "one a child. Seven dead in all."),
        "chip": "7 KILLED IN STRIKES", "src": "Al Jazeera", "cert": "REPORTED",
    },
    {
        "no": 2, "region": "MIDDLE EAST", "place": "Iraq", "scene": "iraq",
        "head": "Baghdad orders Kurdish oilfields seized",
        "deck": ("PM Ali al-Zaidi orders federal units to seize oilfields "
                 "and crossings in Kurdish-run regions. President Barzani "
                 "replies: Kurdistan 'will not submit'."),
        "chip": "OILFIELDS ORDER", "src": "Starlit / wires", "cert": "REPORTED",
    },
    {
        "no": 3, "region": "EUROPE", "place": "Brussels", "scene": "eu",
        "head": "EU unveils new Russia sanctions",
        "deck": ("The European Union announced further restrictive measures "
                 "against Russia amid the war in Ukraine - another turn of "
                 "the sanctions screw on Tuesday."),
        "chip": "NEW EU SANCTIONS", "src": "Wire roundups", "cert": "REPORTED",
    },
]

# Grid of ten full cards (pool cards 1, 2, 6, 36, 33, 10, 11, 13, 14, 37).
GRID = [
    {
        "no": 4, "region": "EUROPE", "place": "Poland", "scene": "awacs",
        "head": "NATO sends early-warning jets to Poland",
        "deck": ("AWACS deployment after Russian missiles landed in Poland; "
                 "Merz vows complete German support."),
        "chip": "AWACS TO POLAND", "src": "Wire reports", "cert": "REPORTED",
    },
    {
        "no": 5, "region": "MIDDLE EAST", "place": "Strait of Hormuz",
        "scene": "hormuz",
        "head": "Iran says 3 tankers hit by mines",
        "deck": ("IRGC claims three oil tankers hit by naval mines in the "
                 "Strait of Hormuz. A claim - not confirmed."),
        "chip": "3 TANKERS HIT - IRAN SAYS", "src": "Iranian claim via wires",
        "cert": "CLAIMED",
    },
    {
        "no": 6, "region": "WORLD", "place": "Ukraine", "scene": "warcount",
        "head": "700,000 Russian dead, new count finds",
        "deck": ("New analysis finds more than 700,000 Russian soldiers "
                 "killed in the nearly five-year war."),
        "chip": "700,000+ KILLED", "src": "RFE/RL", "cert": "REPORTED",
    },
    {
        "no": 7, "region": "WORLD", "place": "Nvidia", "scene": "nvidia",
        "head": "Nvidia's $1 trillion Monday",
        "deck": ("Monday close +31.5%; nearly $1 trillion clawed back as "
                 "Huang returns as CEO, +$34bn in a day."),
        "chip": "+31.5% MONDAY", "src": "Forbes via wires", "cert": "REPORTED",
        "tag": "MONDAY CLOSE",
    },
    {
        "no": 8, "region": "WORLD", "place": "Washington", "scene": "pce",
        "head": "PCE inflation report due today",
        "deck": ("US PCE inflation report due Tuesday 25 November. Figure "
                 "not yet out - none is printed here."),
        "chip": "PCE DUE TODAY", "src": "Scheduled", "cert": "SCHEDULED",
    },
    {
        "no": 9, "region": "ASIA", "place": "China", "scene": "xiamen",
        "head": "Xiamen Airlines orders 50 Boeing jets",
        "deck": "China Southern unit Xiamen Airlines agreed to acquire 50 Boeing 737-8 jets.",
        "chip": "50 JETS ORDERED", "src": "Wires", "cert": "REPORTED",
    },
    {
        "no": 10, "region": "EUROPE", "place": "Madrid", "scene": "madrid",
        "head": "Madrid rout PSV 5-1 in comeback",
        "deck": "Madrid overturned a deficit to beat PSV 5-1: Bellingham stunner, Mbappe brace.",
        "chip": "MADRID 5-1 PSV", "src": "Wires", "cert": "REPORTED",
    },
    {
        "no": 11, "region": "OCEANIA", "place": "Australia", "scene": "coral",
        "head": "12 coral species brought back",
        "deck": ("GBR genetic analysis resurrects 12 Acropora coral species; "
                 "diversity wider than known."),
        "chip": "12 SPECIES BACK", "src": "Science wires", "cert": "REPORTED",
    },
    {
        "no": 12, "region": "OCEANIA", "place": "Fiji", "scene": "fiji",
        "head": "Fiji declares disaster in dry spell",
        "deck": "Nationwide disaster declared amid an El Nino dry spell.",
        "chip": "DISASTER DECLARED", "src": "Wires", "cert": "REPORTED",
    },
    {
        "no": 13, "region": "AMERICAS", "place": "USA", "scene": "storms",
        "head": "Storms target Thanksgiving travel",
        "deck": "Bad weather on both US shorelines risks Thanksgiving travel for millions.",
        "chip": "STORMS BOTH COASTS", "src": "Wires", "cert": "REPORTED",
    },
]

# Number strip: eight figures, each tied to a card on this page.
NUMBERS = [
    ("700,000+", "RUSSIAN DEAD - NEW COUNT"),
    ("3", "TANKERS HIT - IRAN SAYS"),
    ("7", "KILLED IN GAZA STRIKES"),
    ("50", "BOEING 737-8 ORDERED"),
    ("5-1", "MADRID ROUT PSV"),
    ("+31.5%", "NVIDIA - MONDAY CLOSE"),
    ("12", "CORAL SPECIES BACK"),
    ("23", "INJURED - COLOMBIA BOMB"),
]

# Region strip: honest counts across all 37 stories on the page.
REGIONS = [
    ("EUROPE", 8), ("MIDDLE EAST", 6), ("WORLD", 6), ("AFRICA", 5),
    ("AMERICAS", 4), ("ASIA", 2), ("SOUTH ASIA", 2),
    ("ASIA-PACIFIC", 2), ("OCEANIA", 2),
]

# Timeline: six slots, every one anchored in the pool.
TIMELINE = [
    ("22 NOV", "Iran electricity rationing begins"),
    ("MON", "Nvidia close: +31.5%, Huang back"),
    ("TUE", "PCE report due, Washington"),
    ("TUE", "AWACS bound for Poland"),
    ("TUE", "Madrid 5-1 PSV at full time"),
    ("TUE", "Fiji declares disaster"),
]

# ALSO ON THE PAGE: briefs 14-37 (pool cards 7,8,9,12,15,16,17,18,19,20,
# 21,22,23,24,25,26,27,28,29,30,31,32,34,35 in pool order).
BRIEFS = [
    "5 Lynx KF41 IFVs enter Ukrainian service",
    "Car bomb injures at least 23 in Colombia",
    "Dozens held in Cartagena supermarket",
    "England chase 185 in T20I; Fraser-McGurk 27",
    "Iran pharmacies run dry; patients cut doses",
    "Iran braces for winter gas shortages",
    "Britain sanctions Houthis, 4 rebel officials",
    "Senegal AFCON title restored by CAS ruling",
    "Rebels pull back after DR Congo clashes",
    "Nigerian emir suspended after allegation",
    "Sudan RSF commander defects",
    "Cameroon separatist in Norway war crimes court",
    "Old allies reunite in Punjab: BJP + Akali Dal",
    "Bangladesh opens Invest office in Guangzhou",
    "Indonesia's vice-president resigns",
    "Solomon Islands eye Australia treaty",
    "North Korea touts China ties at embassy visit",
    "Denmark court upholds 'ghetto' evictions law",
    "Sarkozy headed for Libya-case trial in Paris",
    "Black Sea clash at the UN over shipping",
    "Shortwave school returns for Afghan girls",
    "Asteroid eclipse: Dimorphos shadows Didymos",
    "US targets 7 firms over chips; one Alibaba's",
    "Decoy army: Moscow buys inflatable decoys",
]

# DATE CHECK: five named discards - stories that are NOT today's news.
DATE_CHECKS = [
    "Mercury explainer - 23 November, not today",
    "COP31 talks - closed earlier this month",
    "Liverpool 4-0 - a weekend score, not Tuesday",
    "GTA VI launch hype - no release today",
    "Thanksgiving Day itself - Thursday, not today",
]

# Map pins for the 13 full cards: page number -> short legend label.
PIN_LABELS = [
    "Gaza", "Iraq", "Brussels", "Poland", "Hormuz", "Ukraine",
    "Nvidia", "Washington", "Xiamen", "Madrid", "Gt Barrier Reef",
    "Fiji", "US coasts",
]

FOOTER_LEFT = ("Sources: RFE/RL - Al Jazeera - DW - Forbes - Starlit Daily "
               "- wire roundups. Claims labelled as claims.")
FOOTER_RIGHT = "Original drawings - drawn for this page"
