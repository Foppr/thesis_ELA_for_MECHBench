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
        # Fractal-like parameters for self-similarity
        self.fractal_depth = 3
        self.fractal_scale = 0.3
        # Chaotic modulation parameters
        self.chaos_factor = 3.8
        self.resonance_strength = 1.2
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add fractal-like chaotic sine-wave perturbations
        for i in range(self.dim):
            # Multi-scale chaotic modulation
            chaotic_term = 0.0
            for depth in range(self.fractal_depth):
                freq = (self.chaos_factor ** depth) * (1.0 + 0.1 * np.sin(i * 0.5))
                amp = self.fractal_scale ** depth
                chaotic_term += amp * np.sin(freq * x_transformed[i] + depth * np.cos(freq * x_transformed[i]))
            f_val += 3.0 * chaotic_term
            
        # Add cross-dimensional resonance terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Resonant interaction with phase coupling
                phase = np.sin(0.5 * x_transformed[i]) * np.cos(0.3 * x_transformed[j])
                f_val += self.resonance_strength * x_transformed[i] * x_transformed[j] * phase
                
        # Add higher-order polynomial with chaotic perturbation
        f_val += 0.1 * np.sum((x_transformed**5) * (1.0 + 0.3 * np.sin(7.0 * x_transformed)))
        
        # Add self-similar multimodal structure
        for i in range(self.dim):
            f_val += 2.5 * np.sin(2.0 * x_transformed[i]) * np.cos(3.0 * x_transformed[i]) * \
                     np.sin(4.0 * x_transformed[i]) * np.cos(5.0 * x_transformed[i])
            
        # Add stochastic noise with fractal-like correlation
        noise = np.random.normal(0, 0.3, self.dim)
        for i in range(self.dim):
            noise[i] += 0.2 * np.sin(5.0 * x_transformed[i]) * np.cos(3.0 * x_transformed[i])
        f_val += np.sum(noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.5
        
        return f_val