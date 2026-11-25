import numpy as np

class ChaoticAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9  # Tent map parameter
        self.seed = 0.7  # Initial seed for chaos
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Generate chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        current = self.seed
        for i in range(self.dim):
            if current < 0.5:
                current = self.r * current
            else:
                current = self.r * (1 - current)
            chaotic_seq[i] = current
        
        # Polynomial coupling terms
        poly_coupling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Higher-order polynomial interactions
            poly_term = xi**3 + 0.5 * xi**4 + 0.3 * xi**5
            
            # Cross-dimensional polynomial coupling
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (xi - x_norm[j])**2 * np.sin(xi * x_norm[j])
            
            poly_coupling += poly_term + coupling_sum
        
        # Gradient-based attraction fields
        attraction_fields = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Attraction from chaotic sequence
            attraction = (xi - chaotic_seq[i])**2
            
            # Additional gradient components
            grad_component = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = abs(xi - x_norm[j])
                    grad_component += np.exp(-dist**2) * np.sin(2.0 * (xi + x_norm[j]))
            
            attraction_fields += attraction + grad_component
        
        # Multi-scale sinusoidal modulation
        modulated = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple frequency components
            freq1 = 2.0 + 0.5 * np.sin(chaotic_seq[i])
            freq2 = 3.0 + 0.3 * np.cos(chaotic_seq[i])
            
            mod_term = np.sin(freq1 * xi) * np.cos(freq2 * xi)
            modulated += mod_term
        
        # Combine all components with dynamic weights
        result = 0.5 * poly_coupling**2 + 0.3 * attraction_fields**2 + 0.2 * modulated**2
        
        # Global scaling factor based on dimensionality
        global_scale = 1.0 + 0.1 * np.sin(self.dim * 0.5) + 0.05 * np.cos(self.dim * 0.3)
        
        return global_scale * result