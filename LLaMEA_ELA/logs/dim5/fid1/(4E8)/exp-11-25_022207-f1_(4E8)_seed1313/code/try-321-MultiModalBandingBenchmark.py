import numpy as np

class MultiModalBandingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters that scale with dimensionality
        self.band_frequencies = np.linspace(1.0, 8.0, min(10, dim))
        self.conditioning_factors = np.logspace(0.5, 2.5, min(12, dim))
        self.cluster_centers = np.random.uniform(-3.0, 3.0, min(8, dim))
        self.asymmetry_params = np.random.uniform(0.5, 2.0, min(6, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Periodic banding valleys with varying frequencies
        banding_term = 0.0
        for i in range(min(len(self.band_frequencies), self.dim)):
            freq = self.band_frequencies[i]
            # Create periodic valley structure with asymmetric depth
            valley_depth = np.sin(freq * x_norm[i]) ** 2
            asymmetry = self.asymmetry_params[i % len(self.asymmetry_params)]
            banding_val = asymmetry * (valley_depth + 0.1 * np.cos(3 * freq * x_norm[i]))
            banding_term += banding_val
            
        # Asymmetric gradient flows with dynamic conditioning
        gradient_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            cond_factor = self.conditioning_factors[i]
            # Asymmetric quadratic gradient with conditioning
            grad_val = cond_factor * (x_norm[i] ** 2) * np.abs(x_norm[i])
            gradient_term += grad_val
            
        # Multi-cluster optima with nested basins
        cluster_term = 0.0
        for i in range(min(len(self.cluster_centers), self.dim)):
            center = self.cluster_centers[i % len(self.cluster_centers)]
            distance = x_norm[i] - center
            # Nested clustering with varying basin widths
            cluster_val = 0.5 * (distance ** 4) + 0.2 * (distance ** 6)
            cluster_term += cluster_val
            
        # Dynamic coupling between dimensions with periodic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, min(self.dim, i + 5)):  # Limited coupling
                # Periodic coupling strength
                coupling_strength = np.sin(2.0 * (i + 1) * x_norm[j]) + 1.5
                coupling_val = coupling_strength * x_norm[i] * x_norm[j]
                coupling_term += coupling_val
                
        # Combine all terms with dynamic weights based on dimensionality
        total_terms = 3.0 + 0.2 * self.dim
        result = (0.6 * banding_term + 
                 0.4 * gradient_term + 
                 0.3 * cluster_term + 
                 0.1 * coupling_term) / total_terms
        
        # Add adaptive noise based on fitness landscape complexity
        noise_amplitude = 0.01 * (1.0 + 0.03 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise