import tensorflow as tf

session = tf.Session()

hello = tf.constant("Hello from my demo")
print(session.run(hello))

a = tf.constant(20)
b = tf.constant(25)

print('a+b = {0}'.format(session.run(a+b)))