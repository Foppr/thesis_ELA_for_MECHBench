import numpy as np

class ChaoticSinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sinusoidal components with higher frequency modulation
        chaotic_sin_sum = 0
        for i in range(self.dim):
            freq = 1.5 + 0.7 * np.sin(i * 0.8) + 0.4 * np.cos(i * 0.5)
            chaotic_sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.4 * np.sin(4.0 * freq * x[i]) + 0.2 * np.cos(2.0 * freq * x[i]**3)
        
        # Modified adaptive radial basis functions with chaotic variance and dynamic centers
        rbf_sum = 0
        for i in range(min(15, self.dim)):
            center = -4.5 + 9.0 * (i / max(1, self.dim - 1)) + 0.6 * np.sin(i * 1.2)
            width = 0.2 + 0.8 * np.abs(np.sin(i * 0.6)) + 0.3 * np.cos(i * 0.4)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2) * (1.0 + 0.1 * np.sin(i * 0.3))
        
        # Increased high-order polynomial couplings with chaotic interaction coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.6 + 0.4 * np.sin(i * 1.0)
            poly_coupling += coeff * (x[i]**4 * x[i+1]**3) + (1.0 - coeff) * (x[i] * x[i+1]**5)
        
        # Enhanced higher-order polynomial terms with chaotic exponents and increased complexity
        poly_terms = 0
        for i in range(self.dim):
            exp_factor = 1.2 + 0.4 * np.sin(i * 0.9)
            poly_terms += 0.008 * x[i]**(7 + int(exp_factor * 5)) - 0.03 * x[i]**(6 + int(exp_factor * 4)) + 0.07 * x[i]**(5 + int(exp_factor * 3)) - 0.05 * x[i]**(4 + int(exp_factor * 2))
        
        # Stronger dynamic cross-dimensional coupling with chaotic weights and increased interaction
        cross_coupling = 0
        for i in range(self.dim - 2):
            weight = 0.9 + 0.1 * np.sin(i * 0.7)
            cross_coupling += weight * (x[i] * x[i+1] * x[i+2])**3
        
        # Global chaotic modulation with multiple frequencies and enhanced amplitude
        chaotic_mod = np.sin(0.6 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.15 * np.sum(x**3)) * np.cos(0.25 * np.sum(x**4))
        
        # Quaternion-based rotational symmetry enhancement with increased dimensionality
        quat_sym = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                quat_sym += (x[i]**2 + x[i+1]**2 + x[i+2]**2 + x[i+3]**2)**2.0
        
        # Fractal-like self-similarity with recursive scaling and higher-order terms
        fractal_term = 0
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                scale = 0.15 + 0.85 * np.abs(np.sin(i * 0.4))
                fractal_term += scale * (x[i]**2 + x[i+1]**2)**(1.5 + 0.4 * np.sin(i * 0.6))
        
        # New chaotic modulation component with additional frequency harmonics
        new_mod = np.sin(0.4 * np.sum(np.abs(x))) * np.cos(0.5 * np.sum(x**2)) * np.sin(0.25 * np.sum(x**4)) * np.cos(0.3 * np.sum(x**5))
        
        # Additional polynomial interaction term with higher-order coupling
        new_poly = 0
        for i in range(self.dim - 1):
            new_poly += 0.02 * (x[i]**2 + x[i+1]**2)**4
        
        # Additional cross-dimensional coupling with cubic interactions
        cubic_coupling = 0
        for i in range(self.dim - 3):
            cubic_coupling += 0.05 * (x[i] * x[i+1] * x[i+2] * x[i+3])**2
        
        # Combine all components with refined scaling factors
        return 2.0 * chaotic_sin_sum + 1.2 * rbf_sum + 0.8 * poly_coupling + 0.5 * poly_terms + 0.3 * cross_coupling + 0.2 * chaotic_mod + 0.08 * quat_sym + 0.06 * fractal_term + 0.12 * new_mod + 0.1 * new_poly + 0.07 * cubic_coupling