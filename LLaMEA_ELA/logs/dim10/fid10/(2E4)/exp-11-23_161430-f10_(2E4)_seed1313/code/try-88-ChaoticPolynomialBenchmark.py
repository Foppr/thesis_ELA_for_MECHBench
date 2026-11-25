import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Highly chaotic parameters with extreme modulation
        self.chaotic_params = 6.0 + 1.2 * np.sin(np.arange(dim) * 0.9)
        # Severely distorted conditioning factors with extreme variation
        self.conditioning_factors = 3.0 + 2.0 * np.cos(np.arange(dim) * 1.2)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Ultra-high-order polynomial chaos component
        poly_chaos = 0.0
        for i in range(self.dim):
            coeff_mod = self.chaotic_params[i] * (1.0 + 0.5 * np.sin(x[i]))
            poly_chaos += coeff_mod * (x[i]**7 - 7*x[i]**5 + 15*x[i]**3 - 9*x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Intensely frequency-modulated sinusoidal perturbation
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(i * 0.7) * self.conditioning_factors[i]
            amp = 1.2 + 0.8 * np.cos(x[i] * 0.8)
            sin_pert += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**3)
        
        # Ultra-strong cross-dimensional coupling with multi-scale interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            l = (i + 4) % self.dim
            weight = 2.0 + 0.8 * np.sin(i * 0.9) * self.conditioning_factors[i]
            cross_coupling += weight * np.sin(5.0 * x[i]) * np.cos(3.0 * x[j]) * \
                             np.exp(-0.15 * (x[k]**2 + x[l]**2 + x[i]**2))
        
        # Severely distorted conditioning term with higher-order components
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**8 - 8*x[i]**6 + 20*x[i]**4 - 16*x[i]**2)
        
        # Combine all components with adjusted weights
        result = 0.5 * np.sum(x**2) + 0.7 * poly_chaos + 0.3 * sin_pert + \
                 0.25 * cross_coupling + 0.15 * cond_term
        
        return result