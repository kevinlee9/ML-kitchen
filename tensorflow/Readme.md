#### 一些函数整理
`tf.image.crop_and_resize`: Extracts crops from the input image tensor and resizes them. used for ROI pooling
`tf.image.random_crop`: Randomly crops a tensor to a given size. cannot automatically 0-pad images
`tf.image.resize_image_with_crop_or_pad`: it takes only center crops(padding) not random crops.

no built in function for random_crop
