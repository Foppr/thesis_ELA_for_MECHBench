import numpy as np

class ChaoticAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic component with nested sinusoids
        f = 0.0
        for i in range(self.dim):
            f += np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.sin(7 * x_norm[i])
            
        # Asymmetric saddle points with dynamic weights
        for i in range(self.dim):
            # Asymmetric quadratic terms with directional bias
            bias = 0.5 * np.sin(i * 0.7)  # Directional bias
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.3 * np.sinh(x[i]**2)
            
        # Nested multi-scale modulations
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                modulation = np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[j])
                f += 0.2 * modulation * (1 + 0.1 * np.sin(i + j))
                
        # Dynamic gradient landscape based on proximity to critical points
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.5))
        scale_factor = 1.0 + 0.5 * np.exp(-proximity / 2.0)
        f *= scale_factor
        
        # Fractal-like complexity with recursive harmonic terms
        for i in range(self.dim):
            f += 0.1 * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i]) * np.sin(19 * x_norm[i])
            
        # Chaotic perturbations
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(23 * x_norm[i]) * np.cos(29 * x_norm[i]) * np.sin(31 * x_norm[i])
        f += 0.05 * chaos
        
        # Strengthened global minimum attraction
        f += 0.2 * np.sum(x**6)
        
        return f