import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar polynomial pattern with varying exponents
        poly_pattern = np.sum((x**2 + 0.1 * x**3 + 0.01 * x**5) ** 2)
        
        # Logarithmic barrier terms to create sharp gradients near boundaries
        log_barrier = np.sum(1.0 / (1.0 + np.exp(-10.0 * (np.abs(x) - 4.5))))
        
        # Quaternion-inspired rotational symmetries in high-dimensional space
        rot_symmetry = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi, yi = x[i], x[i+1]
                rot_symmetry += (xi**2 + yi**2) * np.sin(np.arctan2(yi, xi))
        
        # Multi-scale fractal component with recursive scaling
        fractal = 0.0
        for scale in [0.5, 1.0, 2.0]:
            scaled_x = x * scale
            fractal += np.sum(np.sin(scaled_x) * np.cos(scaled_x**2)) / scale
        
        # Saddle-point inducing cross-term interactions with inverse distance weighting
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                if dist > 0:
                    saddle_interaction += (x[i]**2 + x[j]**2) / dist
        
        # Adaptive Gaussian modulation based on local variance
        local_variance = np.var(x)
        gaussian_mod = np.sum(np.exp(-0.5 * (x**2) / (1.0 + local_variance)))
        
        # Degenerate minimum enhancement via piecewise linear mapping
        degenerate_term = np.sum(np.abs(x - np.round(x / 0.5) * 0.5))
        
        return poly_pattern + log_barrier + rot_symmetry + fractal + saddle_interaction + gaussian_mod + degenerate_term