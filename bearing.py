
# den symperilamvanetai h ekkentrothta logw kataskeyhs
# epishs ayth h ekkentrothta mporei na prosdidei h na afairei apo ekeinh ths fortishs!

from math import sin, tan, atan, pi, e
from factors import table_A5

# ekkentrotita ths fortishs
def calc_e(Mk, Vk):
    return Mk/Vk

# lojotita fortisis ws pros tin katakoryfo
def calc_theta(Hk, Vk):
    return (180*atan(Hk/Vk))/pi

# apomeiwmenes diastaseis pediloy
def calc_rDims(B, L, eB, eL):
    rB = B-2*eB
    rL = L-2*eL
    rA = rB*rL    
    return rB, rL, rA

# ypologizei to m
# na to kanw ligo pio omorfo
def calc_m(rB, rL, H_B, H_L):
    if H_L==0 and H_B==0:
        return 0
    elif H_L==0:
        return (2+(rB/rL))/(1+(rB/rL))
    elif H_B==0:
        return (2+(rL/rB))/(1+(rL/rB))
    else:
        mL = (2+(rL/rB))/(1+(rL/rB))
        mB = (2+(rB/rL))/(1+(rB/rL))
        m = mL*(H_L/H_B)**2 + mB*(H_B/H_L)**2
        return m

def calc_N(phi):
    Nq = (e**(pi*tan((pi*phi)/180)))*((tan(pi/4+(pi*phi)/360))**2)
    Nc = (Nq-1)/tan((pi*phi)/180)
    Ng = 2*(Nq-1)*tan((pi*phi)/180)
    return Nq, Nc, Ng


def calc_s(Br, Lr, phi, Nq):
    sq = 1 + (Br/Lr)*sin((pi*phi)/180)
    sg = 1-0.3*(Br/Lr)
    sc = (sq*Nq-1)/(Nq-1)
    return sq, sg, sc


def calc_pu(puT, Br, Lr, theta, A, phi, m, Nc, c, sc, sq, sg, Nq, Ng, g1, g2, q, D):
    V = puT*Br*Lr
    H = V*tan((pi*theta)/180)
    iq = (1-H*(V+A*c*(1/tan((pi*phi)/180))))**m
    ig = (1-H*(V+A*c*(1/tan((pi*phi)/180))))**(m+1)
    ic = iq - (1-iq)/(Nc*tan((pi*phi)/180))
    pu = c*Nc*sc*ic + (q+g1*D)*Nq*sq*iq + 0.5*g2*Br*Ng*sg*ig

    while abs(pu-puT)>0.1:
        puT = puT-0.1
        V = puT*Br*Lr
        H = V*tan((pi*theta)/180)
        iq = (1-H/(V+A*c*(1/tan((pi*phi)/180))))**m
        ig = (1-H/(V+A*c*(1/tan((pi*phi)/180))))**(m+1)
        ic = iq - (1-iq)/(Nc*tan((pi*phi)/180))
        pu = c*Nc*sc*ic + (q+g1*D)*Nq*sq*iq + 0.5*g2*Br*Ng*sg*ig

    return pu


def check_bearing(B, L, D, g1, g2, phi, c, Gk, Qk, H_BGk, H_BQk, H_LGk, H_LQk, M_BGk, M_LGk, M_BQk, M_LQk, qk, gG, gQ):

    Ed = gG*Gk + gQ*Qk
    # HBd = gG*H_BGk + gQ*H_BQk
    # HLd = gG*H_LGk + gQ*H_LQk
    # MBd = gG*M_BGk + gQ*M_BQk
    # MLd = gG*M_LGk + gQ*M_LQk

    puT = Gk+Qk
    eB = calc_e(M_BGk+M_BQk, Gk+Qk)
    eL = calc_e(M_LGk+M_LQk, Gk+Qk)
    rB, rL, rA = calc_rDims(B, L, eB, eL)
    thetaB = calc_theta(H_BGk+H_BQk, Gk+Qk)
    thetaL = calc_theta(H_LGk+H_LQk, Gk+Qk)
    Nq, Nc, Ng = calc_N(phi)
    sq, sg, sc = calc_s(rB, rL, phi, Nq)

    m = calc_m(rB, rL, H_BGk+H_BQk, H_LGk+H_LQk)

    pu = calc_pu(puT, rB, rL, thetaB, rA, phi, m, Nc, c, sc, sq, sg, Nq, Ng, g1, g2, qk, D)

    Rk = pu*rB*rL

    Rd = Rk/table_A5["grv_R2"]
    FS = Rk/(Gk+Qk)
    # ta 1.35 kai 1.5 einai ta gG gQ?
    FSmin = (1.35/1.5)*table_A5["grv_R2"]

    if Ed > Rd:
        print("redesign!!!")
    print("Ed:   , Rd:    ")
    print("FS:   , FSmin:   ")
    print(FS, FSmin, Rd, Ed)
    

