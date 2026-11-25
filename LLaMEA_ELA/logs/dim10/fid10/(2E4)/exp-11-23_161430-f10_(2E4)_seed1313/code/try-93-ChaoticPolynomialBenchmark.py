import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for polynomial chaos
        self.chaotic_params = 3.8 + 0.5 * np.sin(np.arange(dim) * 0.6)
        # Modified adaptive conditioning factors
        self.conditioning_factors = 1.5 + 0.3 * np.cos(np.arange(dim) * 0.8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with chaotic modulation
        poly_chaos = 0.0
        for i in range(self.dim):
            # Chaotic modulation of polynomial coefficients
            coeff_mod = self.chaotic_params[i] * (1.0 + 0.2 * np.sin(x[i]))
            poly_chaos += coeff_mod * (x[i]**5 - 5*x[i]**3 + 6*x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Sinusoidal perturbation with adaptive frequency
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.0 * np.sin(i * 0.4) * self.conditioning_factors[i]
            amp = 0.7 + 0.2 * np.cos(x[i] * 0.5)
            sin_pert += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**3)
        
        # Cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            weight = 1.0 + 0.4 * np.sin(i * 0.6) * self.conditioning_factors[i]
            cross_coupling += weight * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j]) * \
                             np.exp(-0.1 * (x[k]**2 + x[i]**2))
        
        # Adaptive conditioning term
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**4 - 6*x[i]**2 + 9*x[i])
        
        # Combine all components with adjusted weights
        result = 0.3 * np.sum(x**2) + 0.5 * poly_chaos + 0.2 * sin_pert + \
                 0.15 * cross_coupling + 0.08 * cond_term
        
        return result