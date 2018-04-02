import tensorflow as tf 

W=tf.constant([[1,2,3],[4,5,6]])
print("W: ",W)

a=tf.constant([1,2,3],name="a")
b=tf.constant([4,5,6],name="b")

y=a+b 

init=tf.initialize_all_variables()

with tf.Session() as sess:

    sess.run(init)

    output=sess.run(y)
    print("output: ",output)
