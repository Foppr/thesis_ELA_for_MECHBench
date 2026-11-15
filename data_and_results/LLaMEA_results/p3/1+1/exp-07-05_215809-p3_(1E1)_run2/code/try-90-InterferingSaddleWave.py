import numpy as np

class InterferingSaddleWave:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic wave component with varying frequencies and amplitudes
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with varying bias and non-linear terms
        for i in range(self.dim):
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.2 * np.sinh(x[i]**2)
            
        # Multi-scale interference patterns with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.1 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.05 * np.sin(i * j * 0.1)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Dynamic scaling based on distance from reference points
        scale_factor = 1.0
        for i in range(self.dim):
            dist = np.abs(x[i] - np.sin(i * 0.4)) + 0.1 * np.abs(x[i] - np.cos(i * 0.6))
            scale_factor *= (1.0 + 0.5 * np.exp(-dist / 0.8))
        f *= scale_factor
        
        # Fractal-like periodic components with recursive structure
        for i in range(self.dim):
            f += 0.1 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i])
            
        # Chaotic modulation with exponential decay and varying sensitivity
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.exp(-0.3 * x[i]**2) * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i])
        f += 0.15 * chaos
        
        # Additional multi-modal structure with periodic peaks and valleys
        for i in range(self.dim):
            f += 0.25 * np.sin(8 * x[i]) * np.cos(12 * x[i]) * np.sin(16 * x[i])
            
        # Asymmetric coupling between dimensions with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1 + 0.2 * np.sin(i + j))
                f += coupling
                
        # Enhanced global minimum attraction with higher-order polynomial terms
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Additional noise components with irregular harmonic patterns
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(29 * x_norm[i]) * np.cos(31 * x_norm[i]) + 0.03 * np.sin(37 * x_norm[i])
        f += noise
        
        return f