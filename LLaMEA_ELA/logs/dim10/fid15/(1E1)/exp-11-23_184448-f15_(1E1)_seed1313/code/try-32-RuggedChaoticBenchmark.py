import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x**2) / self.dim))
        
        # Enhanced sine-based chaotic modulation with dynamic frequencies
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1)) + 0.5 * np.cos(i * np.pi / (self.dim + 2))
            amp = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            chaos_factor = 0.4 * np.sin(x[i] * freq) * np.cos(x[i] * 0.5)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.05 * x[i]**2)
        
        # Adaptive polynomial cross-dimension interactions with variable coupling strength
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin((i + j) * np.pi / (self.dim + 1))
                poly_coupling += coupling_strength * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * (i + j)
        
        # Multi-scale exponentially weighted local minima with chaotic positioning
        local_minima = 0.0
        for i in range(self.dim):
            center1 = 2.5 * np.sin(i * np.pi / (self.dim + 4))
            center2 = -2.5 * np.cos(i * np.pi / (self.dim + 5))
            weight1 = np.exp(-0.3 * (x[i] - center1)**2)
            weight2 = np.exp(-0.2 * (x[i] - center2)**2)
            local_minima += (weight1 * (x[i]**4 - 2*x[i]**2 + 1) + 
                           weight2 * (x[i]**3 - x[i])**2)
        
        # Multi-scale chaotic perturbation with varying amplitudes
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.0, 1.5]:
                amp = 0.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
                perturbation += amp * np.sin(x[i] / scale) * np.cos(x[i] * scale)
        
        # Dimensionality-dependent scaling with chaotic factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.25 * poly_coupling + 
                            0.35 * local_minima + 0.15 * perturbation)