import numpy as np

class NestedFractalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.57, 4.0, dim)
        self.cosine_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.cosine_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Fractal dimension and scaling factors
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        # Nested fractal structure
        self.nested_levels = np.random.randint(2, 5, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal-like cosine peaks with varying dimensions
        nested_cosine = 0.0
        for i in range(self.dim):
            amplitude = self.cosine_amplitudes[i]
            frequency = self.cosine_frequencies[i]
            # Add nested fractal scaling based on dimension
            fractal_factor = np.power(2.0, self.fractal_dims[i])
            # Nested structure with multiple cosine components
            nested_component = 0.0
            for level in range(self.nested_levels[i]):
                nested_component += amplitude * np.cos(frequency * np.power(x[i], level + 1) / fractal_factor)
            nested_cosine += nested_component
        
        # Memory-enhanced cosine couplings with chaotic modulation
        memory_cosine = 0.0
        prev_x = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map for chaotic modulation
            logistic_val = self.logistic_r[i] * xi * (1 - xi)
            # Memory effect with cosine coupling
            memory_cosine += np.cos(2 * np.pi * xi + 0.5 * np.cos(prev_x)) * np.exp(-0.1 * logistic_val**2)
            prev_x = xi
        
        # Adaptive conditioning based on fractal dimension and position
        conditioning = 0.0
        for i in range(self.dim):
            # Dimensional conditioning factor
            cond_factor = 1.0 + 0.5 * np.cos(0.3 * x[i]) * (self.fractal_dims[i] - 1.0)
            # Position-based conditioning
            pos_cond = 1.0 + 0.2 * np.sin(0.4 * x[i])
            conditioning += cond_factor * pos_cond
        
        # Deceptive gradient component with multiple local optima
        deceptive = 0.0
        for i in range(self.dim):
            # Add multiple cosine waves with different frequencies and phases
            deceptive += (np.cos(3 * np.pi * x[i]) + 
                         0.5 * np.cos(9 * np.pi * x[i]) + 
                         0.2 * np.cos(15 * np.pi * x[i]))
        
        # Cross-dimensional cubic couplings with chaotic weights
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic weight based on logistic map
                weight = 1.0 + 0.3 * np.cos(self.logistic_r[i] * x[i] * (1 - x[i]))
                cubic_coupling += weight * (x[i]**3 - x[j]**3) * np.sin(0.5 * (x[i] + x[j]))
        
        # Combine all components with dynamic scaling
        dim_factor = 1.0 + 0.2 * np.log(self.dim)
        return (0.30 * nested_cosine + 0.25 * memory_cosine + 
                0.20 * conditioning + 0.15 * deceptive + 0.10 * cubic_coupling) * dim_factor