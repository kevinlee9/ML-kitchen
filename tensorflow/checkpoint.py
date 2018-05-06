saver = tf.train.Saver(max_to_keep=50)

# resume training
print("loading model from checkpoint")
checkpoint = tf.train.latest_checkpoint(filewriter_path)
saver.restore(sess, checkpoint)


# save the model after each epoch
print("Saving checkpoint of model...")
# save checkpoint of the model
checkpoint_name = os.path.join(filewriter_path, 'model_epoch' + str(epoch + 1) + '.ckpt')
saver.save(sess, checkpoint_name)
print("Model checkpoint saved at {}".format(checkpoint_name))
