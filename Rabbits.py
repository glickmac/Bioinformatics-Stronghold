def rabbit(old, young, reproduction_rate, months):
    result = 0
    if months == 1:
        result = young
    else:
        result = rabbit(young, old * reproduction_rate + young, reproduction_rate, months - 1)

    return result

print rabbit(0, 1, 3, 35)
