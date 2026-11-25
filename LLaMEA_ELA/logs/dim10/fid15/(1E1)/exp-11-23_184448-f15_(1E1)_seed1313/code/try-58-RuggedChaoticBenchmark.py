import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x)**2 / (self.dim + 1)))
        
        # Enhanced sine-based chaotic modulation with frequency coupling
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            amp = 1.5 + 0.5 * np.cos(i * np.pi / (self.dim + 3))
            chaos_factor = 0.4 * np.sin(x[i] * freq + 0.5 * np.sum(x[:i+1]))
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor) + 0.3 * np.cos(x[i])) * np.exp(-0.15 * x[i]**2)
        
        # Increased polynomial cross-dimension interactions with varying coupling strengths
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = (i + j) / (self.dim + 1)
                poly_coupling += coupling_strength * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * np.cos((x[i] + x[j]) / 2)
        
        # Adaptive local minima with dynamic positioning and shape
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 5))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            shape_factor = 1.0 + 0.3 * np.sin(x[i] * i)
            local_minima += weight * (x[i]**4 - 2*x[i]**2 + 1) * shape_factor
        
        # Multi-scale chaotic perturbation with phase modulation
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.0, 1.5]:
                phase_shift = np.sin(i * np.pi / (self.dim + 1))
                perturbation += np.sin(x[i] / scale + phase_shift) * np.cos(x[i] * scale + phase_shift)
        
        # Dimensionality-dependent scaling with chaotic factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)