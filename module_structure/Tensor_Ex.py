import torch

__all__ = ['TensorCalculator']


class TensorCalculator():
    def __init__(self):
        return None

    def zeros(self, dim_x, dim_y):
        return torch.zeros(dim_x, dim_y)

    def ones(self, dim_x, dim_y):
        return torch.ones(dim_x, dim_y)

    def random(self, dim_x, dim_y):
        return torch.rand(dim_x, dim_y)

    def add(self, t1, t2):
        return torch.add(t1, t2)

    def multiply(self, t1, t2):
        return torch.matmul(t1, t2)

    def extrafunction_1(self, t1):
        t1_mean = torch.mean(t1, dim=0)
        return torch.matmul(t1, t1_mean)

    def extrafunction_2(self, t1):
        t1_t = torch.transpose(t1, 1, 0)
        suma_columna = torch.sum(t1[:, 0])
        return torch.add(t1, suma_columna)