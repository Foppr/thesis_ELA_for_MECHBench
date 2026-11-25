import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Compute the sinusoidal multimodal function
        # This creates multiple local minima with a global minimum at the origin
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(0.5 * np.pi * x)) / self.dim
        term3 = np.sum(np.cos(0.3 * np.pi * x)) / self.dim
        
        # Combine terms to create a challenging landscape
        return term1 + 0.5 * term2 + 0.3 * term3