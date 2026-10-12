from dic import data

def Price(ticker):
    ticker = ticker.upper() 
    
    if ticker in data:
        return data[ticker]["Price"]
    else:
        return "Ticker not found"

def Market_Cap(highest_budget):
    highest_market_cap = 0

    for key, value in data.items():
        if value["Market Cap"] > highest_market_cap:
            highest_market_cap = value["Market Cap"]
            highest_ticker = key
            
    print("Highest Market Cap")
    print("Ticker:", highest_ticker)
    print("Company:", data[highest_ticker]["Name"])
    print("Market Cap:", highest_market_cap)
    print("-"*50)
    print()

Market_Cap(highest_budget)


def week_lowest():
    week_lowest = float("inf")   
    

    for key, value in data.items():
        if value["52 Week Low"] < week_lowest:
            week_lowest = value["52 Week Low"]
            ticker = key
    
    print("Week Lowest considering 52 weeks ")

    print("Ticker:", ticker)
    print("Company:", data[ticker]["Name"])
    print("52 Week Low:", week_lowest)
    print("-"*50)
    print()
    
week_lowest()



def week_highest():
    week_highest = float("-inf")   

    for key, value in data.items():
        if value["52 Week High"] > week_highest:
            week_highest = value["52 Week High"]
            ticker = key

    print("Week Highest considering 52 weeks")
    print("Ticker:", ticker)
    print("Company:", data[ticker]["Name"])
    print("52 Week High:", week_highest)
    print("-" * 50)

week_highest()
            


    
