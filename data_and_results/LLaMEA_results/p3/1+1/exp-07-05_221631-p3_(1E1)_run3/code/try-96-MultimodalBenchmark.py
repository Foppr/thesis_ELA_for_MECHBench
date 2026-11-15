import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Additional random scaling for each dimension
        self.scales = np.random.uniform(0.5, 2.0, dim)
        # Fractal-like modulation parameters
        self.fractal_freq = np.random.uniform(1.0, 10.0, dim)
        self.fractal_amp = np.random.uniform(0.5, 3.0, dim)
        # Cross-dimensional coupling strength
        self.coupling_strength = 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add fractal-like chaotic sine-wave perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            # Multi-scale chaotic modulation
            chaotic_mod = (np.sin(self.fractal_freq[i] * x_transformed[i]) * 
                          np.cos(self.fractal_freq[i] * x_transformed[i] * 0.7) * 
                          np.sin(self.fractal_freq[i] * x_transformed[i] * 0.3))
            f_val += self.fractal_amp[i] * chaotic_mod
            
        # Add complex cross-dimensional interaction terms with fractal coupling
        for i in range(self.dim):
            # Self-similar interaction pattern
            interaction = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                interaction += (x_transformed[i] * x_transformed[j] * 
                               np.sin(self.fractal_freq[i] * x_transformed[i] + 
                                      self.fractal_freq[j] * x_transformed[j]))
            f_val += self.coupling_strength * interaction
            
        # Add higher-order polynomial with chaotic perturbations
        f_val += 0.1 * np.sum((x_transformed**6) * 
                             (1.0 + 0.3 * np.sin(3.0 * x_transformed) * 
                              np.cos(2.0 * x_transformed)))
        
        # Add fractal interference pattern
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += np.sin(2.0 * (x_transformed[i] - x_transformed[j])) * \
                               np.cos(1.5 * (x_transformed[i] + x_transformed[j]))
        f_val += 0.5 * interference
        
        # Add stochastic noise with fractal characteristics
        noise = np.random.normal(0, 0.3, self.dim)
        fractal_noise = np.sin(self.fractal_freq * x_transformed) * noise
        f_val += np.sum(fractal_noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.2
        
        return f_val