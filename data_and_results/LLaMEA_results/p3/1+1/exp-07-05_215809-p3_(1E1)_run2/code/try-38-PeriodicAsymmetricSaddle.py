import numpy as np

class PeriodicAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic component with multiple frequencies
        f = 0.0
        for i in range(self.dim):
            f += np.sin(x_norm[i]) * np.cos(2 * x_norm[i]) * np.sin(3 * x_norm[i])
            
        # Asymmetric saddle terms with directional bias
        for i in range(self.dim):
            # Asymmetric quadratic with bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i])
            
        # Dynamic coupling between dimensions with varying weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_weight = 0.1 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.05 * np.sin(i * j * 0.1)
                f += coupling_weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.2 * np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.sin(9 * x[i])
            
        # Fractal-like complexity with recursive structure
        for i in range(self.dim):
            f += 0.1 * np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[i]) * np.sin(17 * x_norm[i])
            
        # Chaotic modulation with exponential decay
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.exp(-0.1 * x[i]**2) * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i])
        f += 0.05 * chaos
        
        # Higher-order polynomial terms for increased complexity
        f += 0.1 * np.sum(x**4) + 0.05 * np.sum(x**6)
        
        # Additional asymmetric terms with dynamic weights
        for i in range(self.dim):
            f += 0.15 * np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.sin(4 * x[i]) * np.cos(5 * x[i])
            
        # Final scaling based on distance from origin
        distance = np.sqrt(np.sum(x**2))
        f *= (1.0 + 0.2 * np.exp(-distance / 2.0))
        
        return f