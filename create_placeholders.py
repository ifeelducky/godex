pages = [
    ("legal.html", "Legal Information"),
    ("playing-the-game.html", "Playing the Game"),
    ("character-creation.html", "Character Creation"),
    ("classes.html", "Classes"),
    ("character-origins.html", "Character Origins"),
    ("feats.html", "Feats"),
    ("equipment.html", "Equipment"),
    ("spells.html", "Spells"),
    ("rules-glossary.html", "Rules Glossary"),
    ("gameplay-toolbox.html", "Gameplay Toolbox"),
    ("magic-items.html", "Magic Items"),
    ("monsters.html", "Monsters"),
    ("monsters-a-z.html", "Monsters A–Z"),
    ("animals.html", "Animals"),
    ("stat-block-index.html", "Index of Stat Blocks"),
]

header = """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>{title}</title>
</head>
<body>
<header>
  <h1>{title}</h1>
</header>
<main>
<p>Content forthcoming.</p>
</main>
<footer>
  <p>
    This work includes material from the
    <em>System Reference Document 5.2.1 (“SRD 5.2.1”)</em> by Wizards of the Coast LLC,
    available at
    <a href='https://www.dndbeyond.com/srd' target='_blank' rel='noopener'>
      dndbeyond.com/srd
    </a>.
    The SRD 5.2.1 is licensed under the
    <a href='https://creativecommons.org/licenses/by/4.0/legalcode' target='_blank' rel='noopener'>
      Creative Commons Attribution 4.0 International License
    </a>.
  </p>
  <p>
    <a href='https://creativecommons.org/licenses/by/4.0/' target='_blank' rel='noopener'>
      <img src='https://mirrors.creativecommons.org/presskit/icons/cc.svg' alt='Creative Commons' height='22' />
      <img src='https://mirrors.creativecommons.org/presskit/icons/by.svg' alt='Attribution' height='22' />
    </a>
  </p>
</footer>
</body>
</html>
"""

for filename, title in pages:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header.format(title=title))
