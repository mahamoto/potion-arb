from brownie import network
from degenbot import Erc20Token
from degenbot.liquiditypool.liquidity_pool import LiquidityPool

network.connect("polygon-main")

AMOUNT = 1

AURUM = Erc20Token("0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23")
NEWT = Erc20Token("0x1346FdB62241e238Be9F84A2FC364c0657757015")
WEED = Erc20Token("0x06F34105B7DfedC95125348A8349BdA209928730")
MHP = Erc20Token("0x919B22450c38108bB624c4c72B085Cd7C0442b80")
BHP = Erc20Token("0xe3D73635CF43551d245A551C8Cf909A8475299bb")


AURUM_NEWT = LiquidityPool("0x1Fec149e363b9c3282C2C3509f171cE2Ac77dd27", [AURUM, NEWT], "AURUM-NEWT")
AURUM_WEED = LiquidityPool("0x89176Dc7b5AEBd0D5eFfFc2592e2068266F4b783", [AURUM, WEED], "AURUM-WEED")

#Low Liquidity (20k Aurum)
AURUM_MHP_POOL = LiquidityPool("0xd7ed09F5766b7fa19977ca547BeB7cAA7B3f1A12", [AURUM, MHP], name="AURUM-MHP")

#Super Low Liquidity (1,5k AURUM)
AURUM_BHP_POOL = LiquidityPool("0x974451fbBe641e2C87dA57411269f9E513d945b6", [AURUM, BHP], "AURUM-BHP")


aurum_for_weed = AURUM_WEED.calculate_tokens_in_from_tokens_out(AURUM, AMOUNT * 3) 
aurum_for_newt = AURUM_NEWT.calculate_tokens_in_from_tokens_out(AURUM, AMOUNT * 2)  
cost = aurum_for_weed + aurum_for_newt + 3e18* AMOUNT
aurum_for_mhp = AURUM_MHP_POOL.calculate_tokens_out_from_tokens_in(MHP, AMOUNT)

print(f"""
~~~ Newt + Weed -> Minor Health Potion ~~~
calculation for {AMOUNT} MHP:
input:      {cost/1e18} Au
out:        {aurum_for_mhp/1e18} Au
profit:     {(aurum_for_mhp-cost)/1e18} Au
""")

aurum_for_weed = AURUM_WEED.calculate_tokens_in_from_tokens_out(AURUM, AMOUNT * 3*3) 
aurum_for_newt = AURUM_NEWT.calculate_tokens_in_from_tokens_out(AURUM, AMOUNT * 2*3)  
cost = aurum_for_weed + aurum_for_newt + 4*3e18* AMOUNT
aurum_for_bhp = AURUM_BHP_POOL.calculate_tokens_out_from_tokens_in(BHP, AMOUNT)

print(f"""
~~~ Newt + Weed -> Basic Health Potion ~~~
calculation for {AMOUNT} MHP:
input:      {cost/1e18} Au
out:        {aurum_for_bhp/1e18} Au
profit:     {(aurum_for_bhp-cost)/1e18} Au
""")





aurum_for_bhp = AURUM_BHP_POOL.calculate_tokens_out_from_tokens_in(BHP, AMOUNT)
aurum_for_mhp = AURUM_MHP_POOL.calculate_tokens_in_from_tokens_out(AURUM, 3*AMOUNT)
aurum_in = aurum_for_mhp + 3e18 * AMOUNT
profit = aurum_for_bhp - aurum_in

print(f"""~~~ Minor Health Potion -> Basic Health Potion ~~~
calculation for {AMOUNT} BHP:
input:      {aurum_in/1e18} Au
out:        {aurum_for_bhp/1e18} Au
profit:     {profit/1e18} Au
""")