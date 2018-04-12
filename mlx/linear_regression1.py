import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

learning_rate = 0.01
training_epochs = 2000
display_step = 50 

train_X = numpy.asarray([3.3,4.4,5.5,6.6,4.168,9.779,6.182,7.042])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.573,3.366,2.53,1.221])
n_samples = train_X.shape[0]

X = tf.placeholder("float")
Y = tf.placeholder("float")

W= tf.Variable(rng.randn(),name="weight")
b = tf.Variable(rng.randn(),name="bias")

activation = tf.add(tf.mul(X, W), b)

cost = tf.reduce_sum(tf.pow(activation-Y,2))/(2*n_samples)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for(x,y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})
        
        if epoch % display_step == 0:
            print "Epoch:",'%04d' % (epoch+1), "cost=", "{:.9f}".format(sess.run(cost, feed_dict={X: train_X, Y:train_Y})),"W=",sess.run(W), "b=", sess.run(b)

    print "Optimization Finished!"
    print "cost=", sess.run(cost, feed_dict={X:train_X, Y:train_Y}),"W=", sess.run(W), "b=", sess.run(b)


    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')

    plt.legend()
    plt.show()

