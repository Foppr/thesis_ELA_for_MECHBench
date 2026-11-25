import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Radial sinusoidal component with varying frequencies
        radius = np.sqrt(np.sum(x**2))
        radial_sin = np.sin(3 * radius) * np.cos(7 * radius) * np.exp(-radius / 5)
        
        # Polynomial chaos with mixed exponents and coefficients
        poly_chaos = (np.sum(x**8) / (8 * self.dim) + 
                     np.sum(x**5) / (5 * self.dim) + 
                     np.sum(x**3) / (3 * self.dim) + 
                     0.5 * np.sum(x**2) / self.dim)
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.sin(x[i]) * np.cos(x[i+1]) * np.exp(-abs(x[i] - x[i+1]))
        cross_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation using sine and cosine products
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(2 * x[i]) * np.cos(5 * x[i]) * 
                           np.sin(3 * x[i]) * np.cos(4 * x[i]))
        multi_scale /= self.dim
        
        # Add a nested structure with multiple local minima using trigonometric combinations
        nested = 0.0
        for i in range(self.dim):
            nested += np.sin(10 * x[i]) * np.cos(8 * x[i]) + 0.3 * np.sin(6 * x[i])
        nested /= self.dim
        
        # Combine all components with a global scaling factor
        result = (poly_chaos + cross_coupling + multi_scale + nested + 
                 radial_sin * 0.5)
        
        # Add chaotic perturbation around the global minimum to increase difficulty
        chaos_perturb = 0.1 * np.sum(np.sin(12 * x) * np.cos(9 * x) * np.exp(-x**2)) / self.dim
        result += chaos_perturb
        
        return float(result)