import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Sine-based chaotic modulation with altered frequencies and amplitudes
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 1.5 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            amp = 1.2 + 0.8 * np.cos(i * np.pi / (self.dim + 3))
            chaos_factor = 0.4 * np.sin(x[i] * freq)
            modulated_term += amp * np.sin(x[i] * (1.2 + chaos_factor)) * np.exp(-0.15 * x[i]**2)
        
        # Modified polynomial cross-dimension interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * (i + j)**0.5
        
        # Exponentially weighted local minima with shifted centers
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 4)) + 0.5
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * (x[i]**4 - 3*x[i]**2 + 2)
        
        # Chaotic perturbation with additional harmonic components
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.5, 2.5]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * np.exp(-0.05 * x[i]**2)
        
        # Dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.25 * poly_coupling + 
                            0.35 * local_minima + 0.15 * perturbation)