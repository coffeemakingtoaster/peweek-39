import random

NAMES = [
"gurkwaan",
"Herjeman",
"jollilala",
"coffee",
"Heuser",
"SReaperz",
"ACE",
"Walkercito",
"CanIIAweekee",
"Fazootle",
"Yash",
"smoktwix",
"Doger",
"Pykemon011",
"Dudnikov",
"rikovmike",
"Juna_Gala",
"regarrzo",
"curious__being",
"senwelley",
"Join this team?",
"siddhartha14",
"Lemonadehead",
"DR1ID",
"tabishrfx",
"PyNon",
"Ununennium",
"Manxuma124",
"Barracade",
"zobi",
"KNKWasTaken",
"unilhexium",
"RicBin",
"PyWhiz",
"Anders",
"Jiggly_Balls",
"Djorm",
"Wardini",
"Spears Dracona",
"yarolig",
"Gato",
"visheshdvivedi",
"Apex",
"inkontoasty",
"Tee",
"RestrictionGame",
"francisco",
"Cosmologicon",
"prake",
"ntoll",
"mit-mit",
"MsPear",
"Master_cheese13",
"mauve",
"Sebolpayer_",
"speedlimit36",
"omnia",
"PyTM31",
"Phantasma",
"ericsonwillians"
]

def generate_name() -> str:
    return random.choice(list(set(NAMES)))

