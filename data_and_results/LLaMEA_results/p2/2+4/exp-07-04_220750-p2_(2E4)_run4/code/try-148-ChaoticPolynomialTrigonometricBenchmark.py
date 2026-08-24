import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial base with adaptive exponents and radial dependency
        poly_base = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(r * np.pi / 2)
            poly_base += (x_norm[i] ** exp_factor) * np.exp(-0.1 * x_norm[i]**2)
        
        # Modified trigonometric modulation with frequency coupling
        trig_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * np.pi / 3)
            amp = 1.0 + 0.3 * np.cos(i * np.pi / 4)
            trig_mod += amp * np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi)
        
        # Improved chaotic cross-dimensional interaction using logistic map
        chaotic_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                logistic_input = 3.8 * (x_norm[i] + x_norm[j]) % 1.0
                chaotic_cross += np.sin(15 * logistic_input * np.pi) * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Multi-scale sinusoidal peaks with dynamic scaling
        peak_component = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        for i in range(self.dim):
            scale = 1.0 + 0.7 * np.sin(r * np.pi)
            peak_component += scale * np.sin(10 * x_norm[i] * np.pi) * np.cos(7 * x_norm[i] * np.pi)
        
        # Enhanced non-separable interaction terms with dynamic weights
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin((i + j) * np.pi / 4)
                interaction = weight * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * np.sin(4 * x_norm[i] * x_norm[j] * np.pi)
                non_sep += interaction
        
        # Asymmetric polynomial with enhanced chaotic perturbation
        asym_poly = 0.0
        for i in range(self.dim):
            asym_poly += (x_norm[i]**4 + 0.6 * x_norm[i]**3 + 0.2 * x_norm[i]**2) * np.sin(6 * x_norm[i] * np.pi)
        
        # Combine all components with optimized weights
        return 0.35 * poly_base + 0.25 * trig_mod + 0.2 * chaotic_cross + 0.15 * peak_component + 0.05 * non_sep + 0.05 * asym_poly