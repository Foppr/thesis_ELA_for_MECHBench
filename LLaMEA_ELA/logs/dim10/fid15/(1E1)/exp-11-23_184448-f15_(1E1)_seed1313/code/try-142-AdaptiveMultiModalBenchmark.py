import numpy as np

class AdaptiveMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component with adaptive conditioning
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Multi-scale sinusoidal oscillations with varying frequencies and amplitudes
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 2))
            oscillation_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive conditioning with dimensionality-dependent scaling
        condition_term = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            condition_term += condition_factor * x[i]**4
        
        # Multi-modal structure with varying local minima depths and positions
        modal_term = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 3))
            depth = 0.5 + 0.5 * np.cos(i * np.pi / (self.dim + 4))
            modal_term += depth * (x[i] - center)**6
        
        # Cross-term interactions with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin((i + j) * np.pi / (self.dim + 1))
                cross_term += coupling * x[i]**2 * x[j]**2
        
        # Asymmetric landscape with reflection symmetry breaking
        asymmetry_term = 0.0
        for i in range(self.dim):
            asymmetry_term += (x[i] ** 3) * np.sin(x[i] * np.pi / 2)
        
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (0.2 * radial_term + 0.3 * oscillation_term + 
                            0.15 * condition_term + 0.2 * modal_term + 
                            0.1 * cross_term + 0.05 * asymmetry_term)