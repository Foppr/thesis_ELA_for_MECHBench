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
            freq = 1.2 + 0.4 * np.sin(i * 0.6) + 0.2 * np.cos(i * 0.5)
            chaotic_sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.25 * np.sin(3.0 * freq * x[i])
        
        # Adaptive radial basis functions with altered centers and widths
        rbf_sum = 0
        for i in range(min(12, self.dim)):
            center = -4.5 + 9.0 * (i / max(1, self.dim - 1)) + 0.4 * np.sin(i * 1.2)
            width = 0.2 + 0.6 * np.abs(np.sin(i * 0.4)) + 0.15 * np.cos(i * 0.2)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # High-order polynomial couplings with modified coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.4 + 0.6 * np.sin(i * 1.0)
            poly_coupling += coeff * (x[i]**3 * x[i+1]**2) + (1.0 - coeff) * (x[i] * x[i+1]**4)
        
        # Complex higher-order polynomial terms with altered exponents
        poly_terms = 0
        for i in range(self.dim):
            exp_factor = 1.1 + 0.2 * np.sin(i * 0.7)
            poly_terms += 0.006 * x[i]**(6 + int(exp_factor * 4)) - 0.025 * x[i]**(5 + int(exp_factor * 3)) + 0.04 * x[i]**(4 + int(exp_factor * 2))
        
        # Dynamic cross-dimensional coupling with adjusted weights
        cross_coupling = 0
        for i in range(self.dim - 2):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)
            cross_coupling += weight * (x[i] * x[i+1] * x[i+2])**2
        
        # Global chaotic modulation with new frequencies
        chaotic_mod = np.sin(0.4 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.15 * np.sum(x**3))
        
        # Quaternion-based rotational symmetry enhancement
        quat_sym = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                quat_sym += (x[i]**2 + x[i+1]**2 + x[i+2]**2 + x[i+3]**2)**1.5
        
        # Fractal-like self-similarity with modified scaling
        fractal_term = 0
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                scale = 0.15 + 0.85 * np.abs(np.sin(i * 0.4))
                fractal_term += scale * (x[i]**2 + x[i+1]**2)**(1.3 + 0.2 * np.sin(i * 0.6))
        
        # Introduce a new chaotic modulation component
        new_mod = np.sin(0.25 * np.sum(np.abs(x))) * np.cos(0.35 * np.sum(x**2)) * np.sin(0.15 * np.sum(x**4))
        
        # Add a new polynomial interaction term with different scaling
        new_poly = 0
        for i in range(self.dim - 1):
            new_poly += 0.015 * (x[i]**2 + x[i+1]**2)**3
        
        # Combine all components with updated scaling factors
        return 1.7 * chaotic_sin_sum + 1.1 * rbf_sum + 0.5 * poly_coupling + 0.35 * poly_terms + 0.2 * cross_coupling + 0.12 * chaotic_mod + 0.07 * quat_sym + 0.05 * fractal_term + 0.12 * new_mod + 0.09 * new_poly