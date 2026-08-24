import numpy as np

class ChaoticRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        chaotic_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.0 + 0.3 * np.cos(i * 0.4)
            chaotic_sum += amp * np.sin(freq * x[i] + np.sin(0.5 * x[i]))
        
        # Radial basis functions with chaotic centers and widths
        rbf_sum = 0
        for i in range(min(12, self.dim)):
            center = 5.0 * np.sin(i * 0.3) * np.cos(i * 0.2)
            width = 0.2 + 0.8 * np.sin(i * 0.5)**2
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Cross-dimensional polynomial coupling with chaotic interaction coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.5 + 0.5 * np.sin(i * 0.6)
            poly_coupling += coeff * (x[i] * x[i+1])**3 + 0.1 * (x[i] + x[i+1])**4
        
        # High-order polynomial terms with chaotic exponents
        poly_terms = 0
        for i in range(self.dim):
            exp_val = 2 + 2 * np.sin(i * 0.3)
            poly_terms += 0.02 * x[i]**exp_val - 0.03 * x[i]**(exp_val - 1) + 0.01 * x[i]**(exp_val - 2)
        
        # Global chaotic modulation with multiple periodic components
        global_mod = np.cos(0.2 * np.sum(x**2)) * np.sin(0.1 * np.sum(x)) * np.exp(-0.1 * np.sum(x**2))
        
        # Asymmetric noise injection to increase conditioning difficulty
        noise = 0
        for i in range(self.dim):
            if x[i] > 0:
                noise += 0.05 * np.random.random() * np.sin(i * 0.8)
            else:
                noise += 0.03 * np.random.random() * np.cos(i * 0.6)
        
        # Combine all components with varying weights
        return 2.0 * chaotic_sum + 0.5 * rbf_sum + 0.4 * poly_coupling + 0.3 * poly_terms + 0.2 * global_mod + 0.1 * noise