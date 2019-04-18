from random_walk import RandomWalk
import matplotlib.pyplot as plt


import time
timestr = time.strftime("%Y%m%d-%H%M%S")
path = "plot_images/"

# get screen res
width = 2400
height = 1600


#keep plotting walks while true

while True:

    #make a random walk object and plot the points
    walk = RandomWalk(30000)
    walk.fill_walk()

    walk2 = RandomWalk(30000)
    walk2.fill_walk()

    walk3 = RandomWalk(30000)
    walk3.fill_walk()

    walk4 = RandomWalk(30000)
    walk4.fill_walk()

    #create a list represetning each step
    step_number = list(range(walk.num_points))

    # use the tep list to apply color map gradient from light to dark blue
    plt.scatter(walk.x_values,walk.y_values,c = step_number,cmap=plt.cm.Blues, edgecolor="none",s=1)
    plt.scatter(walk2.x_values,walk2.y_values,c = step_number,cmap=plt.cm.Purples, edgecolor="none",s=1)
    plt.scatter(walk3.x_values,walk3.y_values,c = step_number,cmap=plt.cm.Reds, edgecolor="none",s=1)
    plt.scatter(walk4.x_values,walk4.y_values,c = step_number,cmap=plt.cm.Oranges, edgecolor="none",s=1)


    # emphasise the start and end point
    # plt.scatter(0,0,c='green', edgecolor='none',s=75)  #start
    # plt.scatter(walk.x_values[-1],walk.y_values[-1],c='red', edgecolor='none',s=75)  #end

    # hide the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #set the plotting window to full size


    image = plt.gcf()
    image.savefig(path+"image-"+timestr,bbox_inches='tight', dpi= 235)
    plt.figure(dpi =100,figsize=(10,6))

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running =="n":
            break
