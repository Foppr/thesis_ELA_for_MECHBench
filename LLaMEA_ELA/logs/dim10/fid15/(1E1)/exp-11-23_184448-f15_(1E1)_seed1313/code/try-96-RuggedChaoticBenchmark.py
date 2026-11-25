import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dimension scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Chaotic sine modulation with exponential weighting
        chaotic_modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            amp = 1.5 + 0.5 * np.cos(i * np.pi / (self.dim + 3))
            chaos = np.sin(x[i] * freq) * np.exp(-0.2 * np.abs(x[i]))
            chaotic_modulation += amp * np.sin(x[i] * (1.0 + 0.3 * chaos)) * np.exp(-0.1 * x[i]**2)
        
        # Polynomial cross-dimension interactions with exponential coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.exp(-0.5 * (i - j)**2 / self.dim)
                poly_coupling += coupling_strength * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Exponential barrier potentials with chaotic positioning
        barriers = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4))
            barrier_height = 2.0 + np.sin(i * np.pi / 3)
            barriers += barrier_height * np.exp(-0.5 * (x[i] - center)**2 / (0.5 + 0.1 * i))
        
        # Multi-scale chaotic perturbation with cosine components
        perturbation = 0.0
        scales = [0.2, 0.5, 1.0, 2.0, 4.0]
        for i in range(self.dim):
            for scale in scales:
                perturbation += np.cos(x[i] / scale) * np.sin(x[i] * scale) * np.exp(-0.05 * scale)
        
        # Add a chaotic ridge term
        ridge_term = 0.0
        for i in range(self.dim - 1):
            ridge_term += np.sin(x[i] + x[i+1]) * np.exp(-0.3 * (x[i]**2 + x[i+1]**2))
        
        # Dimensionality-dependent mixing factor
        mix_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 4)
        
        return mix_factor * (base_term + 0.4 * chaotic_modulation + 0.3 * poly_coupling + 
                            0.5 * barriers + 0.2 * perturbation + 0.1 * ridge_term)