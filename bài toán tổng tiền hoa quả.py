# tính tổng tiền mua hoa quả và trung bình mỗi người phải trả
i = input("Bạn có mua cam không ? (có/không) ")
if i == "có" :
	a = int(input("Nhập giá tiền 1 kg cam  : "))
	x = float(input("Số lượng cam đã mua (kg) : "))
else :
	a == 0
	x == 0

print("Bạn đã mua " + str(x) + " kg cam với giá " + str(a) + " VND một cân "  )

e = input("Bạn có mua táo không ? (có/không) ")
if e == "có" :
	b = int(input("Nhập giá tiền 1kg táo : "))
	y = float(input("Số lượng táo đã mua (kg) : "))
else :
	b == 0
	y == 0

print("Bạn đã mua " + str(y) + " kg táo với giá " + str(b) + " VND một cân "  )

g = input("Bạn có mua lê không ? (có/không) ")
if g == "có" :
	c = int(input("Nhập giá tiền 1kg lê : "))
	z = float(input("Số lượng lê đã mua (kg) : "))
else :
	c == 0
	z == 0

print("Bạn đã mua " + str(z) + " kg lê với giá " + str(c) + " VND một cân "  )

p = float(input( "Nhóm bạn có bao nhiêu người : " ))

sum = int(a*x+b*y+c*z)
print("Tổng số tiền phải trả là : " + str(sum) + "VND" )
avg = int(sum/p)
print("Mỗi người phải trả : " + str(avg) + "VND" )
