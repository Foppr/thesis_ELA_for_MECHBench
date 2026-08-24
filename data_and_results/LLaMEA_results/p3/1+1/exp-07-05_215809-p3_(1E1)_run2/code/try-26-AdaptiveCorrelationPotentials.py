import numpy as np

class AdaptiveCorrelationPotentials:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base multimodal component with hyperbolic tangent potentials
        f = 0.0
        for i in range(self.dim):
            f += np.tanh(3 * x[i]) * np.sin(5 * x[i]) * np.cos(7 * x[i])
            
        # Adaptive correlation structure with dimension-specific weights
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.sin(i * 0.3)  # Varying importance per dimension
            f += weight * (x[i]**4 - 2 * x[i]**2 + 1) * np.tanh(x[i])
            
        # Periodic interaction terms with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.3 * np.cos(i * 0.5) * np.sin(j * 0.7)  # Adaptive coupling
                interaction = np.tanh(x[i] + x[j]) * np.sin(2 * x[i] - x[j])
                f += coupling * interaction
                
        # Multi-scale harmonic modulations with dynamic frequency
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.4)
            f += 0.2 * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.tanh(x[i])
            
        # Separability control through dimension-wise conditioning
        condition_number = 1.0 + 2.0 * np.sin(0.2 * self.dim)
        for i in range(self.dim):
            f += 0.1 * (x[i]**2) * (1 + 0.1 * np.sin(i * 0.6)) * condition_number
            
        # Fractal-like self-similarity with recursive scaling
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        f *= scale_factor
        
        # Chaotic perturbations with exponential decay
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[i]) * np.tanh(2 * x[i])
        f += 0.03 * chaos
        
        # Strengthened global minimum attraction
        f += 0.15 * np.sum(x**8)
        
        return f