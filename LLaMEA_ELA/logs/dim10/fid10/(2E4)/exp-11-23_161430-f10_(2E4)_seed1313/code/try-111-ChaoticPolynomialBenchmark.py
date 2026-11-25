import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for polynomial chaos with enhanced modulation
        self.chaotic_params = 3.7 + 0.5 * np.sin(np.arange(dim) * 0.7)
        # Enhanced adaptive conditioning factors with different pattern
        self.conditioning_factors = 2.1 + 0.3 * np.cos(np.arange(dim) * 0.9)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos component with chaotic modulation
        poly_chaos = 0.0
        for i in range(self.dim):
            # Enhanced chaotic modulation of polynomial coefficients
            coeff_mod = self.chaotic_params[i] * (1.0 + 0.3 * np.sin(x[i] * 0.7))
            poly_chaos += coeff_mod * (x[i]**6 - 6*x[i]**4 + 9*x[i]**2) * np.exp(-0.2 * x[i]**2)
        
        # Enhanced sinusoidal perturbation with adaptive frequency
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.5 * np.sin(i * 0.5) * self.conditioning_factors[i]
            amp = 0.8 + 0.2 * np.cos(x[i] * 0.6)
            sin_pert += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Enhanced cross-dimensional coupling with modified weights
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            weight = 1.5 + 0.4 * np.sin(i * 0.7) * self.conditioning_factors[i]
            cross_coupling += weight * np.sin(4.2 * x[i]) * np.cos(3.1 * x[j]) * \
                             np.exp(-0.2 * (x[k]**2 + x[i]**2))
        
        # Enhanced adaptive conditioning term with different polynomial
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**5 - 6*x[i]**3 + 12*x[i])
        
        # Combine all components with adjusted weights for better fitness
        result = 0.4 * np.sum(x**2) + 0.6 * poly_chaos + 0.25 * sin_pert + \
                 0.2 * cross_coupling + 0.1 * cond_term
        
        return result