import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base component with varying exponents
        poly_base = 0.0
        for i in range(self.dim):
            poly_base += (x_norm[i] ** (2 + i % 3)) * np.exp(-0.1 * x_norm[i]**2)
        
        # Trigonometric modulation with varying frequencies and amplitudes
        trig_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.5
            amp = 1.0 + 0.2 * np.sin(i * np.pi / 4)
            trig_mod += amp * np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi)
        
        # Chaotic cross-dimensional interaction using tent map
        chaotic_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tent_input = 2.0 * np.abs(x_norm[i] + x_norm[j]) % 1.0
                chaotic_cross += np.sin(10 * tent_input * np.pi) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Multi-scale sinusoidal peaks with radial dependency
        peak_component = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(r * np.pi)
            peak_component += scale * np.sin(8 * x_norm[i] * np.pi) * np.cos(6 * x_norm[i] * np.pi)
        
        # Non-separable interaction terms with exponential decay
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * np.sin(3 * x_norm[i] * x_norm[j] * np.pi)
                non_sep += interaction
        
        # Asymmetric polynomial with chaotic perturbation
        asym_poly = 0.0
        for i in range(self.dim):
            asym_poly += (x_norm[i]**3 + 0.5 * x_norm[i]**2) * np.sin(5 * x_norm[i] * np.pi)
        
        # Combine all components with adaptive weights
        return 0.4 * poly_base + 0.3 * trig_mod + 0.2 * chaotic_cross + 0.15 * peak_component + 0.1 * non_sep + 0.05 * asym_poly