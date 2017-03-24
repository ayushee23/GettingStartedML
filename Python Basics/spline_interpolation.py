#Spline Interpolation


data_dict = {0 : 0, 10 : 227.04, 15 : 362.78, 20 : 517.35, 22.5 : 602.97}

def calculate_speed(b, g, time):
    xx = (data_dict[g] - data_dict[b])/(g-b)
    return data_dict[b] + (xx * (time - b))

for time in [15]:

    time_list = sorted(data_dict.keys())

    for x in range(len(time_list) - 1):

        if time >= time_list[x] and time <= time_list[x+1]:

            print(calculate_speed(time_list[x], time_list[x+1], time))
        
    

