import numpy as np

class ChaoticSinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal components with dynamic frequencies and phase shifts
        chaotic_sin_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.7 * np.sin(i * 0.8) + 0.4 * np.cos(i * 0.5)
            phase = 0.2 * np.sin(i * 1.3) + 0.1 * np.cos(i * 0.9)
            chaotic_sin_sum += np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase) + 0.4 * np.sin(4.0 * freq * x[i] + phase)
        
        # Adaptive radial basis functions with chaotic centers, widths, and weights
        rbf_sum = 0
        for i in range(min(15, self.dim)):
            center = -4.5 + 9.0 * (i / max(1, self.dim - 1)) + 0.6 * np.sin(i * 1.2)
            width = 0.2 + 0.8 * np.abs(np.sin(i * 0.6)) + 0.3 * np.cos(i * 0.4)
            weight = 0.5 + 0.5 * np.sin(i * 0.7)
            rbf_sum += weight * np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # High-order polynomial couplings with chaotic interaction coefficients and cross-terms
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff1 = 0.6 + 0.4 * np.sin(i * 1.0)
            coeff2 = 0.4 + 0.6 * np.cos(i * 0.8)
            poly_coupling += coeff1 * (x[i]**4 * x[i+1]**3) + coeff2 * (x[i] * x[i+1]**5) + 0.2 * (x[i]**2 * x[i+1]**2)
        
        # Complex higher-order polynomial terms with chaotic exponents and multipliers
        poly_terms = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.4 * np.sin(i * 0.9)
            multiplier = 0.01 + 0.02 * np.cos(i * 0.6)
            poly_terms += multiplier * (x[i]**(7 + int(exp_factor * 5)) - 0.03 * x[i]**(6 + int(exp_factor * 4)) + 0.08 * x[i]**(5 + int(exp_factor * 3)) - 0.1 * x[i]**(4 + int(exp_factor * 2)))
        
        # Dynamic cross-dimensional coupling with chaotic weights and additional interaction terms
        cross_coupling = 0
        for i in range(self.dim - 3):
            weight = 0.9 + 0.1 * np.sin(i * 0.7)
            cross_coupling += weight * (x[i] * x[i+1] * x[i+2] * x[i+3])**2 + 0.1 * (x[i]**2 * x[i+1] * x[i+2]**3)
        
        # Global chaotic modulation with multiple frequencies and amplitude scaling
        chaotic_mod = np.sin(0.6 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.15 * np.sum(x**3)) * np.exp(-0.05 * np.sum(np.abs(x)))
        
        # Additional chaotic modulation with periodic components
        periodic_mod = 0.3 * np.sin(0.4 * np.sum(x)) * np.cos(0.3 * np.sum(x**2)) + 0.2 * np.sin(0.2 * np.sum(x**3))
        
        # Combine all components with enhanced chaotic scaling factors
        return 2.5 * chaotic_sin_sum + 1.5 * rbf_sum + 0.6 * poly_coupling + 0.4 * poly_terms + 0.3 * cross_coupling + 0.2 * chaotic_mod + 0.15 * periodic_mod