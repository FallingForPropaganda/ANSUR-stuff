import ansur_functions as funcs

print("\n\n\nPassoide detector, enter your measurements and you will be given a passing score.")
print("The ratios measured are: hips-waist, hips-shoulder, shoulder-waist, and a raw value of height.")
print("Closer to zero means closer to the average (passing).")
print("However lower scores are generally more feminine, and higher ones are more masculine.")
print("You should also note that scores are reletive to cis people of that gender.")
print("It is recommended that you use ANSUR 2 as it is more recent.\n\n")

print("All measurements are in cm unless otherwise indicated\n\n")
version = input("Which version of ANSUR would you like to use: (1/2) ")
gender = input("Enter your gender: (m/f) ")
bideltoid = float(input("Enter your Bideltoid Shoulder Breadth: "))*10
hipB = float(input("Enter you Hip Breadth: "))*10
shoulderC = float(input("Enter your Shoulder Circumference: "))*10
waistC = float(input("Enter you Waist Circumference: "))*10
hipC = float(input("Enter your Hips Circumference: "))*10
height = float(input("Enter you Height: "))

print("debug")
print(version, gender, bideltoid, hipB, shoulderC, waistC, hipC, height)


if version == "1":
    if gender == "f":
        dataset = "ansur1_female.csv"
    elif gender == "m":
        dataset = "ansur1_male.csv"
    else:
        print("chose m or f (make sure to use lowercase letters and no spaces")
    bidel = "BIDELTOID_BRTH"
    hipbreadth = "HIP_BRTH"
    waist = "WAIST_CIRC_NATURAL"
    hipcirc = "BUTTOCK_CIRC"
    shoulder = "SHOULDER_CIRC"
    heightV = "STATURE"
    height *= 10
else:
    if gender == "f":
        dataset = "ansur2_female.csv"
        print(dataset, gender)
        print("--------------------------------------------------")
    elif gender == "m":
        dataset = "ansur2_male.csv"
    else:
        print("chose m or f (make sure to use lowercase letters and no spaces")
    bidel = "bideltoidbreadth"
    hipbreadth = "hipbreadth"
    waist = "waistcircumference"
    hipcirc = "buttockcircumference"
    shoulder = "shouldercircumference"
    heightV = "Heightin"
    height /= 2.54

bideltoid_hipsB_SD, bideltoid_hipsB_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(bidel, hipbreadth, dataset)))
whr_SD, whr_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(waist, hipcirc, dataset)))
waist_shoulder_SD, waist_shoulder_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(shoulder, waist, dataset)))
height_SD, height_A = funcs.avg_and_sd_calc(funcs.list_gen(heightV, dataset))

bidel_hipB_sd_dif = ((bideltoid/hipB) - bideltoid_hipsB_A)/bideltoid_hipsB_SD
whr_sd_dif = ((waistC/hipC) -  whr_A)/whr_SD
waist_shoulder_sd_dif = ((shoulderC/waistC) - waist_shoulder_A)/waist_shoulder_SD
height_sd_dif = ((height) - height_A)/height_SD

print("\n\nBideltoid Shoulder to Hip Breadth Ratio")
print(f"Average: {round(bideltoid_hipsB_A, 2)}, SD: {round(bideltoid_hipsB_SD, 2)}. This means that 68% of people fall within a range of {round((bideltoid_hipsB_A - bideltoid_hipsB_SD), 2)} - {round((bideltoid_hipsB_A + bideltoid_hipsB_SD), 2)}")
print(f"Your Bideltoid Shoulder to Hip Breadth Ratio: {round((bideltoid/hipB), 2)}")
print(f"You are {round(bidel_hipB_sd_dif, 2)} standard deviations from the average bideltoid shoulder-hip breadth ratio. ")

print("\n\nHips Waist Ratio")
print(f"Average: {round(whr_A, 2)}, SD: {round(whr_SD, 2)}. This means that 68% of people fall within a range of {round((whr_A - whr_SD), 2)} - {round((whr_A + whr_SD), 2)}")
print(f"Your Hips Waist Ratio: {round((waistC/hipC), 2)}")
print(f"You are {round(whr_sd_dif, 2)} standard deviations from the average hips-waist ratio. ")

print("\n\nShoulder Waist Ratio")
print(f"Average: {round(waist_shoulder_A, 2)}, SD: {round(waist_shoulder_SD, 2)}. This means that 68% of people fall within a range of {round((waist_shoulder_A - waist_shoulder_SD), 2)} - {round((waist_shoulder_A + waist_shoulder_SD), 2)}")
print(f"Your Shoulder Waist Ratio: {round((shoulderC/waistC), 2)}")
print(f"You are {round(waist_shoulder_sd_dif, 2)} standard deviations from the average shoulder-waist ratio. ")

if version == "1":
    print("\n\nHeight")
    print(f"Average: {round((height_A/10), 2)}, SD: {round((height_SD/10), 2)}. This means that 68% of people fall within a range of {round(((height_A/10) - (height_SD/10)), 2)} - {round(((height_A/10) + (height_SD/10)), 2)}")
    print(f"Your Height: {round((height/10), 2)}")
    print(f"You are {round(height_sd_dif, 2)} standard deviations from the average height. ")
else:
    print("\n\nHeight")
    print(f"Average: {round((height_A*2.54), 2)}, SD: {round((height_SD*2.54), 2)}. This means that 68% of people fall within a range of {round(((height_A*2.54) - (height_SD*2.54)), 2)} - {round(((height_A*2.54) + (height_SD*2.54)), 2)}")
    print(f"Your Height: {round((height*2.54), 2)}")
    print(f"You are {round(height_sd_dif, 2)} standard deviations from the average height. ")

print(f"\n\nWith weighting, you are {round(( (bidel_hipB_sd_dif*.3) + (whr_sd_dif*0.3) + (waist_shoulder_sd_dif*0.3) + (height_sd_dif*0.1) ),2)} standard deviations from average")
print("A score under within 1 point of 0 means you probably pass. If it is negative you are more feminine than the average, positive is more masculine")
print("About the weighting: I gave height a lower weight because if you would otherwise pass, height won't clock you")
print("But if you otherwise clocky, height can be an issue")