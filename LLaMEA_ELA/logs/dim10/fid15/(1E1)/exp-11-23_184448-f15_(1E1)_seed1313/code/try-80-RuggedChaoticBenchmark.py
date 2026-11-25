import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dimensionality scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Enhanced sine-based chaotic modulation with adaptive frequencies
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.5 * np.sin(i * np.pi / (self.dim + 2))
            amp = 1.2 + 0.8 * np.cos(i * np.pi / (self.dim + 3))
            chaos_factor = 0.4 * np.sin(x[i] * freq)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.15 * x[i]**2)
        
        # Improved polynomial cross-dimension interactions with weighted coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + 1) * (j + 1) / ((self.dim + 1)**2)
                poly_coupling += weight * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Refined exponentially weighted local minima with chaotic positioning
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 4))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * (x[i]**4 - 3*x[i]**2 + 2)
        
        # Multi-scale chaotic perturbation with enhanced complexity
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.5, 3.0]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * (1.0 + 0.2 * np.sin(i))
        
        # Additional ruggedness through fractional polynomial terms
        fractional_term = 0.0
        for i in range(self.dim):
            fractional_term += 0.5 * x[i]**1.5 * np.cos(x[i])
        
        # Combined dimensionality-dependent scaling
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.25 * modulated_term + 0.15 * poly_coupling + 
                            0.35 * local_minima + 0.1 * perturbation + 0.1 * fractional_term)