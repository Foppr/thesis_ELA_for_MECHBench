import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for stability
        self.fractal_dims = [1.3 + 0.2 * np.sin(i * 0.5) for i in range(dim)]
        self.adaptation_factors = [0.8 + 0.4 * np.cos(i * 0.3) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient flow component
        chaotic_term = 0.0
        for i in range(self.dim):
            # Logistic map-like behavior for chaotic dynamics
            chaos_factor = 3.8 * (x[i] % 1.0) * (1 - x[i] % 1.0)
            chaotic_term += chaos_factor * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Fractal basin boundaries with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal structure using fractional dimensions
            fractal_exp = self.fractal_dims[i % len(self.fractal_dims)]
            fractal_term += (np.abs(x[i])**fractal_exp) * np.sin(2 * np.pi * x[i])
            
        # Adaptive conditioning based on position and dimension
        adapt_term = 0.0
        for i in range(self.dim):
            # Position-dependent conditioning factor
            cond_factor = self.adaptation_factors[i % len(self.adaptation_factors)]
            adapt_term += cond_factor * (x[i]**2 + 0.1 * np.sin(10 * x[i])**2)
            
        # Cross-dimensional coupling with non-linear interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                cross_term += np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
                
        # High-frequency oscillatory component for fine structure
        osc_term = 0.0
        for i in range(self.dim):
            # Multiple frequency components
            freqs = [15.0, 25.0, 35.0]
            for freq in freqs:
                osc_term += np.sin(freq * x[i % self.dim]) * np.cos(freq * x[i % self.dim])
                
        # Asymmetric basins with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            # Create asymmetric parabolic wells
            asym = 1.0 + 0.3 * np.sin(0.5 * i)
            basin_term += asym * (x[i] - 0.2 * np.sin(3 * x[i]))**2
            
        # Combine all terms with dimension-dependent weights
        weights = [0.4, 0.25, 0.15, 0.1, 0.1]
        total = (weights[0] * chaotic_term + 
                weights[1] * fractal_term + 
                weights[2] * adapt_term + 
                weights[3] * cross_term + 
                weights[4] * basin_term)
                
        # Add global scaling based on dimensionality
        scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.03 * np.sum(np.abs(x))
        
        return scale * total