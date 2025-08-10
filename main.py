def main():
    print(yyh_characters())

def yyh_characters():
    character_list = [
        "yusuke urameshi",
        "kazuma kawabara",
        "kurama",
        "hiei",
        "genkai",
        "botan",
        "keiko yukimura",
        "koenma",
        "toguro",
        "karasu",
        "shinobu sensui",
        "itsuki",
        "suzaku",
        "raizen",
        "mukuro",
        "yomi"
    ]

    team_urameshi = []
    
    for i in character_list:
        list_length = len(team_urameshi)

        if list_length < 8:
            team_urameshi.append(i)

    return team_urameshi

main()