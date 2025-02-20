import input_data
import tensorflow as tf

# Read MNIST data set
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# Labeling function
x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
matm = tf.matmul(x, W)

# Softmax probabilities
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Cross entropy
y_ = tf.placeholder("float", [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# Training method
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# Start session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Learning steps
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    if i % 10 == 0:
        train_accuracy = sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys})
        print("Step %d - Train accuracy %.3f" % (i, train_accuracy))

# Test learned network
test_accuracy = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print("Test accuracy %.3f" % test_accuracy)
