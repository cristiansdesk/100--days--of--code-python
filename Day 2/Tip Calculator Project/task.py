print("welcome")
bill = float(input("Enter bill: $"))
tip = int(input("how much to tip 10 12 15: "))
guest_split = int(input("how many split: "))




tip_calc = tip / 100
total_bill = (tip_calc * bill) + bill
guest_bill = total_bill / guest_split
print(f"Each gust bill is: ${guest_bill}")