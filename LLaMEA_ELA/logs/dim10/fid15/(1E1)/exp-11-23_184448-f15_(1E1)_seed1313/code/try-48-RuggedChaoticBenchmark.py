import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with conditioning
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Enhanced sine-based chaotic modulation with frequency mixing
        modulated_term = 0.0
        for i in range(self.dim):
            freq1 = 1.0 + 1.5 * np.sin(i * np.pi / (self.dim + 2))
            freq2 = 0.5 + 0.5 * np.cos(i * np.pi / (self.dim + 3))
            amp = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 4))
            chaos_factor = 0.4 * np.sin(x[i] * freq1) * np.cos(x[i] * freq2)
            modulated_term += amp * np.sin(x[i] * (1.0 + 0.5 * chaos_factor)) * np.exp(-0.05 * x[i]**2)
        
        # Modified polynomial cross-dimension interactions with asymmetric coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = (i + 1) * (j + 1) / ((self.dim + 1)**2)
                poly_coupling += coupling_strength * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Improved exponentially weighted local minima with chaotic positioning and multiple peaks
        local_minima = 0.0
        for i in range(self.dim):
            center1 = 2.5 * np.sin(i * np.pi / (self.dim + 4))
            center2 = -2.5 * np.cos(i * np.pi / (self.dim + 5))
            weight1 = np.exp(-0.3 * (x[i] - center1)**2)
            weight2 = np.exp(-0.2 * (x[i] - center2)**2)
            local_minima += weight1 * (x[i]**4 - 3*x[i]**2 + 1) + weight2 * (x[i]**6 - 4*x[i]**4 + 4*x[i]**2)
        
        # Multi-scale chaotic perturbation with varying amplitudes
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.5, 3.0]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * (1.0 + 0.2 * np.sin(i * np.pi / self.dim))
        
        # Dimensionality-dependent scaling with curvature adjustment
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)