import ansur_functions as funcs
print(funcs.fourty_lines())
funcs.resize()

input('')
print(funcs.fourty_lines() + funcs.print_line() + "\n" + funcs.blank_line())
print(f"{funcs.better_print('This is not something that will make you happier, but it might satisfy your curiosity.')}")
print(funcs.blank_line())
print(f"{funcs.better_print('This is a simple program, you enter your measurements from before hrt,')}")
print(f"{funcs.better_print('and it tells you what they would be had you been born opposite your AGAB.')}")
print(funcs.blank_line())
print(f"{funcs.better_print('The method is simple; for each measurement it checks how you compare up to the average for your AGAB,')}")
print(f"{funcs.better_print('then calculates how the corresponding value of the opposite gender.')}")
print(funcs.blank_line())
print(f"{funcs.better_print('For examples, if you are 0.5 standard deviations below average shoulder breadth for an AFAB,')}")
print(f"{funcs.better_print('it would calculate what 0.5 standard deviations below average shoulder breadth is for an AMAB.')}")
print(funcs.blank_line())
print(f"{funcs.better_print('DISCLAIMER: obviously I have no idea what I am doing and nothing here should be taken seriously.')}")
print(funcs.blank_line())
print(f"{funcs.better_print('IT SHOULD ALSO BE NOTED:')}")
print(f"{funcs.better_print('I am using ANSUR datasets which are based on adult Americans so if you began hrt before adulthood this will not be vaild.')}")
print(f"{funcs.better_print('There is also no underbust measurement in ANSUR 2 so I used chest circumference instead.')}")
print(f"{funcs.better_print('Also you need numpy installed for this to work.')}")
print(funcs.blank_line())
print(f"{funcs.better_print('Press enter to continue...')}")
print(funcs.blank_line())
print(funcs.print_line())
input('')

print(funcs.fourty_lines())
version = input("Which version of ANSUR would you like to use? Version 2 is more recent but version 1 is less hugboxy. (1/2) ")
gender = input("Enter your AGAB: (m/f) ")
units = input("Which units would you like to use? (in/cm) ")
if units == "cm":
    multiplier = 10
else:
    multiplier = 25.4
bideltoid = float(input("Enter your Bideltoid Shoulder Breadth: "))*multiplier
hipB = float(input("Enter you Hip Breadth: "))*multiplier
waistC = float(input("Enter you Waist Circumference: "))*multiplier
hipC = float(input("Enter your Hips Circumference: "))*multiplier
chestC = float(input("Enter your Chest Circumference: "))*multiplier
height = float(input("Enter you Height: "))

#selects which version to use based user input
if version == "1":
    bidel = "BIDELTOID_BRTH"
    hipbreadth = "HIP_BRTH"
    waist = "WAIST_CIRC_NATURAL"
    hipcirc = "BUTTOCK_CIRC"
    height_v = "STATURE"
    chest = "CHEST_CIRC"
    height *= multiplier
else:
    bidel = "bideltoidbreadth"
    hipbreadth = "hipbreadth"
    waist = "waistcircumference"
    hipcirc = "buttockcircumference"
    height_v = "Heightin"
    chest = "chestcircumference"
    if units == "cm":
        height /= 2.54

if version == "1":
    dataset_f = "ansur1_female.csv"
    dataset_m = "ansur1_male.csv"
else:
    dataset_f = "ansur2_female.csv"
    dataset_m = "ansur2_male.csv"


#I KNOW THIS SUCKS BUT IT WOULD TAKE ME MORE TIME TO MAKE IT GOOD THAN IT TOOK ME TO MAKE THIS
#I realize now that this would be way easier using lists but I'm retarded (I'll probably fix this when I have the time)
#calculations for AFAB Standard Deviations and Averages
bidel_sd_f, bidel_avg_f = funcs.avg_and_sd_calc(funcs.list_gen(bidel, dataset_f))
hipbreadth_sd_f, hipbreadth_avg_f = funcs.avg_and_sd_calc(funcs.list_gen(hipbreadth, dataset_f))
waist_sd_f, waist_avg_f = funcs.avg_and_sd_calc(funcs.list_gen(waist, dataset_f))
hipcirc_sd_f, hipcirc_avg_f = funcs.avg_and_sd_calc(funcs.list_gen(hipcirc, dataset_f))
height_sd_f, height_avg_f = funcs.avg_and_sd_calc(funcs.list_gen(height_v, dataset_f))
chest_sd_f, chest_avg_f = funcs.avg_and_sd_calc(funcs.list_gen(chest, dataset_f))

#calculations for AMAB Standard Deviations and Averages
bidel_sd_m, bidel_avg_m = funcs.avg_and_sd_calc(funcs.list_gen(bidel, dataset_m))
hipbreadth_sd_m, hipbreadth_avg_m = funcs.avg_and_sd_calc(funcs.list_gen(hipbreadth, dataset_m))
waist_sd_m, waist_avg_m = funcs.avg_and_sd_calc(funcs.list_gen(waist, dataset_m))
hipcirc_sd_m, hipcirc_avg_m = funcs.avg_and_sd_calc(funcs.list_gen(hipcirc, dataset_m))
height_sd_m, height_avg_m = funcs.avg_and_sd_calc(funcs.list_gen(height_v, dataset_m))
chest_sd_m, chest_avg_m = funcs.avg_and_sd_calc(funcs.list_gen(chest, dataset_m))

#calulations to compare to the average of AGAB
if gender == "f":
    new_bidel = ((bideltoid - bidel_avg_f)/bidel_sd_f)*bidel_sd_m + bidel_avg_m
    new_hipbreadth = ((hipB - hipbreadth_avg_f)/hipbreadth_sd_f)*hipbreadth_sd_m + hipbreadth_avg_m
    new_waist = ((waistC - waist_avg_f)/waist_sd_f)*waist_sd_m + waist_avg_m
    new_hipcirc = ((hipC - hipcirc_avg_f)/hipcirc_sd_f)*hipcirc_sd_m + hipcirc_avg_m
    new_chest = ((chestC - chest_avg_f)/chest_sd_f)*chest_sd_m + chest_avg_m
    new_height = ((height - height_avg_f)/height_sd_f)*height_sd_m + height_avg_m
    print(new_bidel, new_hipbreadth, new_waist, new_hipcirc, new_height)
else:
    new_bidel = ((bideltoid - bidel_avg_m)/bidel_sd_m)*bidel_sd_f + bidel_avg_f
    new_hipbreadth = ((hipB - hipbreadth_avg_m)/hipbreadth_sd_f)*hipbreadth_sd_m + hipbreadth_avg_f
    new_waist = ((waistC - waist_avg_m)/waist_sd_m)*waist_sd_f + waist_avg_f
    new_hipcirc = ((hipC - hipcirc_avg_m)/hipcirc_sd_m)*hipcirc_sd_f + hipcirc_avg_f
    new_chest = ((chestC - chest_avg_m)/chest_sd_m)*chest_sd_f + chest_avg_f
    new_height = ((height - height_avg_m)/height_sd_m)*height_sd_f + height_avg_f
    print(new_bidel, new_hipbreadth, new_waist, new_hipcirc, new_height)


print(funcs.fourty_lines() + funcs.print_line())
for x in range(6):
        print(funcs.better_print(' '))
print(f"{funcs.better_print(f'Had you been born opposite your AGAB here is how your measurements would change based on ANSUR {version}:')}")
print(f"{funcs.better_print(f'Bideltoid shoulder breadth: {round(bideltoid/multiplier, 1)} -> {round(new_bidel/multiplier, 1)} {units}')}")
print(f"{funcs.better_print(f'Hip breadth: {round(hipB/multiplier, 1)} -> {round(new_hipbreadth/multiplier, 1)} {units}')}")
print(f"{funcs.better_print(f'Waist circumference: {round(waistC/multiplier, 1)} -> {round(new_waist/multiplier, 1)} {units}')}")
print(f"{funcs.better_print(f'Hip circumference: {round(hipC/multiplier, 1)} -> {round(new_hipcirc/multiplier, 1)} {units}')}")
print(f"{funcs.better_print(f'Chest circumference: {round(chestC/multiplier, 1)} -> {round(new_chest/multiplier, 1)} {units}')}")
if version == '1' and units == "in":
    print(f"{funcs.better_print(f'Height: {int(height/multiplier)//12}ft{round((height/multiplier)%12, 1)} -> {int(new_height/multiplier)//12}ft{round((new_height/multiplier)%12, 1)} {units}')}")
elif version == '1' and units == "cm":
    print(f"{funcs.better_print(f'Height: {round(height/multiplier, 1)} -> {round(new_height/multiplier, 1)} {units}')}")
elif version == '2' and units == 'cm':
    print(f"{funcs.better_print(f'Height: {round(height*2.54, 1)} -> {round(new_height*2.54, 1)} {units}')}")
else:
    print(f"{funcs.better_print(f'Height: {int(height)//12}ft{round((height)%12, 1)} -> {int(new_height)//12}ft{round((new_height)%12, 1)} {units}')}")
print(funcs.blank_line())
print(f"{funcs.better_print('Press enter to continue...')}")
for x in range(6):
        print(funcs.better_print(' '))
print(funcs.print_line())
input('')


print(funcs.fourty_lines() + funcs.print_line() + "\n" + funcs.blank_line())
for x in range(6):
        print(funcs.better_print(' '))
    
print(f"{funcs.better_print(f'Thats all for now, if you want to keep bonepilling yourself try out passoid_detector.py')}")
print(funcs.blank_line())
print(f"{funcs.better_print(f'You can follow my reddit, u/FallingForPropaganda')}")
print(funcs.blank_line())
print(f"{funcs.better_print(f'If you are interested in more bonepills, watch the repository for more updates')}")
print(f"{funcs.better_print(f'In the future Im planning on making an anthro.cs like app that supports ANSUR II, imperial units, and shows SDs from the norm')}")
print(funcs.blank_line())
print(f"{funcs.better_print(f'Press enter to exit...')}")
for x in range(6):
        print(funcs.better_print(' '))
print(funcs.print_line())
input("")
print(funcs.fourty_lines())
'''
new_bidel
new_hipbreadth
new_waist
new_hipcirc
new_height

'''