import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x)**2 / (self.dim + 1)))
        
        # Enhanced sine-based chaotic modulation with multi-frequency components
        modulated_term = 0.0
        for i in range(self.dim):
            freq1 = 1.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            freq2 = 2.0 + np.cos(i * np.pi / (self.dim + 3))
            amp = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 4))
            chaos_factor = 0.5 * np.sin(x[i] * freq1) + 0.3 * np.cos(x[i] * freq2)
            modulated_term += amp * np.sin(x[i] * (1.0 + 0.5 * chaos_factor)) * np.exp(-0.05 * x[i]**2)
        
        # Higher-order polynomial cross-dimension interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * (i + j)**2
        
        # Adaptive local minima with chaotic positioning and varying depths
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 5))
            depth = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 6))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += depth * weight * (x[i]**4 - 2*x[i]**2 + 1)
        
        # Multi-scale chaotic perturbation with asymmetric components
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += np.sin(x[i]) * np.cos(x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
            perturbation += 0.3 * np.sin(x[i] * 2.0) * np.cos(x[i] * 0.7) * np.exp(-0.05 * x[i]**2)
        
        # Dimensionality-dependent complexity factor with chaotic variation
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / (self.dim + 1))
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.25 * poly_coupling + 
                            0.35 * local_minima + 0.15 * perturbation)