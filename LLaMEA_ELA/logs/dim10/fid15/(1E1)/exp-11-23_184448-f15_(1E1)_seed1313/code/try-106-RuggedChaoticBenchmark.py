import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Sine-based chaotic modulation with varying frequencies and amplitudes
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            amp = 0.5 + 1.5 * np.cos(i * np.pi / (self.dim + 2))
            chaos_factor = 0.4 * np.sin(x[i] * freq)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.15 * x[i]**2)
        
        # Polynomial cross-dimension interactions with non-linear coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * (i + j)**1.5
        
        # Exponentially weighted local minima with chaotic positioning and multiple peaks
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
        
        # Chaotic perturbation with multi-scale sine waves and radial basis components
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.5, 3.0]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale)
        
        # Radial basis function component for additional ruggedness
        radial_term = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                radial_term += np.exp(-0.2 * (x[i] - centers[i])**2) * np.sin(x[i]**2)
        
        # Dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation + 0.1 * radial_term)