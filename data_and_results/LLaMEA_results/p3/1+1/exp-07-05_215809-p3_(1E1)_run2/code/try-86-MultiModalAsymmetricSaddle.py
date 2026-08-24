import numpy as np

class MultiModalAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic multi-modal structure with varying frequencies
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with varying bias and non-linear terms
        for i in range(self.dim):
            # Asymmetric quadratic with directional bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.2 * np.sinh(x[i]**2)
            
        # Dynamic coupling between dimensions with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.1 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.05
                f += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Multi-scale periodicity with increasing complexity
        for i in range(self.dim):
            f += 0.15 * np.sin(7 * x[i]) * np.cos(11 * x[i]) * np.sin(13 * x[i]) * np.cos(17 * x[i])
            
        # Fractal-like structure with recursive harmonic components
        for i in range(self.dim):
            f += 0.1 * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i]) * np.sin(29 * x_norm[i])
            
        # Chaotic modulation with exponential decay
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.exp(-0.3 * x[i]**2) * np.sin(31 * x_norm[i]) * np.cos(37 * x_norm[i])
        f += 0.08 * chaos
        
        # Global minimum attraction with higher-order polynomial
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Additional irregular peaks and valleys
        for i in range(self.dim):
            f += 0.1 * np.sin(25 * x[i]) * np.cos(30 * x[i])
            
        # Dimensional weighting to create varying difficulty
        weight_sum = 0.0
        for i in range(self.dim):
            weight_sum += 0.5 * np.sin(i * 0.4) + 0.5
        f *= (1.0 + 0.3 * weight_sum / self.dim)
        
        return f