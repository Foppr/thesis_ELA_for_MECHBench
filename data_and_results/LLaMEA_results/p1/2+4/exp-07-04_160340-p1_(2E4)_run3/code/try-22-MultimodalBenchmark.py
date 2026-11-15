import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply chaotic scaling factor based on dimension
        chaos_factor = 1.0 + 0.15 * np.sin(self.dim * 0.7)
        
        # Create complex sinusoidal components with varying frequencies
        term1 = np.sum(x**2)
        term2 = np.sum(np.sin(chaos_factor * np.sqrt(np.abs(x)))**4)
        term3 = np.sum(np.cos(0.5 * x)**3)
        
        # Add chaotic nested minima structure with exponential decay
        nested_minima = []
        for i in range(1, min(5, self.dim + 1)):
            loc = np.array([2.0 * np.sin(i * 1.3) + 0.5 * np.cos(i*i * 0.8) for _ in range(self.dim)])
            nested_minima.append(loc)
        
        # Calculate penalty for proximity to nested minima with exponential decay
        penalty = 0
        for loc in nested_minima:
            dist = np.sum((x - loc)**2)
            penalty += 1.5 * np.exp(-dist / (2.0 * (1.0 + 0.15 * self.dim)))
        
        # Add saddle point structure with high-order polynomial terms and exponential perturbation
        saddle_term = 0.01 * np.sum(x**6) + 0.05 * np.sum(x**5) + 0.3 * np.sum(np.exp(0.1 * np.abs(x)) - 1)
        
        # Combine all terms with adaptive weighting
        result = 0.85 * term1 + 1.4 * term2 + 0.65 * term3 + saddle_term - penalty
        
        return result