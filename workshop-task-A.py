quantity = int(input("จำนวนปืนที่รับมาขาย (กระบอก):"))
cost_price = float(input("ต้นทุนของปืนที่รับมา (บาท/กระบอก:)"))
sell_price = float(input("ราคาที่จะนำไปขายต่อ (บาท/กระบอก):"))
team_member = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน (คน):"))
total_cost = cost_price*quantity
total_sell = sell_price*quantity
profit = total_sell-total_cost
boss_profit = profit*0.2
member_profit = (profit-boss_profit)/team_member

print("ต้นทุนทั้งหมด",total_cost,"บาท")
print("มีรายได้รวม",total_sell,"บาท")
print("กำไรสุทธิ",profit,"บาท")
print("เป็นเงินของบอส",boss_profit,"บาท")
print(f"มีลูกน้องเข้าร่วม{team_member}คน และได้รับคนละ{member_profit}")
