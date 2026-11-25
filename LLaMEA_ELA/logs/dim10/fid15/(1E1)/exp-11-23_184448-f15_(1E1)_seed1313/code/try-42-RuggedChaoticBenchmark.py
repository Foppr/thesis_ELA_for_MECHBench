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
            amp = 1.5 + 0.8 * np.cos(i * np.pi / (self.dim + 2))
            chaos_factor = 0.5 * np.sin(x[i] * freq)
            modulated_term += amp * np.sin(x[i] * (1.0 + chaos_factor)) * np.exp(-0.15 * x[i]**2)
        
        # Higher-order polynomial cross-dimension interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * (i + j)**2
        
        # Exponentially weighted local minima with chaotic positioning and multiple peaks
        local_minima = 0.0
        for i in range(self.dim):
            center1 = 2.5 * np.sin(i * np.pi / (self.dim + 3))
            center2 = -2.5 * np.cos(i * np.pi / (self.dim + 4))
            weight1 = np.exp(-0.3 * (x[i] - center1)**2)
            weight2 = np.exp(-0.3 * (x[i] - center2)**2)
            local_minima += weight1 * (x[i]**5 - 3*x[i]**3 + 2*x[i]) + weight2 * (x[i]**4 - 2*x[i]**2 + 1)
        
        # Multi-scale fractal perturbation with chaotic frequency modulation
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.3, 0.7, 1.0, 1.5, 2.0]:
                freq_mod = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 5))
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale * freq_mod)
        
        # Chaotic dimensionality scaling with fractal-like behavior
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 7.0)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)