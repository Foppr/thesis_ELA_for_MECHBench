import numpy as np

class ChaoticSinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal components with modified frequencies
        chaotic_sin_sum = 0
        for i in range(self.dim):
            freq = 1.2 + 0.4 * np.sin(i * 0.6) + 0.2 * np.cos(i * 0.3)
            chaotic_sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.25 * np.sin(3.0 * freq * x[i])
        
        # Adaptive radial basis functions with shifted centers and widths
        rbf_sum = 0
        for i in range(min(10, self.dim)):
            center = -3.5 + 7.0 * (i / max(1, self.dim - 1)) + 0.4 * np.sin(i * 1.2)
            width = 0.2 + 0.6 * np.abs(np.sin(i * 0.4)) + 0.1 * np.cos(i * 0.2)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # High-order polynomial couplings with modified coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.4 + 0.6 * np.sin(i * 0.8)
            poly_coupling += coeff * (x[i]**4 * x[i+1]**2) + (1.0 - coeff) * (x[i] * x[i+1]**3)
        
        # Complex higher-order polynomial terms with modified exponents
        poly_terms = 0
        for i in range(self.dim):
            exp_factor = 1.1 + 0.2 * np.sin(i * 0.7)
            poly_terms += 0.006 * x[i]**(5 + int(exp_factor * 5)) - 0.025 * x[i]**(4 + int(exp_factor * 2)) + 0.04 * x[i]**(3 + int(exp_factor * 1))
        
        # Dynamic cross-dimensional coupling with modified weights
        cross_coupling = 0
        for i in range(self.dim - 2):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)
            cross_coupling += weight * (x[i] * x[i+1] * x[i+2])**1.5
        
        # Global chaotic modulation with new frequencies
        chaotic_mod = np.sin(0.4 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.15 * np.sum(x**3))
        
        # Quaternion-based rotational symmetry enhancement
        quat_sym = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                quat_sym += (x[i]**2 + x[i+1]**2 + x[i+2]**2 + x[i+3]**2)**1.4
        
        # Fractal-like self-similarity with altered scaling
        fractal_term = 0
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                scale = 0.15 + 0.85 * np.abs(np.sin(i * 0.25))
                fractal_term += scale * (x[i]**2 + x[i+1]**2)**(1.3 + 0.2 * np.sin(i * 0.4))
        
        # Introduce a new chaotic modulation component
        new_mod = np.sin(0.25 * np.sum(np.abs(x))) * np.cos(0.35 * np.sum(x**2)) * np.sin(0.15 * np.sum(x**4))
        
        # Add a new polynomial interaction term
        new_poly = 0
        for i in range(self.dim - 1):
            new_poly += 0.015 * (x[i]**2 + x[i+1]**2)**2.5
        
        # Combine all components with adjusted scaling factors
        return 1.9 * chaotic_sin_sum + 1.1 * rbf_sum + 0.5 * poly_coupling + 0.35 * poly_terms + 0.3 * cross_coupling + 0.18 * chaotic_mod + 0.07 * quat_sym + 0.05 * fractal_term + 0.12 * new_mod + 0.09 * new_poly