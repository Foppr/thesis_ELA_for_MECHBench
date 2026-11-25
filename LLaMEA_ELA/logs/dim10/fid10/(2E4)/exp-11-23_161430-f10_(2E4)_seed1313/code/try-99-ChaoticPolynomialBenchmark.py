import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for polynomial chaos with slight modification
        self.chaotic_params = 3.9 + 0.4 * np.sin(np.arange(dim) * 0.65)
        # Modified adaptive conditioning factors with different pattern
        self.conditioning_factors = 1.7 + 0.2 * np.cos(np.arange(dim) * 0.85)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with chaotic modulation
        poly_chaos = 0.0
        for i in range(self.dim):
            # Chaotic modulation of polynomial coefficients
            coeff_mod = self.chaotic_params[i] * (1.0 + 0.25 * np.sin(x[i]))
            poly_chaos += coeff_mod * (x[i]**5 - 5*x[i]**3 + 6*x[i]) * np.exp(-0.18 * x[i]**2)
        
        # Sinusoidal perturbation with adaptive frequency
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 3.2 + 1.2 * np.sin(i * 0.45) * self.conditioning_factors[i]
            amp = 0.75 + 0.15 * np.cos(x[i] * 0.55)
            sin_pert += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**3)
        
        # Cross-dimensional coupling with modified weights
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            weight = 1.1 + 0.35 * np.sin(i * 0.65) * self.conditioning_factors[i]
            cross_coupling += weight * np.sin(3.5 * x[i]) * np.cos(2.5 * x[j]) * \
                             np.exp(-0.12 * (x[k]**2 + x[i]**2))
        
        # Adaptive conditioning term with different polynomial
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**4 - 5*x[i]**2 + 8*x[i])
        
        # Combine all components with adjusted weights
        result = 0.35 * np.sum(x**2) + 0.55 * poly_chaos + 0.22 * sin_pert + \
                 0.17 * cross_coupling + 0.09 * cond_term
        
        return result