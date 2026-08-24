import numpy as np

class ExponentialTrigonometricCoupling:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base exponential decay with trigonometric modulation
        f = 0.0
        for i in range(self.dim):
            f += np.exp(-0.5 * x[i]**2) * np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i])
            
        # Adaptive conditioning with dimension-dependent weights
        for i in range(self.dim):
            weight = 0.5 * (1 + np.sin(i * 0.5)) * np.exp(-0.1 * i)
            f += weight * np.sin(4 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
            
        # Multi-scale trigonometric coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.exp(-0.1 * (i + j)) * np.sin(2 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 2 * x[j])
                f += coupling
                
        # Fractal-like structure with recursive exponential terms
        for i in range(self.dim):
            f += 0.3 * np.exp(-0.3 * x[i]**2) * np.sin(7 * x_norm[i]) * np.cos(8 * x_norm[i]) * np.sin(9 * x_norm[i])
            
        # Sharp ridge and valley structure with hyperbolic tangent modulation
        for i in range(self.dim):
            f += 0.2 * np.tanh(2 * x[i]) * np.sin(6 * x[i]) * np.cos(4 * x[i])
            
        # Multi-modal peaks with varying heights and widths
        for i in range(self.dim):
            f += 0.4 * np.exp(-0.5 * (x[i] - np.sin(i * 0.7))**2) * np.sin(10 * x[i]) * np.cos(12 * x[i])
            
        # Dynamic conditioning based on neighbor interactions
        for i in range(self.dim):
            neighbor_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    neighbor_sum += np.exp(-0.2 * (x[i] - x[j])**2)
            f += 0.1 * neighbor_sum * np.sin(5 * x[i])
            
        # Asymmetric saddle points with exponential bias
        for i in range(self.dim):
            bias = 0.3 * np.exp(-0.1 * i) * np.sin(i * 0.8)
            f += (0.5 * x[i]**2 + bias * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Higher-order polynomial with trigonometric modulation
        f += 0.1 * np.sum(x**4) + 0.05 * np.sum(np.sin(x)**2)
        
        # Final scaling and noise addition
        f *= 1.0 + 0.1 * np.sum(np.abs(x))
        f += 0.05 * np.random.randn()
        
        return f