B = 3
L = 4
D = 1

g1 = 20
g2 = 20
phi = 28
c = 10

Gk = 1800
Qk = 350
H_BGk = 360
H_BQk = 70
H_LGk = 0
H_LQk = 0
M_BGk = 1080
M_BQk = 210
M_LGk = 0
M_LQk = 0
qk = 0

gG = 1.35
gQ = 1.5

#einai h antistash tvn gaiwn poy symvallei sthn olisthisi
# leei o EC oti einai Rp/γRe. Ti einai ta symvola?
Rpd = 0 
delta = phi
Rp = 0


# kapoia apo ta parapanv dedomena einai epejergasmena px oi katakoryfew draseis symperilamvanoyn kai ta varh twn 
# themelivn i tvn toixvn varythtas. tha prepei na apofasisw poy akrivws tha ginetai auth h epejergasia, sto paron 
# arxeio i se prohgoumeno?

from bearing import check_bearing
from slide import check_slide


check_bearing(B, L, D, g1, g2, phi, c, Gk, Qk, H_BGk, H_BQk, H_LGk, H_LQk, M_BGk, M_LGk, M_BQk, M_LQk, qk, gG, gQ)

check_slide(H_BGk, H_BQk, gG, gQ, delta, Gk, Qk, Rp)