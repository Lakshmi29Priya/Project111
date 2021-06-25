import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,100):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_deviation=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)

print("Mean of sampling distribution: ",mean)
print("Standard deviation of sampling distribution: ",std_deviation)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()
mean_of_sample1=statistics.mean(data)
print("Mean of sample 1:", mean_of_sample1)
fig=ff.create_distplot([mean_list],["claps"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()
mean_of_sample2=statistics.mean(data)
print("Mean of sample 2:", mean_of_sample2)
fig=ff.create_distplot([mean_list],["claps"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN2"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()
mean_of_sample3=statistics.mean(data)
print("Mean of sample 3:", mean_of_sample3)
fig=ff.create_distplot([mean_list],["claps"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN3"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

z_score=(mean-mean_of_sample2)/std_deviation
print("the z score is equal to",z_score)