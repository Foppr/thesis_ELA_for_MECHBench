import numpy as np

class NestedFractalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute nested fractal parameters
        self.cos_freqs = np.random.uniform(2.0, 6.0, dim)
        self.cos_ampls = np.random.uniform(1.0, 3.0, dim)
        self.fractal_params = np.random.uniform(0.05, 0.5, dim)
        self.cos_couplings = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.fractal_offsets = np.random.uniform(-2.0, 2.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal cosine modulations with hierarchical structure
        nested_cos = 0.0
        for i in range(self.dim):
            freq = self.cos_freqs[i]
            ampl = self.cos_ampls[i]
            offset = self.fractal_offsets[i]
            # Fractal modulation: inner cosine modulates outer cosine
            inner_cos = np.cos(freq * x[i])
            outer_cos = np.cos(3.0 * freq * x[i] + offset)
            nested_cos += ampl * (inner_cos + 0.3 * outer_cos) ** 3
        
        # Dynamic fractal conditioning with dimension-dependent scaling
        fractal_cond = 0.0
        for i in range(self.dim):
            param = self.fractal_params[i]
            # Fractal term with dynamic scaling
            scale_factor = 1.0 + 0.4 * np.cos(0.5 * x[i])
            fractal_cond += param * (x[i] ** 2) / scale_factor
        
        # Cross-dimensional cosine couplings with chaotic weights
        cos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight using logistic map
                logistic_val = 3.8 * (x[i] % 0.25)
                if x[i] >= 0.25:
                    logistic_val = 3.8 * (1.0 - (x[i] % 0.25))
                weight = 1.0 + 0.15 * np.cos(logistic_val)
                cos_coupling += weight * self.cos_couplings[i, j] * (x[i] - x[j]) ** 2
        
        # Hierarchical deceptive gradients using exponential modulation
        gradient = 0.0
        for i in range(self.dim):
            # Create exponential plateaus with varying steepness
            steepness = 1.0 + 0.6 * np.cos(0.5 * x[i])
            gradient_term = np.exp(-steepness * (x[i] ** 2)) * (1.0 + 0.3 * np.sin(0.4 * x[i]))
            gradient += gradient_term
        
        # Combine all components with adaptive weighting
        return (0.25 * nested_cos + 0.30 * fractal_cond + 0.25 * cos_coupling + 
                0.20 * gradient)