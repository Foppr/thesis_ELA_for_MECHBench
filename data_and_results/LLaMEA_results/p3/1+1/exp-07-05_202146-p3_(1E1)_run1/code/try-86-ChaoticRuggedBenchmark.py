import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic coefficients for cross-dimensional interactions
        self.periodic_coeffs = np.array([np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Multi-modal sinusoidal components with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.3 * np.sin(7.0 * x[i])
            
        # Cross-dimensional interaction with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * self.periodic_coeffs[i] * self.periodic_coeffs[j]
                result += 0.1 * interaction
                
        # Chaotic perturbation using logistic map-like dynamics
        chaotic_pert = 0.0
        for i in range(self.dim):
            chaotic_pert += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i])
        result += chaotic_pert
        
        # Fractal-like scaling with recursive structure
        fractal_scale = 1.0
        for i in range(self.dim):
            fractal_scale *= (1.0 + 0.1 * np.sin(4.0 * x[i]))
        result += 0.15 * fractal_scale
        
        # Memory-dependent term with exponential decay
        if hasattr(self, 'prev_x'):
            memory_term = 0.0
            for i in range(self.dim):
                memory_term += 0.05 * (x[i] - self.prev_x[i])**2
            result += memory_term
        self.prev_x = x.copy()
        
        # Global minimum perturbation with chaotic attractor
        attractor = 0.0
        for i in range(self.dim):
            attractor += 0.1 * np.sin(15 * x[i]) * np.cos(8 * x[i])
        result += attractor
        
        # Add high-frequency noise to increase ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.08 * np.sin(25 * x[i]) * np.cos(12 * x[i])
        result += noise
        
        return result