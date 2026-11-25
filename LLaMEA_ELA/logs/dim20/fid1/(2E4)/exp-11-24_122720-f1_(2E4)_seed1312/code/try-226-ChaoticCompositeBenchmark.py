import numpy as np

class ChaoticCompositeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced complexity
        self.freq_factors = [2.1 + 0.3 * np.sin(i) for i in range(dim)]
        self.amp_factors = [1.8 + 0.2 * np.cos(i) for i in range(dim)]
        self.cond_factors = [1.0 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.noise_level = 0.015
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multimodal sinusoidal component with chaotic frequency modulation
        sin_sum = 0
        for i in range(self.dim):
            freq = self.freq_factors[i] * (1 + 0.2 * np.sin(i * np.pi / (self.dim + 2)))
            amp = self.amp_factors[i] * (1 + 0.15 * np.cos(i * np.pi / (self.dim + 3)))
            sin_sum += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Radial symmetry component with chaotic scaling
        norm = np.linalg.norm(x)
        if norm > 0:
            rad_component = (norm - 3.0) ** 2 * (1 + 0.25 * np.sin(norm * 0.5) + 0.1 * np.cos(norm * 0.3))
        else:
            rad_component = 0
            
        # Cross-dimensional coupling with chaotic interaction coefficients
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = (1 + 0.1 * np.sin(i * j)) * (1 + 0.05 * np.cos(i + j))
                cross_sum += coeff * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Higher-order polynomial terms with chaotic coefficients (modified with cubic terms)
        poly_sum = 0
        for i in range(self.dim):
            cond = self.cond_factors[i]
            poly_sum += cond * (0.1 * x[i]**4 + 0.02 * x[i]**6 + 0.005 * x[i]**3) * (1 + 0.1 * np.sin(i))
            
        # Adaptive conditioning based on dimensionality
        adapt_cond = 1.0 + 0.3 * np.log(self.dim + 1) + 0.08 * np.sin(np.log(self.dim + 1))
        
        # Noise injection with chaotic perturbation
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.1 * np.cos(self.dim) + 0.05 * np.sin(self.dim ** 1.5))
        
        # Combine all components with proper scaling
        return adapt_cond * (sin_sum + rad_component + cross_sum + poly_sum) + noise + 0.3 * self.dim