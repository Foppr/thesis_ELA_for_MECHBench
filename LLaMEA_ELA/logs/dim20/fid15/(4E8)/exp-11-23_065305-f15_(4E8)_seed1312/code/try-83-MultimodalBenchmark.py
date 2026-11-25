import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential radial basis component with multiple centers
        radius = np.sqrt(np.sum(x**2))
        exp_radial = np.exp(-radius / 3) * np.sin(2 * radius) * np.cos(4 * radius)
        
        # Trigonometric cross-dimensional coupling with varying interaction strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
        cross_term /= (self.dim * (self.dim - 1) / 2)
        
        # Nested fractal-like structure with sinusoidal modulation
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(7 * x[i])
        fractal /= self.dim
        
        # Multi-scale chaotic modulation using product of sinusoids with different frequencies
        chaos_mod = 0.0
        for i in range(self.dim):
            chaos_mod += (np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i]) * 
                         np.cos(4 * x[i]) * np.exp(-x[i]**2 / 10))
        chaos_mod /= self.dim
        
        # Polynomial component with mixed powers for increased curvature
        poly_component = (np.sum(x**6) / (6 * self.dim) + 
                         np.sum(x**4) / (4 * self.dim) + 
                         np.sum(x**2) / (2 * self.dim))
        
        # Add a global scaling factor and combine all components
        result = (poly_component + cross_term + fractal + chaos_mod + 
                 exp_radial * 0.3)
        
        # Add chaotic perturbation to increase optimization difficulty
        perturb = 0.05 * np.sum(np.sin(15 * x) * np.cos(10 * x) * np.exp(-x**2 / 5))
        result += perturb
        
        return float(result)