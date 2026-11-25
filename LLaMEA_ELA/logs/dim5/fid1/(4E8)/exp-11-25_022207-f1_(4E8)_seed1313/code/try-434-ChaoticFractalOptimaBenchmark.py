import numpy as np

class ChaoticFractalOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic fractal pattern parameters
        self.fractal_dimensions = np.random.uniform(1.1, 2.5, dim)
        self.fractal_amplitudes = np.logspace(0.8, 2.2, dim) * 1.5
        # Dynamic conditioning gradients
        self.conditioning_strengths = np.logspace(0.5, 2.0, dim) * 3.0
        # Cross-dimensional interference parameters
        self.interference_amplitudes = np.random.uniform(0.8, 4.0, dim) * 1.8
        self.interference_frequencies = np.random.uniform(1.0, 5.0, dim) * 1.5
        # Stochastic harmonic modulation
        self.harmonic_modulation = np.random.uniform(0.3, 1.2, dim) * 2.0
        # Adaptive scaling factors
        self.scaling_factors = np.logspace(0.2, 1.5, dim) * 2.5
        # Chaotic coupling matrix
        self.coupling_matrix = np.random.randn(dim, dim) * 0.5
        # Cluster positioning for optima distribution
        self.cluster_centers = np.random.uniform(-4.0, 4.0, dim) * 1.3
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal harmonic terms with chaotic patterns
        fractal_term = 0.0
        for i in range(self.dim):
            dim_frac = self.fractal_dimensions[i]
            amp = self.fractal_amplitudes[i]
            # Fractal pattern with chaotic modulation
            fractal_val = amp * np.sin(2.0 ** (dim_frac * x_norm[i])) ** 2
            fractal_term += fractal_val
            
        # Dynamic conditioning with gradient modulation
        conditioning_term = 0.0
        for i in range(self.dim):
            cond_strength = self.conditioning_strengths[i]
            # Quadratic conditioning with chaotic scaling
            quad_term = cond_strength * x_norm[i] ** 2
            # Add fractal modulation to conditioning
            mod_factor = 1.0 + 0.4 * np.sin(3.0 * x_norm[i]) * np.cos(2.0 * x_norm[i])
            conditioning_term += quad_term * mod_factor
            
        # Cross-dimensional interference with chaotic coupling
        interference_term = 0.0
        for i in range(self.dim):
            amp = self.interference_amplitudes[i]
            freq = self.interference_frequencies[i]
            # Interference pattern with chaotic dynamics
            interference_val = amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            # Coupling effect from other dimensions with chaotic matrix
            coupling_effect = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_effect += self.coupling_matrix[i, j] * x_norm[j]
            interference_val *= (1.0 + 0.3 * coupling_effect)
            interference_term += interference_val
            
        # Stochastic harmonic modulation with fractal characteristics
        modulation_term = 0.0
        for i in range(self.dim):
            mod_amp = self.harmonic_modulation[i]
            scaling = self.scaling_factors[i]
            # Harmonic modulation with chaotic amplitude variations
            mod_val = mod_amp * np.sin(scaling * x_norm[i]) ** 3
            modulation_term += mod_val
            
        # Cluster-based optima positioning with fractal interference
        cluster_term = 0.0
        for i in range(self.dim):
            center = self.cluster_centers[i]
            # Distance from cluster center with fractal modulation
            distance = x_norm[i] - center
            # Polynomial cluster shape with chaotic perturbations
            cluster_val = (distance ** 5) + 0.6 * (distance ** 7) + 0.15 * np.sin(4.0 * distance)
            cluster_term += cluster_val
            
        # Combine all terms with dynamic weights
        result = 1.5 * fractal_term + 1.2 * conditioning_term + 1.0 * interference_term + 0.8 * modulation_term + 1.1 * cluster_term
        
        # Add stochastic noise with chaotic characteristics
        noise_amplitude = 0.03 * (1.0 + 0.08 * self.dim)
        noise = noise_amplitude * np.random.randn() * np.sin(2.0 * np.pi * np.random.rand())
        
        return result + noise