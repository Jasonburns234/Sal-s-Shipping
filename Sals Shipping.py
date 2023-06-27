#Sals Shipping
# Jason burns

weight  = 41.5
cost_ground_premium = 125.00

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight <= 10:
  cost_ground = weight * 4.00 + 20.00
elif weight > 10:
  cost_ground = weight * 4.75 + 20.00


print("Ground shipping Cost: £",cost_ground)
print("Ground shipping Premium FLAT CHARGE:",cost_ground_premium)

#Ground Shipping
if weight <= 2:
  cost_drone = weight * 4.50 + 0.00
elif weight <= 6:
  cost_drone = weight * 9.00 + 0.00
elif weight <= 10:
  cost_drone = weight * 12.00 + 0.00
elif weight > 10:
  cost_drone = weight * 14.25 + 0.00


print("Drone shipping Cost: £",cost_drone)
