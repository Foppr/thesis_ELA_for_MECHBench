import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add asymmetric saddle points using sinusoidal terms with varying amplitudes and phases
        for i in range(self.dim):
            f += 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim]) + \
                 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[(i + 2) % self.dim])
        
        # Add non-separable cross-dimensional interactions with exponential scaling
        for i in range(self.dim):
            f += 0.1 * np.exp(-0.5 * (x[i] - x[(i + 1) % self.dim])**2) * \
                 np.sin(6 * x[i]) * np.cos(4 * x[(i + 3) % self.dim])
        
        # Introduce a set of shifted local minima with varying distances from origin
        shift = 1.5
        for i in range(self.dim):
            f += 0.25 * (x[i] - shift)**2 * np.sin(3 * x[i]) + \
                 0.1 * (x[i] + shift)**4 * np.cos(2 * x[i])
        
        # Add a global perturbation term with strong non-linearity
        f += 0.5 * np.sum(np.sin(0.7 * x) * np.cos(0.9 * x))
        
        return f