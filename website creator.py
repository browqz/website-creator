import webbrowser

couleur_fond = input("Entrez la couleur de fond (Par exemple : #RRGGBB) : ")

couleur_texte = input("Entrez la couleur du texte (Par exemple : #RRGGBB) : ")

taille_police = input("Entrez la taille de la police (en pixels) : ")

texte_page = input("Entrez le texte de la page : ")

url_icone = input("Entrez l'URL de l'icône (favicon) : ")

contenu_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Page personnalisée</title>
    <link rel="icon" type="image/png" href="{url_icone}">
    <style>
        body {{
            background-color: {couleur_fond};
            font-family: Arial, sans-serif;
            color: {couleur_texte};
            font-size: {taille_police}px;
        }}
        #contenu {{
            text-align: center;
            margin-top: 100px;
        }}
    </style>
    <link rel="stylesheet" type="text/css" href="{url_css}">
</head>
<body>
    <div id="contenu">
        <h1>{texte_page}</h1>
        <img src="{url_icone}" alt="Icône personnalisée">
        {contenu_html_supplementaire}
    </div>
</body>
</html>
"""

nom_fichier = "website.html"
with open(nom_fichier, "w", encoding="utf-8") as fichier:
    fichier.write(contenu_html)

webbrowser.open(nom_fichier)

input("Appuyez sur Entrée pour quitter.")