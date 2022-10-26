import os

dossier = os.getcwd()
motifs = [  ".FRENCH.720p.AMZN.WEB-DL.DD5.1.H264-FRATERNiTY",
            ".French.WebDL.720p.NF.E-AC3.5.1.x264-French-Stream.lol",
            ".MULTi.1080p.AMZN.WEB.DDP5.1.H264-FRATERNiTY",
            ".FiNAL.FRENCH.1080p.AMZN.WEB.DDP5.1.H264-French-Stream.lol",
            ".FRENCH.1080p.NF.WEB-DL.DDP5.1.x264-FRATERNiTY",
            ".FRENCH.720p.WEB.x264",
            ".FRENCH.1080p.AMZ.WEB.DDP5.1.H264-FRATERNiTY",
            ".FRENCH.1080p.WEB.x264-STRINGERBELL",
            ".FRENCH.720p.WEB.x264-French-Stream.lol",
            ".FRENCH.720p.WEB.x264-STRINGERBELL",
            ".FRENCH.1080p.NF.WEB.H264-F5K",
            ".US",
            " US",
            " 1080p",
            " MULTi",
            " W",
            " B-iT",
            " B-FRAT",
            " RNiTY",
            " DDP5 1",
            " B-NTGY",
            " AMZN",
            "-NTb",
            "-VROOMM",
            "--Stream Re",
            "-N ",
            "BRip",
            " H264",
            " NF",
            " en VF",
            "French",
            "Dvdrip",
            " DVDRiP",
            "-Xvid",
            "XViD",
            ".tell",
            ".DOWLOAD",
            ".FRENCH",
            "FRENCH",
            ".BluRay",
            ".XviD",
            "-XviD",
            "XviD",
            ".BDRip",
            "-BDRip",
            "BDRip",
            "-EXTREME",
            ".EXTREME",
            "EXTREME",
            ".HDRip",
            "-HDRip",
            "HDRip",
            ".TRUEFRENCH",
            "TRUEFRENCH",
            "-Wawacity.ninja",
            ".Lio",
            "Lio",
            "- Film COMPLET en Français (Romance, Comédie)",
            ".REPACK",
            "-REPACK",
            "REPACK",
            ".WwW.ZoNe-TelecharGement.CaM",
            "-WwW.ZoNe-TelecharGement.CaM",
            "WwW.ZoNe-TelecharGement.CaM",
            ".FuN",
            "-FuN",
            "film",
            "Complet",
            "COMPLET",
            "en français",
            "en Français",
            ".Zone-Telechargement.NET",
            ".Zone-Telechargement",
            "Zone-Telechargement",
            "-NiKKi67",
            ".NiKKi67",
            ".WEBRip",
            "-WEBRip",
            ".NF",
            "en Streaming VF",
            "streaning vf",
            "_wWw.Extreme-Down.Plus",
            "_wWw.Extreme-Down.Xyz",
            "_1",
            "_2",
            ".AC3-THC",
            "-STVFRV",
            ".MD",
            ".HC",
            ".x264",
            " x264",
            " X264",
            ".WEB-DL",
            ".720p",
            "Wiflix - ",
            "Film entier",
            ".AC3-THC",
            "french streaming",
            "en streaming",
            "streaming",
            ".HD",
            " HD",
            ".WwW.Torrent9.tv",
            ".XviD-PREUMS",
            "illimité complet gratuit",
            "-GZR",
            "film romantique",
            "sur Wiflix",
            ".XviD-GLUPS",
            "[ www.Cpasbien.pw ] ",
            " [OxTorrent.cc]",
            "[ OxTorrent cc ] ",
            "[ OxTorrent com ] ",
            "[ OxTorrent cx ] ",
            "[ OxTorrent io ] ",
            "[ OxTorrent nz ] ",
            "-Ox",
            "AAC-NIKOo",
            " [OxTorrent.ph]",
            "[ OxTorrent ph ] ",
            "[ OxTorrent sh ] ",
            "[ OxTorrent tv ] ",
            "[ OxTorrent ws ] ",
            "[ Torrent9 cz ] ",
            "[ Torrent9 info ] ",
            "[ Torrent9 red ] ",
            "[ Torrent9 tv ] ",
            "[ Torrent911 com ] ",
            "FANSUB",
            ".UNRATED",
            ".XviD-FUZION",
            "XviD-FUZION",
            "vf",
            ".H264",
            ".AAC-RARBG",
            "Film",
            "en Streaming",
            "Streaming",
            "-FUZION",
            "  ",
            "-PREUMS",
            "RiP",
            "télécharger",
            "regarder",
            "Regarder",
            "BRRip",
            "-ACOOL",
            "-QCP",
            "(Source)",
            "-GLUPS",
            "IMAX",
            "AC3",
            "FILM ENTIER",
            "VOSTFR",
            ".ZT",
            " ZT",
            ".ZL",
            " ZL"
        ]

annee = ["2010","2011","2012","2013","2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

extensions = [" mp4", " MP4", " avi", "AVI", " mkv", "MKV", " py", " ts", " TS", " txt"]


def renomage():
    # Remplacer les motifs
    for i in motifs:
        for filename in os.listdir(dossier):
            if i in filename:
                newname = "".join(filename.split(i))
                os.rename(filename, newname)


    # # Mettre les dates entre parenthese
    # for j in annee:
    #     for filename in os.listdir(dossier):
    #         if j in filename:
    #             j_ = "(" + j + ")"
    #             newname_ = "".join(filename.replace(j, j_))
    #             os.rename(filename, newname_)


    # Remplacer les points par espace
    for filename in os.listdir(dossier):
        newname_1 = "".join(filename.replace(".", " "))
        os.rename(filename, newname_1)


    # Remplacer les _ par espace
    for filename in os.listdir(dossier):
        newname_2 = "".join(filename.replace("_", " "))
        os.rename(filename, newname_2)


    # Remplacer
    for filename in os.listdir(dossier):
        newname_2 = "".join(filename.replace("S0", "- Saison "))
        os.rename(filename, newname_2)

    # Remplacer
    for filename in os.listdir(dossier):
        newname_2 = "".join(filename.replace("s0", "- Saison "))
        os.rename(filename, newname_2)
    

    # Remplacer
    for filename in os.listdir(dossier):
        newname_2 = "".join(filename.replace("E", " - Episode "))
        os.rename(filename, newname_2)


    # Remplacer
    for filename in os.listdir(dossier):
        newname_2 = "".join(filename.replace("e0", "- Episode "))
        os.rename(filename, newname_2)

    # Remplacer
    for filename in os.listdir(dossier):
        newname_2 = "".join(filename.replace("épisode", "- Episode"))
        os.rename(filename, newname_2)


    # Affecter les extensions
    for k in extensions:
        for filename in os.listdir(dossier):
            if k in filename:
                k_ = "." + k[1:]
                newname__ = "".join(filename.replace(k, k_))
                os.rename(filename, newname__)


    for filename in os.listdir(dossier):
        newname_3 = "".join(filename.replace(" .", "."))
        os.rename(filename, newname_3)


print("Choisissez votre choix")
print("   a - Ajouter des motifs")
print("   b - Ajouter une annee")
print("   c - Ajouter des extensions")
print("   d - proceder au renomage des fichiers")
print("   x - pour quitter")

while 1:
    choix = input("\n Entrer votre choix : ")

    if choix == "a":
        _motifs = input("Entrer le nouveau motif : ")
        motifs.append(_motifs)
        
    elif choix == "b":
        _annee = input("Entrer le nouveau annee : ")
        annee.append(_annee)

    elif choix == "bb":
        print(annee)

    elif choix == "c":
        _extensions = input("Entrer le nouveau extension : ")
        extensions.append(_extensions)

    elif choix == "cc":
        print(extensions)

    elif choix == "d":
        renomage()

    elif choix == "x":
        break





# .rest.gf.fall.tell.go
