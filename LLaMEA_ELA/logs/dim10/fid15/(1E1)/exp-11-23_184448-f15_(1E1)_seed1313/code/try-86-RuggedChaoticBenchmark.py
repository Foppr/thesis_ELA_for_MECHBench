import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Quaternion-based chaotic modulation with complex interactions
        modulated_term = 0.0
        for i in range(self.dim):
            # Use quaternion-like components for richer modulation
            freq1 = 1.0 + 1.5 * np.sin(i * np.pi / (self.dim + 1))
            freq2 = 1.0 + 1.5 * np.cos(i * np.pi / (self.dim + 2))
            amp = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 3))
            chaos_factor1 = 0.4 * np.sin(x[i] * freq1)
            chaos_factor2 = 0.4 * np.cos(x[i] * freq2)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor1 + 0.5 * chaos_factor2)) * np.exp(-0.05 * x[i]**2)
        
        # Higher-order polynomial cross-dimension interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    poly_coupling += (x[i]**3 + x[j]**3 + x[k]**3) * np.sin(x[i] * x[j] * x[k]) * (i + j + k)
        
        # Multi-scale exponentially weighted local minima with quaternion positioning
        local_minima = 0.0
        for i in range(self.dim):
            center1 = 2.5 * np.sin(i * np.pi / (self.dim + 4))
            center2 = 2.5 * np.cos(i * np.pi / (self.dim + 5))
            weight1 = np.exp(-0.3 * (x[i] - center1)**2)
            weight2 = np.exp(-0.3 * (x[i] - center2)**2)
            local_minima += (weight1 + weight2) * (x[i]**5 - 3*x[i]**3 + 2*x[i]**2 + 1)
        
        # Multi-scale chaotic perturbation with complex sine/cosine combinations
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.25, 0.5, 1.0, 2.0, 4.0]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * np.sin(x[i] * scale**0.5)
        
        # Dimensionality-dependent scaling factor with exponential growth
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * (self.dim ** 1.5)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)