import numpy as np

class MultiModalSinusoidalSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base sinusoidal components with varying frequencies and amplitudes
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with quadratic and cubic terms
        for i in range(self.dim):
            # Asymmetric quadratic term with directional bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.1 * x[i]**3
            
        # Multi-scale periodic components with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.5 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.3 * np.sin(i * j * 0.1)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Dynamic scaling based on distance from critical points
        scale_factor = 1.0
        for i in range(self.dim):
            dist = np.abs(x[i] - np.sin(i * 0.4)) + 0.1 * np.abs(x[i] - np.cos(i * 0.3))
            scale_factor += 0.5 * np.exp(-dist)
        f *= scale_factor
        
        # Fractal-like structure with recursive harmonic terms
        for i in range(self.dim):
            f += 0.2 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i])
            
        # Chaotic perturbations with exponential modulation
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.exp(-0.3 * x[i]**2) * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i])
        f += 0.15 * chaos
        
        # Additional multi-modal structure with higher-order terms
        for i in range(self.dim):
            f += 0.1 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i]) * np.cos(40 * x[i])
            
        # Global minimum attraction with polynomial terms
        f += 0.2 * np.sum(x**4) + 0.05 * np.sum(x**6)
        
        # Irregular coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.2 * np.sin(i * 0.2) * np.cos(j * 0.3) + 0.1 * np.sin(i + j)
                f += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        return f