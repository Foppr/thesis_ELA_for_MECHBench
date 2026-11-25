import numpy as np

class NestedFractalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute nested fractal parameters
        self.fractal_dims = np.random.uniform(0.1, 0.9, dim)
        self.cos_freqs = np.random.uniform(2.0, 8.0, dim)
        self.cos_ampls = np.random.uniform(1.0, 3.0, dim)
        self.adaptive_params = np.random.uniform(0.5, 2.0, dim)
        self.fractal_couplings = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.nested_offsets = np.random.uniform(-2.0, 2.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal peaks with chaotic dimensionality
        fractal_peak = 0.0
        for i in range(self.dim):
            fractal_dim = self.fractal_dims[i]
            # Fractal-like behavior using power law modulations
            power_term = np.abs(x[i]) ** (1.0 + 0.5 * np.sin(0.5 * x[i]))
            fractal_peak += (1.0 + 0.3 * np.cos(3.0 * x[i])) * power_term
            
        # Dynamic cosine modulations with chaotic frequency variations
        cos_modulation = 0.0
        for i in range(self.dim):
            freq = self.cos_freqs[i]
            ampl = self.cos_ampls[i]
            offset = self.nested_offsets[i]
            # Chaotic frequency modulation using logistic map
            logistic_val = 4.0 * (x[i] % 0.25)
            if x[i] >= 0.25:
                logistic_val = 4.0 * (1.0 - (x[i] % 0.25))
            freq_mod = freq * (1.0 + 0.1 * np.sin(logistic_val))
            cos_modulation += ampl * np.cos(freq_mod * x[i] + offset)
        
        # Adaptive conditioning with dimension-dependent scaling
        adaptive_cond = 0.0
        for i in range(self.dim):
            param = self.adaptive_params[i]
            # Adaptive eccentricity based on fractal dimension
            eccentricity = 1.0 + 0.4 * np.sin(0.6 * x[i]) * self.fractal_dims[i]
            adaptive_cond += param * (x[i] ** 2) / eccentricity
        
        # Cross-dimensional fractal couplings with chaotic weights
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight using logistic map
                logistic_val = 3.8 * (x[i] % 0.3)
                if x[i] >= 0.3:
                    logistic_val = 3.8 * (1.0 - (x[i] % 0.3))
                weight = 1.0 + 0.3 * np.sin(logistic_val)
                fractal_coupling += weight * self.fractal_couplings[i, j] * np.abs(x[i] - x[j]) ** (1.5 + 0.2 * np.cos(0.8 * x[i]))
        
        # Hierarchical deceptive gradients using fractal sigmoidal modulation
        gradient = 0.0
        for i in range(self.dim):
            # Create fractal plateaus with varying dimensions
            plateau_height = 1.5 + 0.7 * np.sin(0.4 * x[i])
            plateau_width = 0.3 + 0.2 * np.cos(0.6 * x[i])
            # Fractal sigmoidal term
            fractal_sigmoid = plateau_height / (1.0 + np.exp(-x[i] / plateau_width))
            gradient += fractal_sigmoid
        
        # Combine all components with enhanced weighting
        return (0.25 * fractal_peak + 0.30 * cos_modulation + 0.20 * adaptive_cond + 
                0.15 * fractal_coupling + 0.10 * gradient)