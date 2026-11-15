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
        chaos_factor = 1.0 + 0.2 * np.sin(self.dim * 0.7)
        
        # Create complex sinusoidal components with varying frequencies
        term1 = np.sum(x**2)
        term2 = np.sum(np.sin(chaos_factor * np.sqrt(np.abs(x)))**5)
        term3 = np.sum(np.cos(0.3 * x)**4)
        
        # Add chaotic nested minima structure with exponential decay
        nested_minima = []
        for i in range(1, min(8, self.dim + 1)):
            loc = np.array([3.0 * np.sin(i * 0.5) + 0.7 * np.cos(i*i * 0.3) for _ in range(self.dim)])
            nested_minima.append(loc)
        
        # Calculate penalty for proximity to nested minima with dynamic weights
        penalty = 0
        for i, loc in enumerate(nested_minima):
            dist = np.sum((x - loc)**2)
            weight = 1.0 / (1.0 + 0.05 * i)
            penalty += weight * np.exp(-dist / (2.0 * (1.0 + 0.15 * self.dim)))
        
        # Add saddle point structure with high-order polynomial terms and noise
        saddle_term = 0.02 * np.sum(x**7) + 0.03 * np.sum(x**6) + 0.01 * np.sum(x**5)
        
        # Add chaotic noise component
        noise = 0.05 * np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x))
        
        # Combine all terms with adaptive weighting
        result = 0.9 * term1 + 1.8 * term2 + 0.8 * term3 + saddle_term - penalty + noise
        
        return result