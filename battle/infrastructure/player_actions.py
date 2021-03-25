def get_menu_action():
    return input("""
        Que voulez vous faire ?
        d: Entrer dans une nouvelle dark zone
    """)


def get_user_action():
    return [
        int(input("Quel monstre voulez vous attaquer ? ")) - 1,
        input("Quelle compétence (g: pour grenade) ? ")
    ]
