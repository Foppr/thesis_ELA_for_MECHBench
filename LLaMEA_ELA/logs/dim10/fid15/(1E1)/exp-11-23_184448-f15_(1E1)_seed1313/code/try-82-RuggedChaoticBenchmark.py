import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x)**2 / (self.dim + 1)))
        
        # Enhanced sine-based chaotic modulation with dynamic frequencies and amplitudes
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            amp = 1.0 + 0.7 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 5))
            chaos_factor = 0.4 * np.sin(x[i] * freq) * np.cos(x[i] * 0.5)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.15 * x[i]**2)
        
        # Adaptive polynomial cross-dimension interactions with variable coupling strengths
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin((i + j) * np.pi / (self.dim + 1))
                poly_coupling += coupling_strength * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Multi-scale exponentially weighted local minima with fractal-like positioning
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 5))
            scale = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 6))
            weight = np.exp(-0.5 * ((x[i] - center) / scale)**2)
            local_minima += weight * (x[i]**4 - 3*x[i]**2 + 2)
        
        # Multi-scale chaotic perturbation with varying amplitudes and frequencies
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.5, 2.5]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 1)))
        
        # Dimensionality-dependent scaling factor with chaotic modulation
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) * np.sin(self.dim * np.pi / (self.dim + 2))
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)