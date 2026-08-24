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
            
        # Asymmetric saddle points with varying coefficients
        for i in range(self.dim):
            # Asymmetric quadratic and cubic terms
            f += 0.5 * x[i]**2 + 0.1 * x[i]**3 + 0.05 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Multi-scale periodic modulation with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.3 * np.sin(i * 0.5) * np.cos(j * 0.3) + 0.2 * np.sin(i * j * 0.1)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Fractal-like structure with recursive patterns
        for i in range(self.dim):
            f += 0.1 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i])
            
        # Dynamic scaling based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        scale_factor = 1.0 + 0.5 * np.exp(-dist_from_origin / 3.0)
        f *= scale_factor
        
        # Add noise with varying intensity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(17 * x_norm[i]) * np.cos(19 * x_norm[i]) + 0.03 * np.sin(23 * x_norm[i])
        f += noise
        
        # Enhanced multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.2 * np.sin(8 * x[i]) * np.cos(12 * x[i]) * np.sin(16 * x[i])
            
        # Asymmetric coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.1 * np.abs(x[i] - x[j])) * np.sin(x[i] + x[j])
                f += 0.15 * coupling
                
        # Add higher-order polynomial terms for increased complexity
        f += 0.1 * np.sum(x**4) + 0.05 * np.sum(x**5)
        
        # Introduce irregularity through chaotic modulation
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.08 * np.sin(29 * x_norm[i]) * np.cos(31 * x_norm[i]) * np.sin(37 * x_norm[i])
        f += chaos
        
        return f