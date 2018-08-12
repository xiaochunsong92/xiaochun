#Tensor part 
import torch
from torch.autograd import Variable 
a = torch.zeros((15,5))
print('zeors tensor is : {}'.format(a))
b = torch.randn((15,5))
print('normal random is : {}'.format(b))
c = torch.Tensor([[1,2],[3,4],[5,6]])
print('c is : {}'.format(c))
c[0,1] = 200
print('c is changed to : {}'.format(c))

#Variable part
x = Variable(torch.Tensor([1]), requires_grad=True)
w = Variable(torch.Tensor([2]), requires_grad=True)
b = Variable(torch.Tensor([3]), requires_grad=True)

y = w*x + b

y.backward()

print(x.grad)
print(w.grad)
print(b.grad)

