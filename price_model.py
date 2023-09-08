# Hashrate can be specifically user-defined.
# - ZKPool can use num_proofs per hour as hashrate.
# - This can be easily calculated by each prover's proof time.
current_hashrate: int = 0 # Current total proving speed/hour in the pool.
total_hashrate_moving_average: int = 0 # Total proving speed/hour in last MA_DURATION.

# Ratio shows the supply/demand ratio, which ideally should be 1.
# ratio: float = current_hashrate / total_hashrate_moving_average

# Price can be calculated through a bonding curve.
# E.g. we can use a constant product function
# price * ratio = a
# -> price = a * total_hashrate_moving_average / current_hashrate
# Add a small offset to prevent zero devidend and cold start.
# -> price = a * (total_hashrate_moving_average + offset_1) / (current_hashrate + offset2)

# const varibles
MA_DURATION: int = 60     # Moving average duration for calculating total hashrate, minutes.
COEFFICIENT: int = 3.5    # Coefficient. This is similar to price of one task.
OFFSET_1: int = 1         # A small offset to help cold start.
OFFSET_2: int = 0.001     # A small offset to prevent zero devidend.

# # get total used capacity moving average in last MA_DURATION
# def get_cap() -> int:
#     return 50

# Get current price.
def get_price():
    return COEFFICIENT * (total_hashrate_moving_average + OFFSET_1) / (current_hashrate + OFFSET_2)
    

if __name__ == "__main__":
    
    # CASE 1: cold start of ZKPool.
    current_hashrate = 1 # Assume a prover with hashrate 1 is our first prover.
    total_hashrate_moving_average = 0 # No previous hashrate info.
    print(f"CASE 1: current_hashrate = 1, total_hashrate_moving_average = 0, the price is {get_price()}")
    
    # CASE 2: the demand is more than supply.
    current_hashrate = 1100
    total_hashrate_moving_average = 1200
    print(f"CASE 2: current_hashrate = 1100, total_hashrate_moving_average = 1200, the price is {get_price()}")

    # CASE 3: the demand is equal to supply.
    current_hashrate = 1300
    total_hashrate_moving_average = 1300
    print(f"CASE 2: current_hashrate = 1300, total_hashrate_moving_average = 1300, the price is {get_price()}")

    # CASE 4: the demand is more than supply.
    current_hashrate = 1300
    total_hashrate_moving_average = 1100
    print(f"CASE 2: current_hashrate = 1300, total_hashrate_moving_average = 1100, the price is {get_price()}")

    # CASE 1: current_hashrate = 1, total_hashrate_moving_average = 0, the price is 3.4965034965034967
    # CASE 2: current_hashrate = 1100, total_hashrate_moving_average = 1200, the price is 3.8213601623998525
    # CASE 2: current_hashrate = 1300, total_hashrate_moving_average = 1300, the price is 3.502689613315682
    # CASE 2: current_hashrate = 1300, total_hashrate_moving_average = 1100, the price is 2.9642284890550084