#ICER section
POPULATION = 1000000
num_diagnosed_af = (0.04781381200000003 - 0.00021355718514563574)*POPULATION
num_undiagnosed_af = (0.03818486700000002 - 0.00019320498823394407)*POPULATION
num_doctor_no_af = (0.45798582600000054 - 0.0005040685954043092)*POPULATION
num_no_doctor_no_af = (0.456015495 - 0.0005038245281148286)*POPULATION




device_cost_list = [400]
#QALY Disease Treated: 0.45 +-0.06
qaly_diagnosed = 0.45
#qaly_undiagnosed = 0

total_qaly = qaly_diagnosed*num_diagnosed_af

overall_population_cost_no_sensor = 3805516679.884233 #for 10 mil: 37970442809.159996
no_sensor_total_qaly = 19353.07755  #for 10 mil: 193317.30000000002


for i in device_cost_list:
    DEVICE_COST = i
    DIAGNOSED_COST = 42808.44+DEVICE_COST
    UNDIAGNOSED_COST = 44793.8+DEVICE_COST
    DOCTOR_NO_AF_COST = 74.08+DEVICE_COST
    NO_DOCTOR_NO_AF_COST = DEVICE_COST
    pop_cost_diagnosed = DIAGNOSED_COST*num_diagnosed_af
    pop_cost_undiagnosed = UNDIAGNOSED_COST*num_undiagnosed_af
    pop_cost_yesdoc_noaf = DOCTOR_NO_AF_COST*num_doctor_no_af
    pop_cost_nodoc_noaf = NO_DOCTOR_NO_AF_COST*num_no_doctor_no_af
    overall_population_cost = pop_cost_diagnosed + pop_cost_undiagnosed + pop_cost_yesdoc_noaf + pop_cost_nodoc_noaf
    cost_per_qaly = overall_population_cost/total_qaly
    # print("TOTAL COST: "+str(overall_population_cost))
    # print("overall pop cost at $" + str(DEVICE_COST) + " and Sensitivity = " + str(Sensitivity) + " is " + str(overall_population_cost))
    # print("cost per qaly at " + str(DEVICE_COST) + " and Sensitivity = " + str(Sensitivity) + " is " + str(cost_per_qaly))
    ICER = (overall_population_cost - overall_population_cost_no_sensor) / (total_qaly - no_sensor_total_qaly)
    print(overall_population_cost/1000000, total_qaly/1000000)
