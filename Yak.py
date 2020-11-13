import numpy as np

class yak:

    name = ''
    age = 0
    sex = ''

def Stockstatus(Herd, T):
    milk = wol = 0; N = len(Herd)
    age = np.array([]); sexes = np.array([]); nextshave = age_lastshave = np.zeros(N)  # Nextshave registers the remaining days until the next shaving
    for yak in Herd:
        age = np.append(age, float(yak.age))
        sexes = np.append(sexes, yak.sex)
    female = np.where(sexes == 'f')[0]

    for i in range(T):
        alive = np.where(age < 10)[0] # To determine the indices of the alive yaks
        if len(alive) == 0:
            return (milk, wol, age, age_lastshave)
        alivefemale = np.intersect1d(alive,female)
        for j in alivefemale:
            milk = milk + 50 - age[j] * 3
        adult = np.where(age >= 1)[0]
        aliveadult = np.intersect1d(alive,adult)
        if len(aliveadult) > 0 and nextshave[aliveadult].min() <= 0:
            mindex = np.where(nextshave == nextshave[aliveadult].min())[0]
            shave = np.intersect1d(mindex,aliveadult) # To select the alive adult yaks that are eligible to be shaven
            wol = wol + len(shave)
            age_lastshave[shave] = age[shave]
            nextshave[shave] = 8 + age[shave]
        else: nextshave[aliveadult] -= 1
        age = age + 0.01

    return(milk, wol, age, age_lastshave)

