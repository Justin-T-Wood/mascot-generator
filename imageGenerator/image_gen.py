import tensorflow as tf
import tflearn
import numpy as np

def generator(input_layer, reuse=False):
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
    gen_model = tflearn.regression(fc_layer_2, optimizer='adam',
                               loss='categorical_crossentropy',
                               trainable_vars=generator_variables,
                               batch_size=64, name='target_generator')
    generator_network = tflearn.DNN(gen_model)
    return generator_network

def discriminator(input_layer, reuse=False):
    with tf.variable_scope('discriminator', reuse=reuse):
        input_layer = tflearn.conv_2d(input_layer, 64, 5, 2, activation='tanh')
        batch_norm_1 = tflearn.batch_normalization(input_layer, epsilon=1e-5, name='batch_norm_1')
        pool_layer_0 = tflearn.avg_pool_2d(batch_norm_1, 2)
        conv_layer = tflearn.conv_2d(pool_layer_0, 128, 5, activation='tanh')
        pool_layer_1 = tflearn.avg_pool_2d(conv_layer, 2)
        fully_connected_0 = tflearn.fully_connected(pool_layer_1, 1024, activation='tanh')
        full_connected_1 = tflearn.fully_connected(fully_connected_0, 2)
        softmax_layer = tf.nn.softmax(full_connected_1)
        dis_model = tflearn.regression(softmax_layer, optimizer='adam',
                                        placeholder=disc_target,
                                        loss='categorical_crossentropy',
                                        trainable_vars=disc_variables,
                                        batch_size=64, name='target_disc')
        discriminator_network = tflearn.DNN(dis_model)
        return discriminator_network

