import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Fractal-like chaotic modulation with nested sine waves
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 1.5 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.0 + 0.8 * np.cos(i * np.pi / (self.dim + 2))
            chaos_factor = 0.4 * np.sin(x[i] * freq)
            nested_chaos = np.sin(x[i] * (1.0 + chaos_factor + 0.3 * np.sin(x[i] * freq * 2)))
            modulated_term += amp * nested_chaos * np.exp(-0.05 * x[i]**2)
        
        # Higher-order polynomial cross-dimension interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    poly_coupling += (x[i]**3 + x[j]**3 + x[k]**3) * np.sin(x[i] * x[j] * x[k]) * (i + j + k)
        
        # Adaptive local minima with fractal positioning
        local_minima = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * np.pi / (self.dim + 4))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * (x[i]**5 - 3*x[i]**3 + 2*x[i]**2 - x[i])
        
        # Multi-scale chaotic perturbation with fractal frequency modulation
        perturbation = 0.0
        for i in range(self.dim):
            for scale in [0.25, 0.5, 1.0, 2.0]:
                perturbation += np.sin(x[i] / scale) * np.cos(x[i] * scale) * np.sin(x[i] * scale * 3)
        
        # Dimensionality-dependent scaling with fractal factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        return dim_factor * (base_term + 0.4 * modulated_term + 0.3 * poly_coupling + 
                            0.5 * local_minima + 0.2 * perturbation)