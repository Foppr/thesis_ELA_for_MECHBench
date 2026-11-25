import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Chaotic sine wave components with dimension-specific frequencies
        for i in range(self.dim):
            freq = self.chaos_params[i] * (1.0 + 0.3 * np.sin(x[i]))
            result += 3.0 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Radial basis functions with adaptive widths
        rbf_sum = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = 0.5 + 0.3 * np.sin(i * 0.5 + np.sum(x) * 0.2)
            distance = np.sum((x - center)**2)
            rbf_sum += self.rbf_weights[i] * np.exp(-distance / (2 * width**2))
        result += 2.5 * rbf_sum
        
        # Adaptive conditioning based on position
        conditioning_factor = 1.0 + 0.5 * np.sin(np.sum(x) * 0.3)
        for i in range(self.dim):
            result += conditioning_factor * (x[i]**4 - 8*x[i]**2 + 16)
            
        # Cross-dimensional coupling with chaotic interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                coupling_sum += coupling
        result += 1.8 * coupling_sum
        
        # Multi-scale fractal-like oscillations
        for i in range(self.dim):
            scale = 2**(i % 3 + 1)
            result += 1.5 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.4) * np.exp(-0.1 * abs(x[i]))
            
        # Asymmetric barrier with chaotic scaling
        barrier_sum = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.8 * np.sin(i * 0.7 + np.sum(x) * 0.3)
            barrier_sum += scale * np.exp(1.5 * (x[i] - 3.0)**2) + scale * np.exp(1.5 * (x[i] + 3.0)**2)
        result += 0.8 * barrier_sum
        
        return result