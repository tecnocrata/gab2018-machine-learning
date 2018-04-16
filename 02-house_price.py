import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

houses = 160

np.random.seed(55)
#Square feeds
houseSize = np.random.randint(low=1000, high=3500, size=houses)

np.random.seed(55)
housePrice = houseSize *100 + np.random.randint(low=20000, high=70000, size=houses)

plt.plot(houseSize, housePrice, 'bx')
plt.xlabel('Size')
plt.ylabel('Price')
plt.show()

#Better name is: Standarize
def normalize(array):
    return (array-array.mean())/ array.std()

trainSize = math.floor(houses*0.7)

#TRAIN DATA
trainHouseSize = np.asarray(houseSize[:trainSize])
trainHousePrice = np.asarray(housePrice[:trainSize:]) #trainHousePrice = np.asanarray(housePrice[:trainSize:])

trainHouseSizeNormalized = normalize(trainHouseSize)
trainHousePriceNormalized = normalize(trainHousePrice)

#TEST DATA
testHouseSize = np.array(houseSize[trainSize:])
testHousePrice = np.array(housePrice[trainSize:])

testHouseSizeNormalized = normalize(testHouseSize)
testHousePriceNormalized = normalize(testHousePrice)

# Setup tensorFlow place holders que se actualizaran a medida que se reduzca en el gradiente
tfHouseSize = tf.placeholder("float", name="House-Size")
tfHousePrice = tf.placeholder("float", name="House-Price")

#1. Estos son los valores que resultan den 'aprendizaje'
#Los inicializamos en valores randomicos
tfSizeFactor = tf.Variable(np.random.rand(), name="size-factor")
tfPriceOffset = tf.Variable(np.random.rand(), name="price-offset")

#2. Definiendo la formula que predice los valores
tfPricePredicted = tf.add(tf.multiply(tfSizeFactor, tfHouseSize), tfPriceOffset)

#3. Definimos la funcion de perdida/costo (cuanto es el error)
#  esta funcion es el Error Cuadrado Medio

tfCost = tf.reduce_sum(tf.pow(tfPricePredicted-tfHousePrice, 2))/(2*trainSize)

learningRate = 0.1

#4. Definimos el optimizador de Gradiente Descendente que minimizara la perdida
optimizer = tf.train.GradientDescentOptimizer(learningRate).minimize(tfCost)


#Inicializamos las variables anteriormente declaradas, creando el contexto de tensorflow
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    displayEvery =2
    iterations = 50

    for iteration in range(iterations):

        for (x,y) in zip(trainHouseSizeNormalized, trainHousePriceNormalized):
            sess.run(optimizer, feed_dict={tfHouseSize:x, tfHousePrice:y})
        
        if(iteration+1) % displayEvery == 0:
            c= sess.run(tfCost, feed_dict={tfHouseSize: trainHouseSizeNormalized, tfHousePrice: trainHousePriceNormalized})
            print ("Iteration #",'%04d' % (iteration+1), "cost =", "{:9f}".format(c), "size-factor=", sess.run(tfSizeFactor), "price-offset=", sess.run(tfPriceOffset))
    
    print ('Optmization finished!')
    trainingCost = sess.run(tfCost, feed_dict={tfHouseSize: trainHouseSizeNormalized, tfHousePrice: trainHousePriceNormalized})
    print("Trained cost =", trainingCost, "size-factor=", sess.run(tfSizeFactor), "price-offset=", sess.run(tfPriceOffset))

    #PLOT RESULTS
    trainHouseSizeMean = trainHouseSize.mean()
    trainHouseSizeStd = trainHouseSize.std()

    trainHousePriceMean = trainHousePrice.mean()
    trainHousePriceStd = trainHousePrice.std()

    plt.rcParams["figure.figsize"] = (10,8)
    plt.figure()
    plt.ylabel("Price")
    plt.xlabel("Size (Sq ft)")
    plt.plot(trainHouseSize, trainHousePrice, 'go', label='Training data')
    plt.plot(testHouseSize, testHousePrice, 'mo', label='Testing Data')
    #Draw LINE model result
    #plt.plot(trainHouseSizeNormalized*trainHouseSizeStd + trainHouseSizeMean, (sess.run(tfSizeFactor)*trainHouseSizeNormalized+sess.run(tfPriceOffset))*trainHousePriceStd+trainHousePriceMean, label='Learned Regression')
    plt.plot(trainHouseSizeNormalized*trainHouseSizeStd + trainHouseSizeMean, (sess.run(tfSizeFactor)*trainHouseSizeNormalized+sess.run(tfPriceOffset))*trainHousePriceStd+trainHousePriceMean, label='Learned Regression')
    plt.legend(loc='upper left')
    plt.show()