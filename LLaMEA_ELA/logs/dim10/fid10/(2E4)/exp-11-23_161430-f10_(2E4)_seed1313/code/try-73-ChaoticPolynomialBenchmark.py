import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for polynomial chaos with enhanced variability
        self.chaotic_params = 3.5 + 1.0 * np.sin(np.arange(dim) * 0.6 + 1.0)
        # Adaptive conditioning factors with improved distribution
        self.conditioning_factors = 1.2 + 0.4 * np.cos(np.arange(dim) * 0.8 + 0.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with enhanced chaotic modulation
        poly_chaos = 0.0
        for i in range(self.dim):
            # Enhanced chaotic modulation of polynomial coefficients
            coeff_mod = self.chaotic_params[i] * (1.0 + 0.15 * np.sin(x[i] * 1.2))
            poly_chaos += coeff_mod * (x[i]**4 - 6*x[i]**2 + 9) * np.exp(-0.05 * x[i]**2)
        
        # Sinusoidal perturbation with increased complexity
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.0 * np.sin(i * 0.4) * self.conditioning_factors[i]
            amp = 0.6 + 0.4 * np.cos(x[i] * 0.7)
            sin_pert += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * \
                       np.sin(0.5 * x[i] * freq)
        
        # Cross-dimensional coupling with enhanced nonlinearity
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            weight = 0.7 + 0.5 * np.sin(i * 0.5) * self.conditioning_factors[i]
            cross_coupling += weight * np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) * \
                             np.exp(-0.1 * (x[k]**2 + x[i]**2)) * \
                             np.tanh(x[i] * x[j])
        
        # Adaptive conditioning term with improved scaling
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning_factors[i] * (x[i]**3 - 3*x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Additional ridge term to improve conditioning
        ridge_term = 0.05 * np.sum(x**4) / self.dim
        
        # Combine all components with adjusted weights for better balance
        result = 0.25 * np.sum(x**2) + 0.35 * poly_chaos + 0.25 * sin_pert + \
                 0.1 * cross_coupling + 0.05 * cond_term + ridge_term
        
        return result