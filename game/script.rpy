define p = Character("Protagonista")
define m = Character("Monstruo")
define p = Character("Profesor")
define gb = Character("Goblin")

default p_health = 30
default p_atk = 0
default p_def = 0
default p_def_mod = 0
default p_gold = 0

default goblinFriend = False


default m_health = 30
default m_atk = 0
default m_def = 0

label start:

    p "Antes de comenzar, elige tu arma."

    menu:
        "Espada.":
            $ p_atk = 7
            "Escogiste una espada."
        "Lanza.":
            $ p_atk = 5
            $ p_def = 4
            "Escogiste una lanza."
        "Escudo.":
            $ p_atk = 2
            $ p_def = 10
            "Escogiste un escudo."

    p "Bien hecho, ahora ve a luchar con el monstruo."

    $ m_atk = renpy.random.randint(1, 25)
    $ m_def = renpy.random.randint(1, 5)

    jump battle

label battle:
    $ p_def_mod = 0

    menu:
        "Atacar.":
            "¡Atacas al monstruo!"
            $ m_health -= p_atk - m_def
            "¡Haces [p_atk - m_def] puntos de daño!"
        "Defender.":
            "¡Te preparás para el ataque!"
            $ p_def_mod = 5
            "¡Tu defensa aumenta!"
        
    "¡El monstruo ataca!"

    $ p_health -= m_atk - (p_def + p_def_mod)
    "¡Hace [m_atk - (p_def + p_def_mod)] puntos de daño!"

    if (p_health <= 0):
        "Has muerto..."
        jump derrota
    elif (m_health <= 0):
        "¡Mataste al monstruo!"

        $ p_gold = renpy.random.randint(1, 25)

        jump victoria
    else:
        jump battle

label victoria:
    "¡Lo lograste!"
    "Tienes [p_gold] monedas de oro."

    if goblinFriend:
        gb "¡Lo lograste! Sos genial."

    return

label derrota:
    "¡Es el fin!"
    return