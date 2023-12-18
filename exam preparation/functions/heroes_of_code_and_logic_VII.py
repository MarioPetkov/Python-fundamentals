heroes_number = int(input())
max_hp = 100
max_mp = 200
heroes = {}
for hero in range(heroes_number):
    name, hp, mp = input().split(' ')
    hp, mp = int(hp), int(mp)
    if hp > max_hp and mp > max_mp:
        heroes[name] = {'hp': max_hp, 'mp': max_mp}
    else:
        heroes[name] = {'hp': hp, 'mp': mp}
command = input().split(' - ')
while command[0] != 'End':
    
    if command[0] == 'CastSpell':
        hero_name,mp_needed,spell_name = command[1], int(command[2]), command[3]
        if heroes[hero_name]['mp'] >= mp_needed:
            heroes[hero_name]['mp'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        heroes[hero_name]['hp']  -= damage
        if heroes[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        amount_recovered = max_mp - heroes[hero_name]['mp']
        heroes[hero_name]['mp'] += amount
        if heroes[hero_name]['mp'] >= max_mp:
            heroes[hero_name]['mp'] = max_mp
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        amount_recovered = max_hp - heroes[hero_name]['hp']
        heroes[hero_name]['hp'] += amount
        if heroes[hero_name]['hp'] >= max_hp:
            
            heroes[hero_name]['hp'] = max_hp
            print(f"{hero_name} healed for {amount_recovered} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")
    command = input().split(' - ')
for hero_name in heroes.keys():
    print(hero_name)
    print(f'  HP: {heroes[hero_name]["hp"]}')
    print(f'  MP: {heroes[hero_name]["mp"]}')

