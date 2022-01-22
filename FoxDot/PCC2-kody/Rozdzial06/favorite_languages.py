favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
    }

friends = ['paweł', 'sara']
for name in favorite_languages.keys():
    print(f"Witaj,{name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym"
            " językiem programowania jest {language}!")
