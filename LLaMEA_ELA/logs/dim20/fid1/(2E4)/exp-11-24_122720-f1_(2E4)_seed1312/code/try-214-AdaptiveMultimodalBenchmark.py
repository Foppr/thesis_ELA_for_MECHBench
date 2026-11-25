import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning_factors = np.linspace(0.5, 2.0, dim)
        self.interaction_strength = 0.3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying exponents
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            exp_factor = 2 + 0.5 * np.sin(i)
            poly_sum += self.conditioning_factors[i] * (xi ** exp_factor)
            
        # Trigonometric component with dynamic frequencies
        trig_sum = 0
        for i in range(self.dim):
            xi = x[i]
            freq = 1.0 + 0.3 * np.cos(i) + 0.2 * np.sin(i * 0.5)
            trig_sum += np.sin(freq * xi) * np.cos(freq * xi)
            
        # Radial component with multiple harmonic terms
        radius = np.linalg.norm(x)
        if radius == 0:
            radial_sum = 0
        else:
            radial_sum = (radius ** 2) * (
                1 + 0.4 * np.sin(radius) + 
                0.3 * np.cos(2 * radius) + 
                0.2 * np.sin(3 * radius) +
                0.1 * np.cos(4 * radius)
            )
            
        # Cross-dimensional interaction with dynamic weights
        interaction_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = self.interaction_strength * (1 + 0.1 * np.sin(i + j))
                interaction_sum += weight * np.exp(-dist ** 2) * np.sin(dist)
                
        # Adaptive conditioning component
        adaptive_sum = 0
        for i in range(self.dim):
            xi = x[i]
            adaptive_factor = 1.0 + 0.2 * np.sin(xi) * np.cos(xi)
            adaptive_sum += adaptive_factor * xi ** 3
            
        # Combine all components with dynamic scaling
        total_components = [poly_sum, trig_sum, radial_sum, interaction_sum, adaptive_sum]
        weights = [1.0, 0.7, 1.2, 0.8, 0.9]
        
        result = sum(w * comp for w, comp in zip(weights, total_components))
        
        # Add dimensionality-dependent penalty
        penalty = 0.05 * self.dim * np.sum(np.abs(x))
        
        return result + penalty + 0.1 * np.random.rand()