import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly modified fractal parameters for increased complexity
        self.fractal_dims = [1.3 + 0.2 * np.sin(i * 0.7) for i in range(dim)]
        self.adaptation_factors = [0.8 + 0.4 * np.cos(i * 0.5) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient flow with modified non-linearity
        chaotic_term = 0.0
        for i in range(self.dim):
            # Modified logistic map behavior
            chaos_factor = 3.8 * (x[i] % 1.0) * (1 - x[i] % 1.0)
            chaotic_term += chaos_factor * np.sin(17 * x[i]) * np.cos(9 * x[i])
            
        # Fractal basin boundaries with altered self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Modified multi-scale fractal structure
            fractal_exp = self.fractal_dims[i % len(self.fractal_dims)]
            fractal_term += (np.abs(x[i])**fractal_exp) * np.sin(4 * np.pi * x[i])
            
        # Adaptive conditioning with stronger coupling
        adapt_term = 0.0
        for i in range(self.dim):
            # Enhanced position-dependent conditioning factor
            cond_factor = self.adaptation_factors[i % len(self.adaptation_factors)]
            adapt_term += cond_factor * (x[i]**2 + 0.2 * np.sin(14 * x[i])**2)
            
        # Extended cross-dimensional coupling with higher interaction strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                cross_term += np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2) * np.cos(0.6 * (x[i] + x[j]))
                
        # Enhanced high-frequency oscillatory component
        osc_term = 0.0
        for i in range(self.dim):
            # Additional frequency components
            freqs = [22.0, 33.0, 44.0, 55.0, 66.0]
            for freq in freqs:
                osc_term += np.sin(freq * x[i % self.dim]) * np.cos(freq * x[i % self.dim])
                
        # Modified asymmetric basins with increased complexity
        basin_term = 0.0
        for i in range(self.dim):
            # Altered asymmetric parabolic wells
            asym = 1.3 + 0.3 * np.sin(0.7 * i)
            basin_term += asym * (x[i] - 0.35 * np.sin(5 * x[i]))**2
            
        # Combine all terms with adjusted weights for better balance
        weights = [0.38, 0.22, 0.19, 0.14, 0.17]
        total = (weights[0] * chaotic_term + 
                weights[1] * fractal_term + 
                weights[2] * adapt_term + 
                weights[3] * cross_term + 
                weights[4] * basin_term)
                
        # Modified global scaling based on dimensionality
        scale = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sum(np.abs(x))
        
        return scale * total