Product = ["Leather_Wallet","Umbrella","Cigarette","Honey"]
Unit_price = [1100,900,200,100]
GST = [18,12,28,0]
Quantity = [1,4,3,2]


dis_lis = []

dis_price = (Unit_price[0]-((5/100)*Unit_price[0]))
dis_lis.append(dis_price)
dis_price = (Unit_price[1]-((5/100)*Unit_price[1]))
dis_lis.append(dis_price)
dis_lis.append(Unit_price[2])
dis_lis.append(Unit_price[3])

Gst_amt_Lw = ((GST[0]/100)*dis_lis[0])*Quantity[0]
Gst_amt_Um = ((GST[1]/100)*dis_lis[1])*Quantity[1]
Gst_amt_ci = ((GST[2]/100)*dis_lis[2])*Quantity[2]
Gst_amt_ho = ((GST[3]/100)*dis_lis[3])*Quantity[3]

Gst_amt = []

Gst_amt.append(Gst_amt_Lw)
Gst_amt.append(Gst_amt_Um)
Gst_amt.append(Gst_amt_ci)
Gst_amt.append(Gst_amt_ho)


total_lw =  (((GST[0]/100)*dis_lis[0])+dis_lis[0])*Quantity[0]
total_Um =  (((GST[1]/100)*dis_lis[1])+dis_lis[1])*Quantity[1]
total_ci =  (((GST[2]/100)*dis_lis[2])+dis_lis[2])*Quantity[2]
total_ho =  (((GST[3]/100)*dis_lis[3])+dis_lis[3])*Quantity[3]

total_amt = []

total_amt.append(total_lw)
total_amt.append(total_Um)
total_amt.append(total_ci)
total_amt.append(total_ho)

gst_max = 0
for i in Gst_amt:
    if i>gst_max:
        gst_max = i


total_amt_to_be_paid= 0
for i in total_amt:
    total_amt_to_be_paid = total_amt_to_be_paid+i

print("The product for which we paid maximum Gst amount is:",Product[1],"and the maximum GST amount paid is:",gst_max)
print("Total amount to be paid to the shop-keeper is: \n",total_amt_to_be_paid)