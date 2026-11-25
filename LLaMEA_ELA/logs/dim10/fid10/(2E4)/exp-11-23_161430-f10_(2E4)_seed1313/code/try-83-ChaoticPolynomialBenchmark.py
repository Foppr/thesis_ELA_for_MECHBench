import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher modulation
        self.chaotic_params = 4.0 + 0.8 * np.sin(np.arange(dim) * 0.6)
        # Improved conditioning factors with greater variation
        self.conditioning_factors = 1.5 + 0.5 * np.cos(np.arange(dim) * 0.8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos component with higher-order terms
        poly_chaos = 0.0
        for i in range(self.dim):
            coeff_mod = self.chaotic_params[i] * (1.0 + 0.2 * np.sin(x[i]))
            poly_chaos += coeff_mod * (x[i]**5 - 5*x[i]**3 + 6*x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Modified sinusoidal perturbation with frequency modulation
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(i * 0.4) * self.conditioning_factors[i]
            amp = 0.7 + 0.3 * np.cos(x[i] * 0.5)
            sin_pert += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Enhanced cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            weight = 1.0 + 0.4 * np.sin(i * 0.6) * self.conditioning_factors[i]
            cross_coupling += weight * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j]) * \
                             np.exp(-0.1 * (x[k]**2 + x[i]**2))
        
        # Enhanced conditioning term with cubic and quintic components
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**6 - 6*x[i]**4 + 9*x[i]**2)
        
        # Combine all components with adjusted weights
        result = 0.3 * np.sum(x**2) + 0.5 * poly_chaos + 0.2 * sin_pert + \
                 0.15 * cross_coupling + 0.08 * cond_term
        
        return result