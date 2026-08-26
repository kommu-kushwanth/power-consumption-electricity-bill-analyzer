print("=" * 50)
print("POWER CONSUMPTION & ELECTRICITY BILL")
print("ANALYZER")
print("=" * 50)

appliances = []

while True:

    print("\n---------- MAIN MENU ----------")
    print("1. Add Appliance")
    print("2. View Appliances")
    print("3. Calculate Energy Consumption")
    print("4. Calculate Electricity Bill")
    print("5. Show Power Consumption Report")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    # 1. Add Appliance
    if choice == 1:
        name = input("\nEnter appliance name: ")
        power = float(input("Enter power rating (in Watts): "))
        quantity = int(input("Enter quantity: "))
        hours = float(input("Enter usage per day (hours): "))
        appliance = {
            "name": name,
            "power": power,
            "quantity": quantity,
            "hours": hours
        }

        appliances.append(appliance)

        print("\nAppliance added successfully!")

    # 2. View Appliances
    elif choice == 2:
        if len(appliances) == 0:
            print("\nNo appliances added.")
        else:
            print("\n------------- APPLIANCES -------------")
            for i in range(len(appliances)):
                print("\nAppliance", i + 1)
                print("Name     :", appliances[i]["name"])
                print("Power    :", appliances[i]["power"], "W")
                print("Quantity :", appliances[i]["quantity"])
                print("Hours/day:", appliances[i]["hours"])

    # 3. Calculate Energy Consumption
    elif choice == 3:
        if len(appliances) == 0:
            print("\nNo appliances added.")
        else:
            total_daily_energy = 0
            total_monthly_energy = 0
            print("\n--------- ENERGY CONSUMPTION ---------")
            for appliance in appliances:
                daily_energy = (
                    appliance["power"]
                    * appliance["quantity"]
                    * appliance["hours"]
                ) / 1000
                monthly_energy = daily_energy * 30
                total_daily_energy += daily_energy
                total_monthly_energy += monthly_energy
                print("\n", appliance["name"])
                print("Daily Energy  :", round(daily_energy, 2), "kWh")
                print("Monthly Energy:", round(monthly_energy, 2), "kWh")

            print("\n--------------------------------------")
            print("Total Daily Energy   :", round(total_daily_energy, 2), "kWh")
            print("Total Monthly Energy :", round(total_monthly_energy, 2), "kWh")

    # 4. Calculate Electricity Bill
    elif choice == 4:
        if len(appliances) == 0:
            print("\nNo appliances added.")
        else:
            total_energy = 0
            for appliance in appliances:
                daily_energy = (
                    appliance["power"]
                    * appliance["quantity"]
                    * appliance["hours"]
                ) / 1000
                monthly_energy = daily_energy * 30
                total_energy += monthly_energy

            print("\nTotal Monthly Consumption:",
                  round(total_energy, 2), "kWh")

            # Simple tariff calculation
            if total_energy <= 100:
                bill = total_energy * 2.50

            elif total_energy <= 200:
                bill = (100 * 2.50) + ((total_energy - 100) * 4.00)

            elif total_energy <= 300:
                bill = (100 * 2.50) + (100 * 4.00) + ((total_energy - 200) * 5.50)

            else:
                bill = (
                    (100 * 2.50)
                    + (100 * 4.00)
                    + (100 * 5.50)
                    + ((total_energy - 300) * 7.00)
                )

            print("Estimated Electricity Bill: ₹", round(bill, 2))

    # 5. Power Consumption Report
    elif choice == 5:

        if len(appliances) == 0:
            print("\nNo appliances added.")

        else:

            highest_appliance = appliances[0]
            highest_energy = 0
            total_energy = 0

            for appliance in appliances:

                daily_energy = (
                    appliance["power"]
                    * appliance["quantity"]
                    * appliance["hours"]
                ) / 1000

                monthly_energy = daily_energy * 30

                total_energy += monthly_energy

                if monthly_energy > highest_energy:
                    highest_energy = monthly_energy
                    highest_appliance = appliance

            print("\n========================================")
            print("        POWER CONSUMPTION REPORT")
            print("========================================")

            print("Total Appliances :", len(appliances))
            print("Total Monthly Energy:",
                  round(total_energy, 2), "kWh")

            print("\nHighest Power Consumer:")
            print("Appliance :", highest_appliance["name"])
            print("Power     :", highest_appliance["power"], "W")
            print("Quantity  :", highest_appliance["quantity"])
            print("Usage     :", highest_appliance["hours"], "hours/day")
            print("Consumption:",
                  round(highest_energy, 2), "kWh/month")

            print("\nEnergy Saving Suggestion:")

            if total_energy > 300:
                print("Your energy consumption is HIGH.")
                print("Try reducing appliance usage.")
                print("Use energy-efficient appliances.")

            elif total_energy > 200:
                print("Your energy consumption is MODERATE.")
                print("Switch off appliances when not required.")

            else:
                print("Your energy consumption is LOW.")
                print("Good! Continue saving energy.")

            print("========================================")

    # 6. Exit
    elif choice == 6:

        print("\nThank you for using")
        print("Power Consumption & Electricity Bill Analyzer!")
        break

    else:
        print("\nInvalid choice!")
        print("Please enter a number between 1 and 6.")