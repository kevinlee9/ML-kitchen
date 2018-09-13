    def build_sp_softmax(self,last_layer,layer):
        preds_max = tf.reduce_max(self.net[last_layer],axis=3,keepdims=True)
        preds_exp = tf.exp(self.net[last_layer] - preds_max)
        self.net[layer] = preds_exp / tf.reduce_sum(preds_exp,axis=3,keepdims=True) + self.min_prob
        self.net[layer] = self.net[layer] / tf.reduce_sum(self.net[layer],axis=3,keepdims=True)
        return layer
