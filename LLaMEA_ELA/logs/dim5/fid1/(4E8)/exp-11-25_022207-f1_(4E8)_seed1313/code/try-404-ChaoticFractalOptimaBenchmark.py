import numpy as np

class ChaoticFractalOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic fractal structure parameters
        self.nest_levels = min(6, dim // 2 + 2)
        self.scale_factors = np.logspace(0.3, 3.0, self.nest_levels) * 1.5
        self.fractal_exponents = np.linspace(1.0, 4.2, self.nest_levels) * 1.1
        # Dynamic conditioning with chaotic stiffness
        self.stiffness_factors = np.logspace(0.6, 2.5, dim) * 2.0
        # Chaotic coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.5, 2.2, dim) * 1.3
        # Chaos parameter for dynamic behavior
        self.chaos_factor = 0.8 + np.random.rand() * 0.4
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Chaotic fractal nested optima with self-similar patterns
        fractal_term = 0.0
        for i in range(self.nest_levels):
            scale = self.scale_factors[i]
            exponent = self.fractal_exponents[i]
            # Self-similar pattern with chaotic modulation
            chaos_mod = 1.0 + 0.3 * np.sin(self.chaos_factor * i * np.pi / (self.nest_levels + 1))
            fractal_val = scale * chaos_mod * np.abs(x_norm) ** exponent
            fractal_term += np.sum(fractal_val)
            
        # Dynamic conditioning with chaotic stiffness
        conditioning_term = 0.0
        for i in range(self.dim):
            stiffness = self.stiffness_factors[i]
            # Exponential conditioning with chaotic sinusoidal modulation
            chaos_mod = 1.0 + 0.25 * np.sin(self.chaos_factor * i * np.pi / (self.dim + 1))
            cond_val = stiffness * np.exp(0.4 * x_norm[i] ** 2) * (1.0 + 0.3 * chaos_mod * np.sin(4.0 * x_norm[i]))
            conditioning_term += cond_val
            
        # Dynamic cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_strength = self.coupling_strengths[i]
                # Chaotic coupling with dynamic phase shifts and modulation
                phase_shift = np.pi * (i * j) / (self.dim + 2) + 0.5 * self.chaos_factor * np.sin(i * j)
                chaos_mod = 1.0 + 0.2 * np.cos(self.chaos_factor * (i + j))
                coupling_val = coupling_strength * chaos_mod * x_norm[i] * x_norm[j] * np.cos(phase_shift + 0.6 * x_norm[i] ** 2)
                coupling_term += coupling_val
                
        # Multi-scale clustering with chaotic positioning
        cluster_term = 0.0
        for i in range(self.dim):
            # Cluster positioning with chaotic spacing
            chaos_pos = 3.0 * np.sin(0.8 * (i + 1) * np.pi / self.dim + self.chaos_factor * np.cos(i))
            distance = x_norm[i] - chaos_pos
            # Polynomial clustering with chaotic complexity
            cluster_val = 1.0 * (distance ** 4) + 0.6 * (distance ** 6) + 0.2 * (distance ** 8)
            cluster_term += cluster_val
            
        # Combined terms with chaotic weighting
        result = 1.5 * fractal_term + 1.1 * conditioning_term + 0.9 * coupling_term + 0.8 * cluster_term
        
        # Add chaotic noise with self-similar characteristics
        noise_amplitude = 0.03 * (1.0 + 0.08 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise