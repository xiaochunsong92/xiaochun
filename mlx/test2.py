import tensorflow as tf 

learning_rate = 0.01
batch_size = 16 
epoch_step = 10000
display_step = 100

x = tf.placeholder("float",[None, 20])
y = tf.placeholder("float",[None, 5])

layer1 = 16
layer2 = 32

w = {
    "h1":tf.Variable(tf.random_normal([20, layer1])),
    "h2":tf.Variable(tf.random_normal([layer1, layer2])),
    "out":tf.Variable(tf.random_normal([layer2, 5]))
    }

b = {
    "h1":tf.Variable(tf.random_normal([layer1])),
    "h2":tf.Variable(tf.random_normal([layer2])),
    "out":tf.Variable(tf.random_normal([5]))
    }

def network(x_input,weight,biases):
    net1 = tf.nn.relu(tf.matmul(x_input, weights["h1"]) + biases["h1"])
    net2 = tf.nn.relu(tf.matmul(net1, weights["h2"]) + biases["h2"])
    output = tf.matmul(net2, weights["out"]) + biases["out"]

    return output
pred = network(x, w, b)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

correct_pref = tf.equal(tf.argmax(y,1), tf.argmax(pred,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, "float"))

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(epoch_step):
        avg_cost = 0
        total_batch = int(alldata/batch_size)
        for i in range(total_batch):
            x_batch, y_batch = one_batch_size_input, one_batch_size_output

            _,output = sess.run(optimizer, cost], feed_dict = {x:x_batch, y:y_batch})
            avg_cost += output/total_batch 
        if epoch % display_step == 0:
            print("cost:",avg_cost)

    print("finish!")

    print("accuracy: ", sess.run(accuracy, feed_dict = {x:test_x, y: test_y}))

