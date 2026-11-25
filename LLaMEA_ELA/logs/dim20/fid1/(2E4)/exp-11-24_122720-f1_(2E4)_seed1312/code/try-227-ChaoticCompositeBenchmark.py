import numpy as np

class ChaoticCompositeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced complexity
        self.freq_factors = [2.0 + 0.4 * np.sin(i * 1.3) for i in range(dim)]
        self.amp_factors = [1.5 + 0.3 * np.cos(i * 0.7) for i in range(dim)]
        self.cond_factors = [1.0 + 0.6 * np.sin(i * np.pi / (dim + 2)) for i in range(dim)]
        self.noise_level = 0.012
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multimodal sinusoidal component with chaotic frequency modulation
        sin_sum = 0
        for i in range(self.dim):
            freq = self.freq_factors[i] * (1 + 0.25 * np.sin(i * 0.8))
            amp = self.amp_factors[i] * (1 + 0.2 * np.cos(i * 0.6))
            sin_sum += amp * np.sin(freq * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Radial symmetry component with enhanced chaotic scaling
        norm = np.linalg.norm(x)
        if norm > 0:
            rad_component = (norm - 2.5) ** 2 * (1 + 0.3 * np.sin(norm * 0.6) + 0.15 * np.cos(norm * 0.4))
        else:
            rad_component = 0
            
        # Cross-dimensional coupling with improved interaction coefficients
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = (1 + 0.15 * np.sin(i * j * 0.5)) * (1 + 0.08 * np.cos(i + j * 0.3))
                cross_sum += coeff * np.sin(0.4 * x[i]) * np.cos(0.25 * x[j]) * np.exp(-0.03 * abs(x[i] - x[j]))
                
        # Higher-order polynomial terms with improved chaotic coefficients
        poly_sum = 0
        for i in range(self.dim):
            cond = self.cond_factors[i]
            poly_sum += cond * (0.12 * x[i]**4 + 0.015 * x[i]**6) * (1 + 0.12 * np.sin(i * 0.9))
            
        # Adaptive conditioning based on dimensionality with improved scaling
        adapt_cond = 1.0 + 0.25 * np.log(self.dim + 1) + 0.09 * np.sin(np.log(self.dim + 1) * 0.8)
        
        # Noise injection with enhanced chaotic perturbation
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.12 * np.cos(self.dim * 0.7) + 0.06 * np.sin(self.dim ** 1.3))
        
        # Combine all components with proper scaling and reduced bias
        return adapt_cond * (sin_sum + rad_component + cross_sum + poly_sum) + noise + 0.25 * self.dim