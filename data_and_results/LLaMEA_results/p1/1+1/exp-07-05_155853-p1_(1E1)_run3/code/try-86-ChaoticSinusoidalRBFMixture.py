import numpy as np

class ChaoticSinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal components with dynamic frequencies
        chaotic_sin_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.6 * np.sin(i * 0.8) + 0.2 * np.cos(i * 0.3)
            chaotic_sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.2 * np.sin(4.0 * freq * x[i])
        
        # Adaptive radial basis functions with chaotic centers and widths
        rbf_sum = 0
        for i in range(min(10, self.dim)):
            center = -4.5 + 9.0 * (i / max(1, self.dim - 1)) + 0.4 * np.sin(i * 1.2)
            width = 0.2 + 0.8 * np.abs(np.sin(i * 0.6)) + 0.1 * np.cos(i * 0.4)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # High-order polynomial couplings with chaotic interaction coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.4 + 0.6 * np.sin(i * 1.0)
            poly_coupling += coeff * (x[i]**4 * x[i+1]**2) + (1.0 - coeff) * (x[i] * x[i+1]**5)
        
        # Complex higher-order polynomial terms with chaotic exponents
        poly_terms = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.4 * np.sin(i * 0.7)
            poly_terms += 0.006 * x[i]**(7 + int(exp_factor * 5)) - 0.025 * x[i]**(6 + int(exp_factor * 4)) + 0.06 * x[i]**(5 + int(exp_factor * 3))
        
        # Dynamic cross-dimensional coupling with chaotic weights
        cross_coupling = 0
        for i in range(self.dim - 2):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)
            cross_coupling += weight * (x[i] * x[i+1] * x[i+2])**2
        
        # Global chaotic modulation with multiple frequencies
        chaotic_mod = np.sin(0.6 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.15 * np.sum(x**3))
        
        # Combine all components with chaotic scaling factors
        return 2.2 * chaotic_sin_sum + 1.3 * rbf_sum + 0.6 * poly_coupling + 0.35 * poly_terms + 0.25 * cross_coupling + 0.15 * chaotic_mod