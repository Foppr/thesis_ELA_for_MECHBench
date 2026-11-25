import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.polynomial_degree = 5
        self.fractal_dimension = 1.3
        self.ridge_strength = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with adaptive weights
        poly_term = 0.0
        for i in range(self.dim):
            # Use Legendre polynomials up to degree 5
            legendre_vals = [1, x[i]]
            if self.polynomial_degree > 1:
                for j in range(2, self.polynomial_degree + 1):
                    legendre_vals.append(((2*j - 1) * x[i] * legendre_vals[-1] - (j - 1) * legendre_vals[-2]) / j)
            poly_term += np.sum([legendre_vals[j] * np.sin(i * j * 0.5) for j in range(len(legendre_vals))])
        
        # Fractal Brownian motion component with varying Hurst parameter
        fbm_term = 0.0
        hurst = self.fractal_dimension / self.dim
        for i in range(self.dim):
            # Simple fractal-like behavior using sine and cosine with different frequencies
            fbm_term += np.sin(x[i] * (1 + 0.5 * np.sin(i))) * np.cos(x[i] * (1 + 0.3 * np.cos(i)))
            fbm_term += np.sin(x[i] * 2) * np.cos(x[i] * 1.5)
        
        # Adaptive ridge interactions with dynamic coupling
        ridge_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1 * (x[i] + x[j])**2)
                # Adaptive ridge strength based on dimension
                strength = self.ridge_strength * (1 + 0.3 * np.sin(i * j * 0.2))
                ridge_term += strength * np.exp(-dist**2) * np.sin(dist)
        
        # Multi-scale oscillatory component with varying amplitudes
        osc_term = 0.0
        for i in range(self.dim):
            scale = 1 + 0.5 * np.sin(i * 0.7)
            osc_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale**2)
        
        # Asymmetric exponential decay with dynamic phase shifts
        asym_term = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.8) + 0.3 * np.cos(i * 0.5)
            asym_term += np.exp(-0.3 * (x[i] - phase_shift)**2) * np.sin(3 * x[i]) * np.cos(x[i])
        
        # Global scaling factor with multi-modal influence
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.2)
        
        return global_scale * (0.25 * poly_term + 0.2 * fbm_term + 0.25 * ridge_term + 0.15 * osc_term + 0.15 * asym_term)