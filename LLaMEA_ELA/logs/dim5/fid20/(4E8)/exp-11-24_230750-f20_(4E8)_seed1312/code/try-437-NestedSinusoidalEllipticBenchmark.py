import numpy as np

class NestedSinusoidalEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute nested sinusoidal parameters
        self.sin_freqs = np.random.uniform(1.0, 4.0, dim)
        self.sin_ampls = np.random.uniform(0.5, 2.0, dim)
        self.elliptic_params = np.random.uniform(0.1, 1.0, dim)
        self.quad_couplings = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.nested_offsets = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested sinusoidal modulations with hierarchical structure
        nested_sin = 0.0
        for i in range(self.dim):
            freq = self.sin_freqs[i]
            ampl = self.sin_ampls[i]
            offset = self.nested_offsets[i]
            # Nested modulation: inner sine modulates outer sine
            inner_sin = np.sin(freq * x[i])
            outer_sin = np.sin(2.0 * freq * x[i] + offset)
            nested_sin += ampl * (inner_sin + 0.5 * outer_sin) ** 2
        
        # Dynamic elliptic conditioning with dimension-dependent scaling
        elliptic_cond = 0.0
        for i in range(self.dim):
            param = self.elliptic_params[i]
            # Elliptic term with dynamic eccentricity
            eccentricity = 1.0 + 0.3 * np.sin(0.7 * x[i])
            elliptic_cond += param * (x[i] ** 2) / eccentricity
        
        # Cross-dimensional quadratic couplings with chaotic weights
        quad_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight using tent map
                tent_val = 2.0 * (x[i] % 0.5)
                if x[i] >= 0.5:
                    tent_val = 2.0 * (1.0 - (x[i] % 0.5))
                weight = 1.0 + 0.2 * np.sin(tent_val)
                quad_coupling += weight * self.quad_couplings[i, j] * (x[i] - x[j]) ** 2
        
        # Hierarchical deceptive plateaus using sigmoidal modulation
        plateau = 0.0
        for i in range(self.dim):
            # Create plateaus with varying heights and widths
            plateau_height = 1.0 + 0.5 * np.sin(0.3 * x[i])
            plateau_width = 0.5 + 0.3 * np.cos(0.4 * x[i])
            plateau_term = plateau_height * (1.0 / (1.0 + np.exp(-x[i] / plateau_width)))
            plateau += plateau_term
        
        # Combine all components with adaptive weighting
        return (0.30 * nested_sin + 0.35 * elliptic_cond + 0.25 * quad_coupling + 
                0.10 * plateau)