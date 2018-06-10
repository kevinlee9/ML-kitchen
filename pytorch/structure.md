a good example of project structure
see [PyTorch-ENet](https://github.com/davidtvs/PyTorch-ENet) and [PyTorch-ENet: My introduction to PyTorch](http://www.davidtvs.com/pytorch-enet/) for details

.
├── data                     (modules related to datasets)
│   ├── camvid.py
│   ├── cityscapes.py
│   ├── __init__.py
│   └── utils.py
├── metric                   (modules related to evaluation metrics)
│   ├── confusionmatrix.py
│   ├── __init__.py
│   ├── iou.py
│   ├── metric.py
│   └── multilabelconfusionmatrix.py
├── models                   (modules that define models)
│   └── enet.py
├── save                     (checkpoints are saved here by default)
│   ├── ENet_CamVid
│   └── ENet_Cityscapes
├── args.py                  (command-line arguments for main.py)
├── main.py                  (entry point to train and test the model)
├── requirements.txt         (pip dependencies)
├── test.py                  (defines the Test class)
├── train.py                 (defines the Train class)
├── transforms.py            (custom image transforms)
└── utils.py
