from autocorrect import Speller

corrector = Speller(lang='es')

def corregir_palabra(palabra: str):
    if not corrector(palabra) == palabra:
        return corrector(palabra)
    else:
        return palabra

print(corregir_palabra('dia'))