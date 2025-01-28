from random import choice

heavy_greataxe = ['Battleaxe','Halberd','Gran sudaruska','Adretian Axe','Canorian Axe','Iron Birch','Evanspear Hand Axe','Night Axe','Master Hawk Hand Axe','Relic Axe','Quartztone Pickaxe','Skyreap Blade','Enforcer Axe','Alloyec Canorian Axe','Alloyed Halberd','Alloyed Adretian Axe','Pale Briar','Chorus of Agonies']
heavy_greatsword = ['Avenger','Zweihander','Ysley Pyre keeper','Markor Inheritor','Crescent Cleaver','Darksteel Greatsword','Inquisitor Greadsword','Crypt Blade','Kyrsieger','Hailbreaker','The Long Tong of The Law','Wretched Mawblades','First Light','Alloyed Zweihander','Alloyed Crescent Cleaver','Darkalloy Greatsword','Alloyed Inheritor','Kyrscleave','Railblade','Fractine','Enforcer Blade']
heavy_greathammer = ['Steel Maul','Forge Greathammer','Rockmaller','Great Maul','Putrid Edenstaff','Alloyed Steel Maul','Alloyed Forge Greathammer','Pale Morning','Petra Anchor','Sovereign Punishment','Stoneheart','Enforcer Hammer','Kanabo','Hivelord Hubris']
medium_sword = ['Sword','Dormant Splinter','Messer','Falchion','Scimitar','Katana','Curved Blade of Winds','Worshipper Longsword','Officer Saber','Vigil Longsword','Champion Sword','Cavalry Saber','Ignition Deepcrusher','Shotel','Warden Ceremonial Sword','Razor Cutlass','Forgotten Gladius','Fondant Splitter','Serpent Edge','Hallowcleave','Alloyed Messer','Alloyed Falchion','Alloyed Vigil Longsword','Alloyed Shotel','Alloyed Katana','Kyrsblade','Eye of Malice','Umbrite Witherblade','Purple Cloud','Soulthorn','Shattered Katana','Nocturne','Hero blade of fire','Hero blade of ice','Hero blade of shadow','Hero blade of lightning','Hero blade of wind','Wyrmtooth']
medium_spears = ['Irontusk','Iron Spear','Gremorian Longspear','Ritual Spear','Acheron Warspear','Imperial Staff','Trident Spear','Kyrswynter','Serrated Warspear','Bloodtide Trident','Alloyed Longspear','Rifle Spear','Imperator Edge','Alloyed Trident Spear','True Seraph Spear','Kyrsglaive']
medium_clubs = ['Mace','Toothed Club','Pleeksty Inferno','Ignition Deepcrusher','Morning Star','Sacred Hammer','The Pastry Paster','Pernach']
medium_twinblades = ['Iron Twinblade','Scalesplitter','Crescendo','Alloyed Scalesplitter','Death Reverie']
medium_rifles = ['Summer rifle','Rosen Hellflame','Stormseye','Rosen Peacemaker','Iron Blunderbuss']
light_daggers = ['Stiletto','Gilded Knife','Silver Dagger','Canor Fang','Whaling Knife','Champion Dagger','Central Dirk','Tanto','Nemit Sickle','Flareblood Kamas','The Flippers of Fate','Krulian Knife','Spectral Grasp','Kyrsedge','Alloyed Whaling Knife','Alloyed Tanto','Cerulean Thread']
light_fists = ['Anklets of Alsin','Jus Karita','Legion Kata','Way of Navae','Fang and Coil','Iron Cestus','Wraithclaw','Legion Cestus','Coral Cestus','Flamekeeper Cestus','Drakemaw Gauntlets','Bloodalloy Cestus','Gaunts of Enmity','Light Final Toll','Vortex Echo']
light_flintlocks = ['Silversix','Flintlock','Dawnshot','Iron Requiem','Repeater','Dragoon','Rosen Roscoe','Alloyed Dawnshot','Aranea?']
light_Rapiers = ['Quickfang','Apprentice Rapier','Inquisitor Thorn','Deepspindle','Crucible Rapier','Golden Swordfish','Skullpiercer','Kyrstreza']

peso_da_arma = str(input('Olá, Escolha entre:\n[1]: Heavy\n[2]: Medium\n[3]: Light\n')).strip().capitalize()
tipo_da_arma = ''

while 'Heavy' not in peso_da_arma or 'Medium' not in peso_da_arma or 'Light' not in peso_da_arma:
    peso_da_arma = str(input('Você digitou errado! Escolha entre: [Heavy, Medium, Light] ')).strip().capitalize()

if peso_da_arma == 'Heavy':
    tipo_da_arma = str(input('Qual tipo deseja? Escolha entre:\n[1]: Great axe\n[2]: Great sword\n[3]: Great hammer\n[É Necessário digitar o nome Corretamente] ')).strip().capitalize()
    
    while tipo_da_arma not in 'Great axe' or tipo_da_arma not in 'Great sword' or tipo_da_arma not in 'Great hammer':
        tipo_da_arma = str(input('Você digitou errado! Escolha entre:\n[1]: Great axe\n[2]: Great sword\n[3]: Great hammer\n[É Necessário digitar o nome Corretamente] ')).strip().capitalize()

    if tipo_da_arma == 'Great axe':
        print(f'Parabéns! A Arma escolhida foi: {choice(heavy_greataxe)}')
    elif tipo_da_arma == 'Great sword':
        print(f'Parabéns! A Arma escolhida foi: {choice(heavy_greatsword)}')
    elif tipo_da_arma == 'Great hammer':
        print(f'Parabéns! A Arma escolhida foi: {choice(heavy_greathammer)}')

elif peso_da_arma == 'Medium':
    tipo_da_arma = str(input('Qual tipo deseja? Digite:\n[1]: Sword\n[2]: Spear\n[3]: Club\n[4]: Twinblade\n[5]: Rifle\n[É Necessário digitar o nome Corretamente] ')).strip().capitalize()
    
    while tipo_da_arma not in 'Sword' or tipo_da_arma not in 'Spear' or tipo_da_arma not in 'Club' or tipo_da_arma not in 'Twinblade' or tipo_da_arma not in 'Rifle':
         tipo_da_arma = str(input('Você digitou errado! Escolha entre:\n[1]: Sword\n[2]: Spear\n[3]: Club\n[4]: Twinblade\n[5]: Rifle\n[É Necessário digitar o nome Corretamente] ')).strip().capitalize()
    
    if tipo_da_arma == 'Sword':
        print(f'Parabéns! A Arma escolhida foi: {choice(medium_sword)}')
    elif tipo_da_arma == 'Spear':
        print(f'Parabéns! A Arma escolhida foi: {choice(medium_spears)}')
    elif tipo_da_arma == 'Club':
        print(f'Parabéns! A Arma escolhida foi: {choice(medium_clubs)}')
    elif tipo_da_arma == 'Twinblade':
        print(f'Parabéns! A Arma escolhida foi: {choice(medium_twinblades)}')
    elif tipo_da_arma == 'Rifle':
        print(f'Parabéns! A Arma escolhida foi: {choice(medium_rifles)}')

elif peso_da_arma == 'Light':
    tipo_da_arma = str(input('Qual tipo deseja? Digite:\n[1]: Daggers\n[2]: Fist\n[3]: Flintlock\n[4]: Rapier\n[É Necessário digitar o nome Corretamente] ')).strip().capitalize()
    
    while tipo_da_arma not in 'Daggers' or tipo_da_arma not in 'Fist' or tipo_da_arma not in 'Flintlock' or tipo_da_arma not in 'Rapier':
         tipo_da_arma = str(input('Você digitou errado! Escolha entre:\n[1]: Daggers\n[2]: Fist\n[3]: Flintlock\n[4]: Rapier\n[É Necessário digitar o nome Corretamente] ')).strip().capitalize()
        
    if tipo_da_arma == 'Daggers':
        print(f'Parabéns! A Arma escolhida foi: {choice(light_daggers)}')
    elif tipo_da_arma == 'Fist':
        print(f'Parabéns! A Arma escolhida foi: {choice(light_fists)}')
    elif tipo_da_arma == 'Flintlock':
        print(f'Parabéns! A Arma escolhida foi: {choice(light_flintlocks)}')
    elif tipo_da_arma == 'Rapier':
        print(f'Parabéns! A Arma escolhida foi: {choice(light_Rapiers)}')
