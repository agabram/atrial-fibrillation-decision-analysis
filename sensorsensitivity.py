import random
import statistics
Specificity = .985 #1 - FP_RATE
Sensitivity = 80 #1 - FN_RATE

DOCTOR_FOLLOW_UP = .57 # people who went to doctor after notification
POPULATION = 1000000
device_cost_list = [1,5,10,15,20,25,30,50,75,100,150,200,250,300,350,400,450,500]
num_diagnosed_af = 0
num_undiagnosed_af = 0
num_doctor_no_af = 0
num_no_doctor_no_af = 0
sensitivity_100_qaly = []
sensitivity_100_cost = []

percent_diagnosed_af_list = []
percent_undiagnosed_af_list = []
percent_doctor_no_af_list = []
percent_no_doctor_no_af_list = []
#people who wore sensor
for a in range(1000):
    for i in range(POPULATION):
        generated_int_zero = random.randrange(0, 1000)/1000
        generated_int_one = random.randrange(0, 1000)/1000
        generated_int_two = random.randrange(0, 1000)/1000
        generated_int_three = random.randrange(0, 1000)/1000
        generated_int_four = random.randrange(0, 1000)/1000
        generated_int_five = random.randrange(0, 1000)/1000

    #SET WHETHER PATIENT HAS AF
        if generated_int_zero < .086:
            AF = True
        else:
            AF = False
    #patient enters tree
        if AF:
            if generated_int_one < Sensitivity:
                #get notification
                if generated_int_three < DOCTOR_FOLLOW_UP:
                    #go to doctor
                    num_diagnosed_af += 1
                else:
                    #no doctor but yes AF
                    num_undiagnosed_af += 1
            else:
                #no notification but yes AF
                if generated_int_four < .5:
                    #50% of patients > 65 go to doctor annually
                    num_diagnosed_af += 1
                else:
                    num_undiagnosed_af += 1
        else:
            # no AF
            if generated_int_two < Specificity:
                #no notification, no AF
                if generated_int_four < .5:
                    #50% of patients > 65 go to doctor annually
                    num_doctor_no_af += 1
                else:
                    num_no_doctor_no_af += 1
            else:
                #get notification, no AF
                if generated_int_five < DOCTOR_FOLLOW_UP:
                    #go to doctor
                    num_doctor_no_af += 1
                else:
                    num_no_doctor_no_af += 1

    percent_diagnosed_af = num_diagnosed_af / POPULATION
    percent_undiagnosed_af = num_undiagnosed_af / POPULATION
    percent_doctor_no_af = num_doctor_no_af / POPULATION
    percent_no_doctor_no_af = num_no_doctor_no_af / POPULATION
    percent_diagnosed_af_list.append(percent_diagnosed_af)
    percent_undiagnosed_af_list.append(percent_undiagnosed_af)
    percent_doctor_no_af_list.append(percent_doctor_no_af)
    percent_no_doctor_no_af_list.append(percent_no_doctor_no_af)
    num_diagnosed_af = 0
    num_undiagnosed_af = 0
    num_doctor_no_af = 0
    num_no_doctor_no_af = 0

print(statistics.stdev(percent_diagnosed_af_list))
print(statistics.stdev(percent_undiagnosed_af_list))
print(statistics.stdev(percent_doctor_no_af_list))
print(statistics.stdev(percent_no_doctor_no_af_list))
average_diagnosed_percent = sum(percent_diagnosed_af_list)/len(percent_diagnosed_af_list)
print(average_diagnosed_percent)

average_undiagnosed_percent = sum(percent_undiagnosed_af_list)/len(percent_undiagnosed_af_list)
print(average_undiagnosed_percent)

average_doc_no_af_percent = sum(percent_doctor_no_af_list)/len(percent_doctor_no_af_list)
print(average_doc_no_af_percent)

average_no_doc_no_af_percent = sum(percent_no_doctor_no_af_list)/len(percent_no_doctor_no_af_list)
print(average_no_doc_no_af_percent)

file1 = open("Sensor80.txt","a")
file1.write("Diagnosed: " + str(average_diagnosed_percent) +"\nUndiagnosed:" + str(average_undiagnosed_percent) + "\nDoc no af:" + str(average_doc_no_af_percent) + "\nNo Doc no af:" + str(average_no_doc_no_af_percent))
file1.close()

