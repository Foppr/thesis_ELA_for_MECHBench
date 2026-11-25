import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Enhanced sine-based chaotic modulation with higher frequency variations
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.5 + 0.8 * np.cos(i * np.pi / (self.dim + 2))
            chaos_factor = 0.4 * np.sin(x[i] * freq)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.15 * x[i]**2)
        
        # Stronger polynomial cross-dimension interactions with asymmetric coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = (i + 1) * (j + 1) / ((self.dim + 1)**2)
                poly_coupling += coupling_strength * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
        
        # Modified exponentially weighted local minima with chaotic positioning and multiple peaks
        local_minima = 0.0
        for i in range(self.dim):
            center1 = 2.5 * np.sin(i * np.pi / (self.dim + 4))
            center2 = -2.5 * np.cos(i * np.pi / (self.dim + 5))
            weight1 = np.exp(-0.3 * (x[i] - center1)**2)
            weight2 = np.exp(-0.2 * (x[i] - center2)**2)
            local_minima += weight1 * (x[i]**4 - 3*x[i]**2 + 2) + weight2 * (x[i]**3 - x[i])
        
        # Chaotic perturbation with multi-scale sine waves and phase shifts
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.5]:
                phase_shift = np.sin(i * np.pi / (self.dim + 1))
                perturbation += np.sin(x[i] / scale + phase_shift) * np.cos(x[i] * scale + phase_shift)
        
        # Dimensionality-dependent scaling factor with logarithmic growth
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 2)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)