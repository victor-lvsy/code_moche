import numpy as IIIII
import json as IIIIIIII
import re as IIIIIIIII
from unidecode import unidecode
from matplotlib import pyplot as IIIIII

from IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII import (
    IIIIIIIIIIIIIIIIIIIIIIIIIII,
    IIIIIIIIIIIIIIIIIIIIIIIIIIII,
    IIIIIIIIIIIIIIIIIIIIIIIIIIIII,
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIII,
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII,
)

with open("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII.txt") as IIIIIIIIII:
    IIIIIII = IIIIIIIIII.read()

IIIIIII = " ".join(IIIIIII.split())

IIIIIII = unidecode(IIIIIII.lower())
IIIIIII = IIIIIIIII.sub(r"[^a-zA-Z0-9\s]+", "", IIIIIII)
IIIIIII = IIIIIIIIIIIIIIIIIIIIIIIIIII(IIIIIII)

IIIIIII = IIIIIIIIIIIIIIIIIIIIIIIIIIII(IIIIIII)

IIIIIII = (
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII" + IIIIIII + "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
)

IIIIIIIIIIIIII = []
for IIIIIIIIIIII, IIIIIIIIIIIII in enumerate(IIIIIII):
    if IIIIIIIIIIIII != "I":
        IIIIIIIIIIIIIII = IIIIIII[IIIIIIIIIIII - 32 : IIIIIIIIIIII + 33]
        IIIIIIIIIIIIIIII = []
        for IIIIIIIIIIIIIIIII in IIIIIIIIIIIIIII:
            if IIIIIIIIIIIIIIIII != "I":
                IIIIIIIIIIIIIIII.append(ord(IIIIIIIIIIIIIIIII) - 96)
        IIIIIIIIIIIIII.append(IIIIIIIIIIIIIIII)

IIIIIIIIIIIIIIIIII = []
for IIIIIIIIIIIIIIIII in IIIIIIIIIIIIII:
    IIIIIIIIIIIIIIIIIIII = 0
    IIIIIIIIIIIIIIIIIIIII = 0
    for IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII in IIIIIIIIIIIIIIIII:
        IIIIIIIIIIIIIIIIIIII = (
            IIIIIIIIIIIIIIIIIIII
            + IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
            * 10**IIIIIIIIIIIIIIIIIIIII
        )
        IIIIIIIIIIIIIIIIIIIII += 1
    IIIIIIIIIIIIIIIIIIII = abs(IIIIIIIIIIIIIIIIIIII // 45261254324214354632135156452)
    while IIIIIIIIIIIIIIIIIIII > 100000000000:
        IIIIIIIIIIIIIIIIIIII = IIIIIIIIIIIIIIIIIIII // 156565
    IIIIIIIIIIIIIIIIII.append(IIIIIIIIIIIIIIIIIIII)

with open(
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII.json", "r"
) as IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII:
    IIIIIIIIIIIIIIIIIIIIII = IIIIIIII.load(IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII)

IIIIIIIIIIIIIIIIIIIIIII = IIIII.zeros([1107, 3]).astype(IIIII.uint8)
for (
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII,
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII,
) in enumerate(IIIIIIIIIIIIIIIIII):
    IIIIIIIIIIIIIIIIIIIIIII[
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII, 0
    ] = IIIIIIIIIIIIIIIIIIIIIIIIIIIII(
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII, IIIIIIIIIIIIIIIIIIIIII
    )
    IIIIIIIIIIIIIIIIIIIIIII[
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII, 1
    ] = IIIIIIIIIIIIIIIIIIIIIIIIIIIIII(
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII, IIIIIIIIIIIIIIIIIIIIII
    )
    IIIIIIIIIIIIIIIIIIIIIII[
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII, 2
    ] = IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII(
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII, IIIIIIIIIIIIIIIIIIIIII
    )
IIIIIIIIIIIIIIIIIIIIIII = IIIII.reshape(IIIIIIIIIIIIIIIIIIIIIII, (41, 27, 3))

IIIIII.imshow(IIIIIIIIIIIIIIIIIIIIIII)
IIIIII.show()
