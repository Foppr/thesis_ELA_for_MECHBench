import numpy as np

class TentHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map parameters
        self.mu_values = 1.8 + 0.3 * np.sin(np.linspace(0, 2*np.pi, dim))
        self.harmonic_coeffs = np.random.randn(dim) * 0.4
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent dynamics component
        tent_term = 0.0
        for i in range(self.dim):
            mu = self.mu_values[i]
            # Use previous dimension's value for chaotic coupling
            if i > 0:
                x_prev = x[i-1] if i > 0 else x[0]
                tent_term += mu * np.abs(x_prev - 0.5) * np.sin(x[i])
            else:
                tent_term += mu * np.abs(x[i] - 0.5)
        tent_term /= self.dim
        
        # Spherical harmonic decomposition with adaptive angular modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            angle_freq = 1.0 + 0.8 * np.sin(i * np.pi / (self.dim + 1)) + 0.2 * np.cos(x[i])
            harmonic_term += self.harmonic_coeffs[i] * np.sin(angle_freq * x[i]) * np.cos(angle_freq * x[i])
        harmonic_term /= self.dim
        
        # Adaptive elastic net penalty with dynamic regularization
        elastic_term = 0.0
        for i in range(self.dim):
            # Dynamic elastic coefficient based on dimension and value
            elastic_coeff = 0.3 + 0.2 * np.sin(i * np.pi / self.dim) + 0.1 * np.abs(x[i])
            elastic_term += elastic_coeff * (np.abs(x[i]) + 0.5 * x[i]**2)
        elastic_term /= self.dim
        
        # Cross-dimensional interaction with tent coupling and exponential terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Tent coupling between dimensions
                tent_coupling = np.sin(x[i] * x[j]) + 0.3 * np.exp(-np.abs(x[i] - x[j]))
                cross_term += tent_coupling * np.exp(-0.5 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale spatial dynamics with spherical harmonics
        spatial_term = 0.0
        for i in range(self.dim):
            # Spherical harmonic oscillators with different frequencies
            freq = 2.0 + 0.6 * np.sin(i * np.pi / self.dim) + 0.3 * np.cos(x[i])
            spatial_term += np.sin(freq * x[i]) * np.cos(3.0 * freq * x[i]) + 0.4 * np.sin(2.0 * freq * x[i])
        spatial_term /= self.dim
        
        # Asymmetric distortion with tent map transformation
        asym_term = 0.0
        for i in range(self.dim):
            # Apply tent map to input for asymmetric effect
            tent_val = self.mu_values[i] * np.abs(x[i] - 0.5)
            asym_term += np.abs(tent_val) + 0.6 * tent_val**2
        asym_term /= self.dim
        
        # Dynamic conditioning factor with tent modulation
        cond_factor = 1.0 + 0.3 * np.sin(np.mean(np.abs(x))) + 0.15 * np.cos(self.dim * np.pi / 4.0)
        
        # Combine all terms with dynamic weights based on chaotic parameters
        total = (0.22 * tent_term + 
                0.22 * harmonic_term + 
                0.18 * elastic_term + 
                0.17 * cross_term + 
                0.13 * spatial_term + 
                0.08 * asym_term) * cond_factor
        
        return total