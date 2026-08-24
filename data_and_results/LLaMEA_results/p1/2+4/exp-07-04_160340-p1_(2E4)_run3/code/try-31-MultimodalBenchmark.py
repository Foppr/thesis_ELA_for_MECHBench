import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Create chaotic gradient components using sine and cosine
        grad_x = np.sin(x) * np.cos(2 * x) + 0.1 * np.sin(10 * x)
        
        # Exponentially decaying correlation structure
        corr_factor = np.exp(-0.1 * np.arange(self.dim))
        corr_x = x * corr_factor
        
        # Polynomial terms with varying degrees
        poly_term = np.sum(corr_x**4) + 0.5 * np.sum(corr_x**3) + 0.1 * np.sum(corr_x**2)
        
        # Saddle point structure with multiple interacting dimensions
        saddle_term = np.sum((x**2 - 1)**2) * np.prod(np.cos(x))
        
        # Chaotic perturbation with varying frequency
        chaotic_pert = np.sum(np.sin(5 * x + np.sin(3 * x))**2)
        
        # Add multiple nested local minima with different attraction basins
        minima_positions = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.0] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim)
        ]
        
        # Attraction basin penalty based on distance to minima
        basin_penalty = 0
        for pos in minima_positions:
            dist = np.sum((x - pos)**2)
            basin_penalty += np.exp(-dist / 2.0) / (1.0 + dist)
        
        # Combine all components
        result = poly_term + saddle_term + chaotic_pert + basin_penalty
        
        # Add small random noise to increase robustness testing
        noise = 0.001 * np.random.random()
        
        return result + noise