import numpy as np

class ChaoticAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic component with nested sinusoids and fractal scaling
        f = 0.0
        for i in range(self.dim):
            f += np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.sin(7 * x_norm[i])
            
        # Asymmetric saddle points with dynamic weights and directional bias fields
        for i in range(self.dim):
            # Directional bias with fractal-like modulation
            bias = 0.5 * np.sin(i * 0.7) * np.cos(i * 0.3) * np.sin(i * 0.1)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.3 * np.sinh(x[i]**2)
            
        # Multi-scale nested modulations with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                modulation = np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[j]) * np.exp(-0.1 * (i - j)**2)
                f += 0.3 * modulation * (1 + 0.2 * np.sin(i + j) * np.cos(i - j))
                
        # Dynamic gradient landscape with proximity-based conditioning
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.5))
        scale_factor = 1.0 + 0.8 * np.exp(-proximity / 1.5)
        f *= scale_factor
        
        # Fractal-like complexity with recursive harmonic terms and chaotic perturbations
        for i in range(self.dim):
            f += 0.15 * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i]) * np.sin(19 * x_norm[i])
            
        # Chaotic perturbations with exponential decay and multi-frequency components
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(23 * x_norm[i]) * np.cos(29 * x_norm[i]) * np.sin(31 * x_norm[i]) * np.exp(-0.05 * i)
        f += 0.1 * chaos
        
        # Strengthened global minimum attraction with multi-modal basin structure
        f += 0.25 * np.sum(x**6) + 0.1 * np.sum(np.abs(x)**8)
        
        # Introduce extreme conditioning and interaction between dimensions
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.5 * np.sin(i * 0.2) * np.cos(i * 0.3))
        f *= condition_factor
        
        # Add high-frequency chaotic noise with dimension-dependent scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(41 * x_norm[i]) * np.cos(43 * x_norm[i]) * np.sin(47 * x_norm[i]) * (1.0 + 0.1 * i)
        f += 0.08 * noise
        
        return f