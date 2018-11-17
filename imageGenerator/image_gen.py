import tensorflow as tf
import tflearn
import numpy as np

def generator(x, reuse=False):
    with tf.variable_scope('generator', reuse=reuse):
    ## design the generator network
    ## input layer is ????
    input_layer = tflearn.input_data(shape=[None, 32, 32, 3])
    ## fully connected layer
    fc_layer_0 = tflearn.fully_connected(input_layer, 512, activation='relu', name='fc_layer_0')
    normalize_layer = tflearn.batch_normalization(fc_layer_0)
    tan_layer = tf.nn.tanh(normalize_layer)
    reshaped_layer = tf.reshape(tan_layer, shape=[-1, 7, 7, 128])
    upsample_layer = tflearn.upsample_2d(reshaped_layer, 2)
    ## convolutional layer
    conv_layer = tflearn.conv_2d(input_layer,
                        nb_filter=64,
                        filter_size=5,
                        activation='tanh',
                        name='conv_layer_1')
    ## max pooling layer
    pool_layer = tflearn.max_pool_2d(conv_layer, 2, name='pool_layer_1')
    ## fully connected layer
    fc_layer_1 = tflearn.fully_connected(pool_layer, 512, activation='relu', name='fc_layer_1')
    ## dropout layer
    dropout_layer = tflearn.dropout(fc_layer_1, 0.5)
    ## fully connected with 2 layers, 0 is not a bee, 1 is a bee
    fc_layer_2 = tflearn.fully_connected(dropout_layer, 2, activation='softmax', name='fc_layer_2')
    ## network is trained with relu, categorical cross entropy loss function, and eta = 0.01
    network = tflearn.regression(fc_layer_2, optimizer='relu',
                        loss='categorical_crossentropy', learning_rate=0.01)
    return network