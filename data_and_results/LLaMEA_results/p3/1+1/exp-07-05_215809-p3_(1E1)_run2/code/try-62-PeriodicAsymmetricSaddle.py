import numpy as np

class PeriodicAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic trigonometric components with varying frequencies
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with varying bias and non-linear terms
        for i in range(self.dim):
            # Asymmetric quadratic and cubic terms with dimension-specific bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.1 * x[i]**3 + 0.05 * np.sin(7 * x[i])
            
        # Dynamic coupling between dimensions with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.1
                f += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Multi-scale periodicity with fractal-like structure
        for i in range(self.dim):
            f += 0.15 * np.sin(11 * x[i]) * np.cos(13 * x[i]) * np.sin(17 * x[i]) * np.cos(19 * x[i])
            
        # Chaotic modulation with exponential decay
        chaos_mod = 0.0
        for i in range(self.dim):
            chaos_mod += np.exp(-0.5 * x[i]**2) * np.sin(23 * x_norm[i]) * np.cos(29 * x_norm[i])
        f += 0.1 * chaos_mod
        
        # Enhanced global minimum attraction with higher-order polynomial terms
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Additional multi-modal structure with irregular peaks
        for i in range(self.dim):
            f += 0.1 * np.sin(15 * x[i]) * np.cos(20 * x[i]) * np.sin(25 * x[i])
            
        # Dimension-specific scaling for varying difficulty
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.8)
            f += 0.05 * scale_factor * np.sin(31 * x[i]) * np.cos(37 * x[i])
            
        # Asymmetric noise components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(41 * x_norm[i]) * np.cos(43 * x_norm[i]) + 0.02 * np.sin(47 * x_norm[i])
        f += noise
        
        # Cross-dimensional coupling with dynamic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.15 * np.sin(i * 0.2) * np.cos(j * 0.3) + 0.1
                cross_coupling += weight * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        f += cross_coupling
        
        return f