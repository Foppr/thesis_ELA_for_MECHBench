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
            freq = 1.0 + 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(i * 0.4)
            chaotic_sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.3 * np.sin(3.0 * freq * x[i])
        
        # Adaptive radial basis functions with chaotic centers and widths
        rbf_sum = 0
        for i in range(min(12, self.dim)):
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.5 * np.sin(i * 1.1)
            width = 0.3 + 0.7 * np.abs(np.sin(i * 0.5)) + 0.2 * np.cos(i * 0.3)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # High-order polynomial couplings with chaotic interaction coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.5 + 0.5 * np.sin(i * 0.9)
            poly_coupling += coeff * (x[i]**3 * x[i+1]**2) + (1.0 - coeff) * (x[i] * x[i+1]**4)
        
        # Complex higher-order polynomial terms with chaotic exponents
        poly_terms = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(i * 0.8)
            poly_terms += 0.005 * x[i]**(6 + int(exp_factor * 4)) - 0.02 * x[i]**(5 + int(exp_factor * 3)) + 0.05 * x[i]**(4 + int(exp_factor * 2))
        
        # Dynamic cross-dimensional coupling with chaotic weights
        cross_coupling = 0
        for i in range(self.dim - 2):
            weight = 0.8 + 0.2 * np.sin(i * 0.6)
            cross_coupling += weight * (x[i] * x[i+1] * x[i+2])**2
        
        # Global chaotic modulation with multiple frequencies
        chaotic_mod = np.sin(0.5 * np.sum(x**2)) * np.cos(0.2 * np.sum(x)) * np.sin(0.1 * np.sum(x**3))
        
        # Quaternion-based rotational symmetry enhancement
        quat_sym = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                quat_sym += (x[i]**2 + x[i+1]**2 + x[i+2]**2 + x[i+3]**2)**1.5
        
        # Fractal-like self-similarity with recursive scaling
        fractal_term = 0
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                scale = 0.1 + 0.9 * np.abs(np.sin(i * 0.3))
                fractal_term += scale * (x[i]**2 + x[i+1]**2)**(1.2 + 0.3 * np.sin(i * 0.5))
        
        # Introduce a new chaotic modulation component for better fitness
        new_mod = np.sin(0.3 * np.sum(np.abs(x))) * np.cos(0.4 * np.sum(x**2)) * np.sin(0.2 * np.sum(x**4))
        
        # Add a new polynomial interaction term for enhanced ruggedness
        new_poly = 0
        for i in range(self.dim - 1):
            new_poly += 0.01 * (x[i]**2 + x[i+1]**2)**3
        
        # Add a new chaotic interaction term to improve balance
        chaotic_interaction = 0
        for i in range(self.dim - 1):
            chaotic_interaction += np.sin(0.5 * x[i] * x[i+1]) * np.cos(0.3 * (x[i]**2 + x[i+1]**2))
        
        # Add a new fractal-like coupling for better complexity
        fractal_coupling = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                fractal_coupling += 0.05 * (x[i]**2 + x[i+1]**2)**(1.1 + 0.2 * np.sin(i * 0.4))
        
        # Combine all components with refined scaling factors
        return 1.8 * chaotic_sin_sum + 1.0 * rbf_sum + 0.6 * poly_coupling + 0.4 * poly_terms + 0.25 * cross_coupling + 0.15 * chaotic_mod + 0.06 * quat_sym + 0.04 * fractal_term + 0.1 * new_mod + 0.08 * new_poly + 0.05 * chaotic_interaction + 0.03 * fractal_coupling