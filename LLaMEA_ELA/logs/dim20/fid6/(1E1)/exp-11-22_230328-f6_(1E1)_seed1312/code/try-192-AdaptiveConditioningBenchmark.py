import numpy as np

class AdaptiveConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random conditioning parameters for each dimension
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        # Generate rotation matrices for each dimension
        self.rotation_matrices = []
        for _ in range(dim):
            angle = np.random.uniform(0, 2 * np.pi)
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            self.rotation_matrices.append(np.array([[cos_a, -sin_a], [sin_a, cos_a]]))
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with adaptive conditioning
        rb_term = 0.0
        for i in range(self.dim):
            # Apply conditioning factor
            conditioned_x = x_norm[i] * self.conditioning_factors[i]
            # Add radial basis function with sinusoidal modulation
            rb_term += np.exp(-0.5 * conditioned_x**2) * np.sin(3 * np.pi * conditioned_x)
        
        # Multi-scale oscillation component with varying frequencies
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Varying frequencies: 2, 4, 8, 16
            oscillation_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Cross-dimensional coupling with rotation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Rotate the pair of dimensions
                xy = np.array([x_norm[i], x_norm[j]])
                rotated_xy = self.rotation_matrices[i] @ xy
                
                # Add coupling with varying strength based on dimension indices
                coupling_strength = 1.0 / (1.0 + abs(i - j))
                coupling_term += coupling_strength * np.exp(-0.5 * (rotated_xy[0]**2 + rotated_xy[1]**2)) * \
                               np.sin(2 * np.pi * (rotated_xy[0] + rotated_xy[1]))
        
        # Adaptive conditioning bias term
        bias_term = 0.0
        for i in range(self.dim):
            bias_term += self.conditioning_factors[i] * np.sin(x_norm[i]) * np.cos(x_norm[i])
        
        # Global scaling and final combination
        combined = rb_term + 0.5 * oscillation_term + 0.3 * coupling_term + 0.2 * bias_term
        
        # Add noise for additional challenge
        noise = 0.01 * np.random.uniform(-1, 1)
        
        return combined + noise