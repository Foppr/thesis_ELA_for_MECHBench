import numpy as np

class MultiModalSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic component with multiple frequencies
        f = 0.0
        for i in range(self.dim):
            f += np.sin(x_norm[i]) + 0.5 * np.sin(2 * x_norm[i]) + 0.3 * np.sin(3 * x_norm[i])
            
        # Asymmetric saddle points with varying curvature
        for i in range(self.dim):
            # Create asymmetric quadratic terms with directional bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (0.5 * x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.1 * np.sinh(x[i]**2)
            
        # Multi-scale coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Dynamic coupling with varying weights based on dimension indices
                weight = 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.1 * np.sin(i + j)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Fractal-like structure with recursive periodic components
        for i in range(self.dim):
            f += 0.15 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i])
            
        # Chaotic modulation with irregular frequency components
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(17 * x_norm[i]) * np.cos(19 * x_norm[i]) * np.sin(23 * x_norm[i])
        f += 0.1 * chaos
        
        # Additional multi-modal structure with varying peak heights
        for i in range(self.dim):
            f += 0.25 * np.sin(5 * x[i]) * np.cos(8 * x[i]) * np.sin(12 * x[i])
            
        # Dynamic scaling based on proximity to critical points
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.3)) + 0.1 * np.abs(x[i] - np.cos(i * 0.5))
        scale_factor = 1.0 + 0.5 * np.exp(-proximity / 2.0)
        f *= scale_factor
        
        # Enhanced global minimum attraction with higher-order polynomial terms
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Add irregular noise components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(29 * x_norm[i]) + 0.03 * np.cos(31 * x_norm[i])
        f += noise
        
        # Multi-scale harmonic coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                weight = 0.1 * np.exp(-0.2 * (i + j))
                f += weight * np.sin(3 * x[i]) * np.cos(4 * x[j])
                
        # Final adjustment to ensure proper scaling
        f *= 1.0 + 0.03 * np.sum(np.abs(x))
        
        return f