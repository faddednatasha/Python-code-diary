Program No. : 25
      Program :  To find profit and loss if selling n cost price is given.

def calculate_profit_loss():
    print("--- Profit and Loss Calculator ---")
    
    try:
        # 1. Get Cost Price and Selling Price from the user
        cp = float(input("Enter the Cost Price (CP): "))
        sp = float(input("Enter the Selling Price (SP): "))

        # 2. Check conditions
        if sp > cp:
            profit = sp - cp
            # Calculate Profit Percentage
            profit_percent = (profit / cp) * 100
            print(f"\nResult: **PROFIT**")
            print(f"Amount: {profit:.2f}")
            print(f"Profit Percentage: {profit_percent:.2f}%")
            
        elif cp > sp:
            loss = cp - sp
            # Calculate Loss Percentage
            loss_percent = (loss / cp) * 100
            print(f"\nResult: **LOSS**")
            print(f"Amount: {loss:.2f}")
            print(f"Loss Percentage: {loss_percent:.2f}%")
            
        else:
            print("\nResult: **No Profit, No Loss** (Breakeven)")

    except ValueError:
        print("Error: Please enter valid numerical values.")
    except ZeroDivisionError:
        print("Error: Cost Price cannot be zero when calculating percentage.")

# Run the program
calculate_profit_loss()
