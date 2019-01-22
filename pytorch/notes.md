
### Resources
[PyTorch 0.4.0 Migration Guide](https://pytorch.org/blog/pytorch-0_4_0-migration-guide/)

### Locally disabling gradient computation
The context managers `torch.no_grad()`, `torch.enable_grad()`, and `torch.set_grad_enabled()` are helpful for locally **disabling and enabling gradient computation**
```python
>>> x = torch.zeros(1, requires_grad=True)
>>> with torch.no_grad():
...     y = x * 2
>>> y.requires_grad
False

>>> is_train = False
>>> with torch.set_grad_enabled(is_train):
...     y = x * 2
>>> y.requires_grad
False

>>> torch.set_grad_enabled(True)  # this can also be used as a function
>>> y = x * 2
>>> y.requires_grad
True

>>> torch.set_grad_enabled(False)
>>> y = x * 2
>>> y.requires_grad
False
```

### NN
#### Module()
`Module.modules()`: Returns an iterator over **all** modules in the network.  
```python
# Duplicate modules are returned only once. In the following example, l will be returned only once.
>>> l = nn.Linear(2, 2)
>>> net = nn.Sequential(l, l)
>>> for idx, m in enumerate(net.modules()):
        print(idx, '->', m)
        
"""
0 -> Sequential (
  (0): Linear (2 -> 2)
  (1): Linear (2 -> 2)
)
1 -> Linear (2 -> 2)
"""

>>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
>>> for idx, m in enumerate(net.modules()):
        print(idx, '->', m)
        
"""
0 -> Sequential (
  (0): Linear (2 -> 2)
  (1): Linear (2 -> 2)
)
1 -> Linear (2 -> 2)
2 -> Linear (2 -> 2)
"""
```

`Module.parameters()`: Returns an iterator over module parameters. This is typically passed to an optimizer

#### Sequential
A sequential container. Modules will be added to it in the order they are passed in the constructor. Alternatively, an ordered dict of modules can also be passed in.
```python
# Example of using Sequential
model = nn.Sequential(
          nn.Conv2d(1,20,5),
          nn.ReLU(),
          nn.Conv2d(20,64,5),
          nn.ReLU()
        )

# Example of using Sequential with OrderedDict
model = nn.Sequential(OrderedDict([
          ('conv1', nn.Conv2d(1,20,5)),
          ('relu1', nn.ReLU()),
          ('conv2', nn.Conv2d(20,64,5)),
          ('relu2', nn.ReLU())
        ]))
```

#### ModuleList
Holds submodules in a list.

ModuleList can be indexed like a regular Python list, but **modules it contains are properly registered, and will be visible by all Module methods**.

#### ModuleDict
Holds submodules in a dict.
```python
class B(nn.Module):
    def __init__(self):
        super(B, self).__init__()
        self.base = nn.ModuleDict(a.named_children())
```


#### Parameter()
A kind of Tensor that is to be considered a module parameter, Parameters are **`Tensor` subclasses**.  
That have a very special property when used with `Module`s - when they’re assigned as Module attributes **they are automatically added to the list of its parameters**, and will appear e.g. in `parameters()` iterator. Assigning a Tensor doesn’t have such effect. This is because one might want to cache some temporary state, like last hidden state of the RNN, in the model

### Tensor
#### Attributes
`torch.dtype`, `torch.device`, and `torch.layout`

### Memory Management
Automatically grow, but not release automatically,
`memory_cached`, `memory_allocated()`, `empty_cache()`
```python
import torch
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv = torch.nn.Conv2d(3, 10, kernel_size=3)
    def forward(self, x):
        return self.conv(x)
        
a = Net().cuda()
# 700M
print(torch.cuda.memory_cached())
images = torch.ones(1, 3, 321, 321)
for i in range(5):
    a(images.cuda())
print(torch.cuda.memory_cached())
# 22000M
images = torch.ones(3, 3, 321, 321)
for i in range(5):
    a(images.cuda())
print(torch.cuda.memory_cached())
# 53000M
images = torch.ones(1, 3, 321, 321)
for i in range(5):
    a(images.cuda())
print(torch.cuda.memory_cached())
# 53000M
```
