import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic oscillatory components with geometrically varying frequencies
        oscillation_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            freq = 2**(i % 5 + 1)  # Geometric frequency progression
            oscillation_term += np.sin(freq * np.pi * xi) * np.cos(freq * np.pi * xi)
        
        # Fractal-like geometric conditioning with multi-scale interactions
        fractal_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale geometric modulation
            scale1 = 1 + 0.5 * np.sin(7 * np.pi * xi)
            scale2 = 1 + 0.3 * np.cos(11 * np.pi * xi)
            scale3 = 1 + 0.4 * np.sin(13 * np.pi * xi)
            fractal_term += scale1 * scale2 * scale3 * xi**2
        
        # Cross-dimensional coupling with exponential decay and geometric weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Geometric weight based on dimension indices
                weight = 1.0 / (1 + np.exp(2 * (i + j) / self.dim))
                coupling_term += weight * np.exp(-0.5 * (xi**2 + x_norm[j]**2)) * \
                                np.sin(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Multi-scale polynomial with asymmetric curvature and varying exponents
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Varying exponents based on dimension index
            exp1 = 2 + (i % 4)
            exp2 = 3 + (i % 3)
            exp3 = 4 + (i % 2)
            poly_term += (xi**exp1 + 0.5 * xi**exp2 - 0.3 * xi**exp3) * np.exp(-0.1 * xi**2)
        
        # Adaptive conditioning with dimensionality-dependent modulation
        cond_factor = 1.0 + 0.3 * np.sin(np.pi * self.dim / (self.dim + 5))
        
        # Combine all terms with dynamic scaling
        result = 1.2 * oscillation_term + 0.9 * fractal_term + 0.8 * coupling_term + \
                 0.7 * poly_term
        
        # Add global modulation with periodic and multiplicative components
        global_mod = 0.5 * np.sin(5 * np.pi * np.sum(x_norm**2)) * \
                     np.cos(3 * np.pi * np.prod(x_norm))
        
        result = result * cond_factor + global_mod
        
        # Add chaotic perturbation for increased ruggedness
        chaos_perturb = 0.1 * np.sin(47 * np.pi * np.sum(np.abs(x_norm)))
        result += chaos_perturb
        
        return result