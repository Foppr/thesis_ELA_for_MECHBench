import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dimensionality scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Nested sine-based chaotic modulation with fractal frequency patterns
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            amp = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 4))
            chaos_factor = 0.5 * np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.05 * x[i]**2)
        
        # Higher-order polynomial cross-dimension interactions with chaotic coupling coefficients
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(i * j * np.pi / (self.dim + 1)) * np.cos(i + j)
                poly_coupling += (x[i]**3 + x[j]**3) * coupling * np.sin(x[i] * x[j])
        
        # Exponentially weighted local minima with fractal positioning and multi-scale chaos
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 5)) * np.cos(i * np.pi / (self.dim + 6))
            weight = np.exp(-0.3 * (x[i] - center)**2) * (1.0 + 0.2 * np.sin(x[i] * 2.0))
            local_minima += weight * (x[i]**5 - 3*x[i]**3 + 2*x[i])
        
        # Multi-scale chaotic perturbation with nested sine waves and dynamic phase shifts
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.25, 0.5, 1.0, 2.0, 4.0]:
                phase_shift = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
                perturbation += np.sin(x[i] / scale + phase_shift) * np.cos(x[i] * scale + phase_shift)
        
        # Dimensionality-dependent scaling factor with chaotic component
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / (self.dim + 1))
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)