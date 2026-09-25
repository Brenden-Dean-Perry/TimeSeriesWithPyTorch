import torch
from matplotlib import pyplot as plt


def plot_sigmoid_function():
    x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
    sigmoid = torch.nn.Sigmoid()
    __plot_activation_fn_and_derivative(
        sigmoid, x, xlabel='x', ylabel='Sigmoid(x)',
        title='Sigmoid Activation Function'
    )

def plot_tanh_function():
    x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
    y_tanh = torch.nn.Tanh()
    __plot_activation_fn_and_derivative(
        y_tanh, x, xlabel='x', ylabel='Tanh(x)',
        title='Tanh Activation Function'
    )

def plot_relu_function():
    x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
    y_relu = torch.nn.ReLU()
    __plot_activation_fn_and_derivative(
        y_relu, x, xlabel='x', ylabel='ReLU(x)',
        title='ReLU Activation Function'
    )

def plot_leaky_relu_function():
    x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
    y_leaky_relu = torch.nn.LeakyReLU(negative_slope=0.1)
    __plot_activation_fn_and_derivative(
        y_leaky_relu, x, xlabel='x', ylabel='Leaky ReLU(x)',
        title='Leaky ReLU Activation Function', ylim=(-2, 6)
    )

def plot_switch_function():
    x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
    swish_fn = Swish(beta=1.0)
    __plot_activation_fn_and_derivative(
        swish_fn, x, xlabel='x', ylabel='Swish(x)',
        title='Swish Activation Function'
    )

class Swish(torch.nn.Module):
    def __init__(self, beta=1.0):
        super().__init__()
        self.beta = torch.nn.Parameter(torch.tensor(beta))

    def forward(self, x):
        return x * torch.sigmoid(self.beta * x)

def __plot_activation_fn_and_derivative(fn, x, xlabel='x', ylabel='y',
                                       title='Activation Function', linewidth=2.5,
                                       figsize=(10, 5), ylim=None):
    plt.figure(figsize=figsize)
    x = x.detach().requires_grad_(True)
    y = fn(x)
    y.backward(torch.ones_like(x))
    dy_dx = x.grad
    plt.plot(x.detach().numpy(), y.detach().numpy(), linewidth=linewidth, label='Function')
    plt.plot(x.detach().numpy(), dy_dx.detach().numpy(), linewidth=linewidth,
             linestyle='--', label='Derivative')
    plt.axvline(0, color='black', linewidth=1.5, linestyle='--')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if ylim:
        plt.ylim(ylim)
    plt.legend()
    plt.show()