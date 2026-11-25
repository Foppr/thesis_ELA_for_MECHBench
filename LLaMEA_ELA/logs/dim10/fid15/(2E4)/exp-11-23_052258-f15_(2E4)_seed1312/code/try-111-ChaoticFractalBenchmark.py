import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for stability
        self.fractal_dims = [1.2 + 0.3 * np.sin(i * 0.6) for i in range(dim)]
        self.adaptation_factors = [0.7 + 0.5 * np.cos(i * 0.4) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient flow component with enhanced non-linearity
        chaotic_term = 0.0
        for i in range(self.dim):
            # Enhanced logistic map behavior
            chaos_factor = 4.0 * (x[i] % 1.0) * (1 - x[i] % 1.0)
            chaotic_term += chaos_factor * np.sin(15 * x[i]) * np.cos(7 * x[i])
            
        # Fractal basin boundaries with improved self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal structure using fractional dimensions
            fractal_exp = self.fractal_dims[i % len(self.fractal_dims)]
            fractal_term += (np.abs(x[i])**fractal_exp) * np.sin(3 * np.pi * x[i])
            
        # Adaptive conditioning based on position and dimension with stronger coupling
        adapt_term = 0.0
        for i in range(self.dim):
            # Position-dependent conditioning factor
            cond_factor = self.adaptation_factors[i % len(self.adaptation_factors)]
            adapt_term += cond_factor * (x[i]**2 + 0.15 * np.sin(12 * x[i])**2)
            
        # Cross-dimensional coupling with stronger interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                cross_term += np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] + x[j]))
                
        # High-frequency oscillatory component for fine structure with more complexity
        osc_term = 0.0
        for i in range(self.dim):
            # Multiple frequency components
            freqs = [20.0, 30.0, 40.0, 50.0]
            for freq in freqs:
                osc_term += np.sin(freq * x[i % self.dim]) * np.cos(freq * x[i % self.dim])
                
        # Asymmetric basins with multiple local minima and enhanced complexity
        basin_term = 0.0
        for i in range(self.dim):
            # Create asymmetric parabolic wells with higher non-linearity
            asym = 1.2 + 0.4 * np.sin(0.6 * i)
            basin_term += asym * (x[i] - 0.3 * np.sin(4 * x[i]))**2
            
        # Combine all terms with improved weights for better balance
        weights = [0.35, 0.2, 0.18, 0.12, 0.15]
        total = (weights[0] * chaotic_term + 
                weights[1] * fractal_term + 
                weights[2] * adapt_term + 
                weights[3] * cross_term + 
                weights[4] * basin_term)
                
        # Add global scaling based on dimensionality with modified parameters
        scale = 1.0 + 0.25 * np.log(self.dim + 1) + 0.04 * np.sum(np.abs(x))
        
        return scale * total