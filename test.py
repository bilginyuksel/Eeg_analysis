import pickle
from scipy.io import loadmat
import pandas
import random

__LEFT_BACKWARD = "Sol Kol Arka"
__LEFT_FORWARD = "Sol Kol Ön"
__RIGHT_BACKWARD ="Sağ Kol Arka"
__RIGHT_FORWARD = "Sağ Kol Ön"
__RIGHT_LEG = "Sağ Ayak"
__LEFT_LEG = "Sol Ayak"
# Load already trained random forest classifier model
model = pickle.load(open('rfclassifier.sav','rb'))

raw_data = loadmat("Subject1_2D.mat")


def robotic_arm_movement_test(current_pos, obj_pos, list_of_movements):
    # our strategy is change your current position to reach object
    if len(current_pos)!=3 or len(obj_pos)!=3:
        print("Wrong input format !")
        return None # error

    x,y,z = [( obj_pos[i]-current_pos[i]) for i in range(3)]

    print("You have to move your arm on X position {0} unit".format(x))
    print("You have to move your arm on Y position {0} unit".format(y))
    print("You have to move your arm on X position {0} unit".format(z))

    _x,_y,_z = current_pos
    print("Model predictions completed....")
    global model
    prediction_counter = 1
    for i in list_of_movements:
        prediction = model.predict(i.drop("label",axis=1))
        print("-"*25) 
        print(str(prediction_counter)+". Prediction")
        prediction_counter +=1
        print("Model Prediction : ",prediction)
        print("Actual Label : ",i.label.iloc[0])
        if prediction == __LEFT_FORWARD:
            # update x value  ++ 
            print("X Value Before Prediction : ",_x)
            _x+=1
            print("X Value After Prediction : ",_x)
        elif prediction == __LEFT_BACKWARD:
            # update x value --
            print("X Value Before Prediction : ",_x)
            _x-=1
            print("X Value After Prediction : ",_x)
        elif prediction == __RIGHT_FORWARD:
            # update y value ++
            print("Y Value Before Prediction : ",_y)
            _y+=1
            print("Y Value After Prediction : ",_y)
        elif prediction == __RIGHT_BACKWARD:
            # update y value --
            print("Y Value Before Prediction : ",_y)
            _y-=1
            print("Y Value After Prediction : ",_y)
        elif prediction == __RIGHT_LEG:
            # update z value ++ 
            print("Z Value Before Prediction : ",_z)
            _z+=1
            print("Z Value After Prediction : ",_z)
        elif prediction == __LEFT_LEG:
            # update z value --
            print("Z Value Before Prediction : ",_z)
            _z-=1
            print("Z Value After Prediction : ",_z)

    print("-"*25)
    print("Results")
    print("Starting position : ({0},{1},{2})".format(current_pos[0],current_pos[1],current_pos[2]))
    print("Object Position : ({0},{1},{2})".format(obj_pos[0],obj_pos[1],obj_pos[2]))
    print("Final Position : ({0},{1},{2})".format(_x,_y,_z))

def takeSampleData(data):
    rand_number = random.randint(1,len(data))

    return data[rand_number-1:rand_number]


data1 = pandas.DataFrame(raw_data['LeftBackwardImagined'])
data2 = pandas.DataFrame(raw_data['LeftForwardImagined'])
data3 = pandas.DataFrame(raw_data['RightBackwardImagined'])
data4 = pandas.DataFrame(raw_data['RightForwardImagined'])
data5 = pandas.DataFrame(raw_data['RightLeg'])
data6 = pandas.DataFrame(raw_data['LeftLeg'])
data1['label'] = [__LEFT_BACKWARD for i in range(len(data1))]
data2['label'] =[__LEFT_FORWARD for i in range(len(data2))]
data3['label'] = [__RIGHT_BACKWARD for i in range(len(data3))]
data4['label'] = [__RIGHT_FORWARD for i in range(len(data4))]
data5['label'] = [__RIGHT_LEG for i in range(len(data5))]
data6['label'] = [__LEFT_LEG for i in range(len(data6))]

# For this unit test.
current_position = [0,2,1]
target_position = (1,3,0)
"""
On this first unit test. Our robotic arms current position is (x,y,z) = (0,2,1),
and our target position is (x,y,z) = (1,3,0)

In our system subject has to think right things for moving the robotic arm correctly..
Our Thought System : 
    x++ -> Subject has to think to move his left arm forward
    x-- -> Subject has to think to move his left arm backward
    y++ -> Subject has to think to move his right arm forward
    y-- -> Subject has to think to move his right arm backward
    z++ -> Subject has to think to move his right leg
    z-- -> Subject has to think to move his left leg

So in our first test, the movements should declare as :
    1 Left Arm Forward
    1 Right Arm Forward
    1 Left Leg
"""
# TEST 1
list_of_movements = [takeSampleData(data2),takeSampleData(data4),takeSampleData(data6)]

robotic_arm_movement_test(current_pos=current_position,obj_pos=target_position,list_of_movements=list_of_movements)

#************************************************************************************
# TEST 2
print("*"*30)
print("*"*30)
print("-"*25)
print("TEST 2")
current_position = [10,4,7]
target_position = (1,-5,-3)
"""
for this test the subject has to think moving x-- 9 times.
y-- 9 times
z-- 10 times
"""
list_of_movements.clear()
# For left arm backward
for _ in range(9):
    list_of_movements.append(takeSampleData(data1))
# For right arm backward
for _ in range(9):
    list_of_movements.append(takeSampleData(data3))
# For Left Leg
for _ in range(10):
    list_of_movements.append(takeSampleData(data6))

robotic_arm_movement_test(current_position,target_position,list_of_movements)





class UserDefinedTests():
    
    def __init__(self,current_pos,obj_pos):
        # Make controls here.
        # Right now test only accepts 3 dimensions.

        self.old_x,self.old_y,self.old_z = current_pos
        self.current_pos = current_pos
        self.obj_pos = obj_pos
        self.dimension = len(obj_pos)
        self.list_of_movements = []

        print("Start Position : ({0},{1},{2})".format(self.old_x,self.old_y,self.old_z))
        print("Target Position : ({0},{1},{2})".format(self.obj_pos[0],self.obj_pos[1],self.obj_pos[2]))
        print("-"*30)

        self.__LEFT_BACKWARD = "Sol Kol Arka"
        self.__LEFT_FORWARD = "Sol Kol Ön"
        self.__RIGHT_BACKWARD ="Sağ Kol Arka"
        self.__RIGHT_FORWARD = "Sağ Kol Ön"
        self.__RIGHT_LEG = "Sağ Ayak"
        self.__LEFT_LEG = "Sol Ayak"

    def setData(self,*args):
        self.left_backward,self.left_forward,self.right_backward,self.right_forward,self.right_leg,self.left_leg = args

    def setModel(self,model):
        self.model = model

    def __sample(self,data):
        r_num = random.randint(1,len(data))
        return data[r_num-1:r_num]

    def __addData(self,data,number_of_times):
        for _ in range(number_of_times):
            self.list_of_movements.append(self.__sample(data))

    def prepareTest(self):
        print("Preparing Test...")
        self.x,self.y,self.z = [(self.obj_pos[i] - self.current_pos[i]) for i in range(self.dimension)]
        print("You have to move your arm on X position {0} unit".format(self.x))
        print("You have to move your arm on Y position {0} unit".format(self.y))
        print("You have to move your arm on Z position {0} unit".format(self.z))

        if self.x < 0:
            # Left arm backward
            self.x*=-1
            self.__addData(self.left_backward,self.x)
        else:
            # Left arm forward
            self.__addData(self.left_forward,self.x)

        if self.y < 0:
            # Right arm backward
            self.y*=-1
            self.__addData(self.right_backward,self.y)
        else:
            self.__addData(self.right_forward,self.y)

        if self.z < 0:
            # Left Leg
            self.z *=-1
            self.__addData(self.left_leg,self.z)
        else:
            # Right Leg
            self.__addData(self.right_leg,self.z)

    

    def move(self):
        # detailed move
        step = 1
        for i in self.list_of_movements:
            prediction = self.model.predict(i.drop("label",axis=1))
            print("-"*30)
            print("Step {0}".format(step))
            step+=1
            print("Model Prediction : ",prediction)
            print("Actual Label : ",i.label.iloc[0])

            if prediction == self.__LEFT_FORWARD:
                self.current_pos[0]+=1
            elif prediction == self.__LEFT_BACKWARD:
                self.current_pos[0]-=1
            elif prediction == self.__RIGHT_FORWARD:
                self.current_pos[1]+=1
            elif prediction == self.__RIGHT_BACKWARD:
                self.current_pos[1]-=1
            elif prediction == self.__RIGHT_LEG:
                self.current_pos[2]+=1
            elif prediction == self.__LEFT_LEG:
                self.current_pos[2]-=1

            print("Updated (x,y,z) = ({0},{1},{2})".format(self.current_pos[0],self.current_pos[1],self.current_pos[2]))

    def results(self):
        # if self.current_pos != self.obj_pos:
        #     print("Wrong Place !!")
        print("-"*30)
        print("Old Position : ({0},{1},{2})".format(self.old_x,self.old_y,self.old_z))
        print("Target Position : ({0},{1},{2})".format(self.obj_pos[0],self.obj_pos[1],self.obj_pos[2]))
        print("Current Position : ({0},{1},{2})".format(self.current_pos[0],self.current_pos[1],self.current_pos[2]))

print("*"*30)
print("*"*30)
print("TEST 1")
test1 = UserDefinedTests([0,1,2],[1,1,1])
test1.setData(data1,data2,data3,data4,data5,data6)
test1.setModel(model)
test1.prepareTest()
test1.move()
test1.results()



print("*"*30)
print("*"*30)
print("Welcome to user defined test simulation")
c_pos = input("Enter your current position: [x,y,z]")
t_pos = input("Enter your target position: [x,y,z]")
c_pos = list(map(int,c_pos.split(",")))
t_pos = list(map(int,t_pos.split(",")))
print("*"*30)
print("*"*30)
print("TEST 2")
test2 = UserDefinedTests(c_pos,t_pos)
test2.setData(data1,data2,data3,data4,data5,data6)
test2.setModel(model)
test2.prepareTest()
test2.move()
test2.results()
