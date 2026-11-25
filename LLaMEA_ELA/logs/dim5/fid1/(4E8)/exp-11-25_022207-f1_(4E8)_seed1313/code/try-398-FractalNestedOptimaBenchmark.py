import numpy as np

class FractalNestedOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal-like nested structure parameters
        self.nest_levels = min(5, dim // 2 + 1)
        self.scale_factors = np.logspace(0.5, 2.5, self.nest_levels) * 1.2
        self.fractal_exponents = np.linspace(1.2, 3.8, self.nest_levels) * 0.9
        # Adaptive conditioning with dimension-specific stiffness
        self.stiffness_factors = np.logspace(0.8, 2.2, dim) * 1.5
        # Dynamic coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.3, 1.8, dim) * 1.1
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal nested optima with self-similar patterns
        fractal_term = 0.0
        for i in range(self.nest_levels):
            scale = self.scale_factors[i]
            exponent = self.fractal_exponents[i]
            # Self-similar pattern with varying exponents and scales
            fractal_val = scale * np.abs(x_norm) ** exponent
            fractal_term += np.sum(fractal_val)
            
        # Adaptive conditioning with dimension-specific stiffness
        conditioning_term = 0.0
        for i in range(self.dim):
            stiffness = self.stiffness_factors[i]
            # Exponential conditioning with sinusoidal modulation
            cond_val = stiffness * np.exp(0.3 * x_norm[i] ** 2) * (1.0 + 0.2 * np.sin(3.0 * x_norm[i]))
            conditioning_term += cond_val
            
        # Dynamic cross-dimensional coupling with fractal-like interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_strength = self.coupling_strengths[i]
                # Fractal coupling with phase shifts and dynamic modulation
                phase_shift = np.pi * (i * j) / (self.dim + 1)
                coupling_val = coupling_strength * x_norm[i] * x_norm[j] * np.cos(phase_shift + 0.5 * x_norm[i] ** 2)
                coupling_term += coupling_val
                
        # Multi-scale clustering with varying cluster sizes and positions
        cluster_term = 0.0
        for i in range(self.dim):
            # Cluster positioning with fractal-based spacing
            cluster_pos = 3.0 * np.sin(0.7 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            # Polynomial clustering with increasing complexity
            cluster_val = 0.8 * (distance ** 4) + 0.4 * (distance ** 6) + 0.1 * (distance ** 8)
            cluster_term += cluster_val
            
        # Combined terms with fractal-inspired weighting
        result = 1.2 * fractal_term + 0.9 * conditioning_term + 0.75 * coupling_term + 0.65 * cluster_term
        
        # Add fractal noise with self-similar characteristics
        noise_amplitude = 0.025 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise