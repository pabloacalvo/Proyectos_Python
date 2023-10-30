from pathlib import Path

guia = Path(Path.home(),"Europa")

# Forma recursiva "**/*.txt"
for txt in Path(guia).glob("**/*.txt"):
    print(txt)


# relative_to Devuelve un nuevo objeto path relacionado con el argumento determinado
guia = Path("Europa","españa","Barcelona","SagradaFamilia.txt")
en_europa = guia.relative_to("Europa")
en_espana = guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espana)

