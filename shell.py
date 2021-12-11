import aura

while True:
    text = input("aura > ")
    result, error = aura.run(text)

    if error: print(error.as_string())
    else: print(result)