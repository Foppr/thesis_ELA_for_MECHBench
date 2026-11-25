import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Enhanced sine-based chaotic modulation with dynamic frequencies
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            amp = 1.5 + 0.5 * np.cos(i * np.pi / (self.dim + 3))
            chaos_factor = 0.4 * np.sin(x[i] * freq)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.05 * x[i]**2)
        
        # Adaptive polynomial cross-dimension interactions with varying coupling strengths
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = (i + j) / (self.dim * (self.dim + 1) / 2)
                poly_coupling += coupling_strength * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Self-similar local minima with fractal-like positioning
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * (x[i]**4 - 3*x[i]**2 + 2)
        
        # Multi-scale chaotic perturbation with varying amplitudes
        perturbation = 0.0
        scales = [0.25, 0.5, 1.0, 2.0, 4.0]
        for i in range(self.dim):
            for scale in scales:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * (1.0 / scale)
        
        # Dimensionality-dependent complexity factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.25 * poly_coupling + 
                            0.35 * local_minima + 0.15 * perturbation)