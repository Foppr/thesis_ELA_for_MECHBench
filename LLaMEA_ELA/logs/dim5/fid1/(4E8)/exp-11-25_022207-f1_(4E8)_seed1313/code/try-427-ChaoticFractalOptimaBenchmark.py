import numpy as np

class ChaoticFractalOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperbolic fractal structure parameters
        self.nest_levels = min(8, dim // 2 + 3)
        self.scale_factors = np.logspace(0.5, 4.0, self.nest_levels) * 2.0
        self.fractal_exponents = np.linspace(1.2, 5.0, self.nest_levels) * 1.3
        # Dynamic conditioning with hyperbolic stiffness
        self.stiffness_factors = np.logspace(0.8, 3.0, dim) * 2.5
        # Chaotic coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.7, 2.5, dim) * 1.5
        # Chaos parameter for dynamic behavior
        self.chaos_factor = 0.9 + np.random.rand() * 0.5
        # Hyperbolic tangent modulation factors
        self.tanh_factors = np.random.uniform(0.3, 1.2, dim) * 1.1
        # Adaptive scaling parameters
        self.adaptive_scale = 1.0 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Hyperbolic fractal nested optima with self-similar patterns
        fractal_term = 0.0
        for i in range(self.nest_levels):
            scale = self.scale_factors[i]
            exponent = self.fractal_exponents[i]
            # Self-similar pattern with hyperbolic modulation
            chaos_mod = 1.0 + 0.4 * np.tanh(self.chaos_factor * i * np.pi / (self.nest_levels + 2))
            fractal_val = scale * chaos_mod * np.abs(x_norm) ** exponent
            fractal_term += np.sum(fractal_val)
            
        # Dynamic conditioning with hyperbolic stiffness
        conditioning_term = 0.0
        for i in range(self.dim):
            stiffness = self.stiffness_factors[i]
            # Exponential conditioning with hyperbolic sinusoidal modulation
            chaos_mod = 1.0 + 0.3 * np.tanh(self.chaos_factor * i * np.pi / (self.dim + 2))
            cond_val = stiffness * np.exp(0.5 * x_norm[i] ** 2) * (1.0 + 0.4 * chaos_mod * np.sin(5.0 * x_norm[i]))
            conditioning_term += cond_val
            
        # Dynamic cross-dimensional coupling with hyperbolic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_strength = self.coupling_strengths[i]
                # Hyperbolic coupling with dynamic phase shifts and modulation
                phase_shift = np.pi * (i * j) / (self.dim + 3) + 0.6 * self.chaos_factor * np.tanh(i * j)
                chaos_mod = 1.0 + 0.25 * np.sin(self.chaos_factor * (i + j))
                coupling_val = coupling_strength * chaos_mod * x_norm[i] * x_norm[j] * np.tanh(phase_shift + 0.7 * x_norm[i] ** 2)
                coupling_term += coupling_val
                
        # Multi-scale clustering with hyperbolic positioning
        cluster_term = 0.0
        for i in range(self.dim):
            # Cluster positioning with hyperbolic spacing
            chaos_pos = 4.0 * np.tanh(0.9 * (i + 1) * np.pi / self.dim + self.chaos_factor * np.sin(i))
            distance = x_norm[i] - chaos_pos
            # Polynomial clustering with hyperbolic complexity
            cluster_val = 1.2 * (distance ** 4) + 0.8 * (distance ** 6) + 0.3 * (distance ** 8)
            cluster_term += cluster_val
            
        # Combined terms with hyperbolic weighting
        result = 2.0 * fractal_term + 1.5 * conditioning_term + 1.1 * coupling_term + 1.0 * cluster_term
        
        # Add hyperbolic noise with self-similar characteristics
        noise_amplitude = 0.04 * (1.0 + 0.1 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        # Apply adaptive scaling
        result *= self.adaptive_scale
        
        return result + noise