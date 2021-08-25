
Good = .20
Fair = .15
Bad = .10


bill_total = input("What was your bill total?")
service = input("How was your service?(Good, Fair, or Bad)")

tip_total_good = bill_total * Good
tip_total_fair = bill_total * Fair
tip_total_bad = bill_total * Fair

total_amount_good = tip_total_good + bill_total 
total_amount_fair = tip_total_fair + bill_total
total_amount_bad = tip_total_bad + bill_total

if service == Good:
  print("tip amount: %s" %tip_total_good)
  print("total amount: %s" %total_amount_good)

elif service == Fair:
    print("tip amount: %s" %tip_total_fair)
    print("total amount: %s" %total_amount_fair)
elif service == Bad:
    print("tip amount: %s" %tip_total_bad)
    print("total mount: %s" %total_amount_bad)

else:
  print(service)