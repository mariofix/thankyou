import random

thanks_array = [
    "dankie",
    "faleminderit",
    "shukran",
    "chnorakaloutioun",
    "hvala",
    "blagodaria",
    "gràcies",
    "M̀h’gōi",
    "děkuji",
    "tak",
    "dank u",
    "tänan",
    "kiitos",
    "merci",
    "danke",
    "ευχαριστώ",
    "mahalo",
    "shukriya",
    "takk",
    "terima kasih",
    "grazie",
    "arigatô",
    "gamsahamnida",
    "paldies",
    "choukrane",
    "ačiū",
    "blagodaram",
    "terima kasih",
    "grazzi",
    "Xièxiè",
    "bayarlalaa",
    "dziękuję",
    "obrigado",
    "mulţumesc",
    "спасибо",
    "Ďakujem",
    "gracias",
    "tack",
    "nandri",
    "kop khun",
    "teşekkür ederim",
    "Дякую",
    "diolch",
    "a dank",
    "ngiyabonga",
    "dankon",
]


def give_thanks():
    return random.choice(thanks_array)
