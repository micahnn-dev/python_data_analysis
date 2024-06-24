# Initialiser les variables
player_1 = input("Entrez le nom du 1er joueur: ").strip().capitalize()
player_1_pv = input("Entrez le nombre de PV du 1er joueur: ").strip()

print()

player_2 = input("Entrez le nom du 2ème joueur: ").strip().capitalize()
player_2_pv = input("Entrez le nombre de PV du 1er joueur: ").strip()

print()

# Afficher les valeurs des variables
length_of_entered_strings = len(player_1 + player_1_pv + player_2 + player_2_pv)
length_of_entered_strings += 25
print('+' * length_of_entered_strings)
print(f'+ {player_1} ({int(player_1_pv)} PV) affronte {player_2} {int(player_2_pv)} (PV) +')
print('+' * length_of_entered_strings)

player_2_pv = int(player_2_pv)
player_1_pv = int(player_1_pv)

print()

# Début de l'affrontement
attaque_1 = int(input(player_1 + ', combien de PV infligez-vous à ' + player_2 + ' ? '))

print()

player_2_pv -= attaque_1
msg1 = player_1 + ' attaque ' + player_2 + ' qui perd ' + str(attaque_1) + ' PV'
msg2 = player_2 + ' a maintenant ' + str(player_2_pv) + ' PV'
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print('+' * (max_size+4))
print('+', msg1, '+')
print('+', msg2, '+')
print('+' * (max_size+4))

print()

attaque_2 = int(input(player_2 + ', combien de PV infligez-vous à ' + player_1 + ' ? '))

print()

player_1_pv -= attaque_2
msg1 = player_2 + ' attaque ' + player_1 + ' qui perd ' + str(attaque_2) + ' PV'
msg2 = player_1 + ' a maintenant ' + str(player_1_pv) + ' PV'
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print('+' * (max_size+4))
print('+', msg1, '+')
print('+', msg2, '+')
print('+' * (max_size+4))

print()

msg1 = 'Résulat du combat :'
msg2 = player_1 + ' a ' + str(player_1_pv) + ' PV'
msg3 = player_2 + ' a ' + str(player_2_pv) + ' PV'
max_size = max(len(msg1), len(msg2), len(msg3))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
msg3 += ' ' * (max_size - len(msg3))
print('+' * (max_size+4))
print('+', msg1, '+')
print('+', msg2, '+')
print('+', msg3, '+')
print('+' * (max_size+4))
