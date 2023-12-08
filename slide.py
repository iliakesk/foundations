# se oti afora to memomwmeno themelio to arxeio einai swsto. parola ayta, den einai plhres. na ton toixo antisthrijhs
# kai ton elegxo se olisthish gia to symplhrwsw


from math import tan, pi
from factors import table_A5, table_A13


def check_slide(H_BGk, H_BQk, gG, gQ, delta, Gk, Qk, Rp):

    HBd = gG*H_BGk + gQ*H_BQk #ti ginetai an exv kai pros tin alli kateuthinsi? elegxw jexvrista?
    Vk = Gk+Qk

    Hd = HBd
    Rd = (Vk*tan((pi*delta)/180))/table_A5["grh_R2"]
    Rpd = Rp/table_A13["gre_R2"]
    
    FS = (Vk*tan((pi*delta)/180))/(H_BGk + H_BQk)
    
    FSmin = (1.35/1.5)*table_A5["grh_R2"]

    if Hd > Rd + Rpd:
        print("redesign!!!")
    print("Hd:   , Rd:    , Rpd:     ")
    print("FS:   , FSmin:   ")
    print(FS, FSmin, Rd, Hd)