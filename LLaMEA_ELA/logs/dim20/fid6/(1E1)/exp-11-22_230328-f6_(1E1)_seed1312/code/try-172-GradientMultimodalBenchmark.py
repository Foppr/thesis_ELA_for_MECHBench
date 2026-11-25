import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for gradient modulation
        self.gradient_strengths = np.random.uniform(0.5, 2.0, dim)
        self.curvature_params = np.random.uniform(1.0, 3.0, dim)
        self.saddle_points = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.path_weights = np.random.uniform(0.1, 1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with varying curvature
        quadratic_term = 0.0
        for i in range(self.dim):
            curvature = self.curvature_params[i]
            quadratic_term += 0.5 * curvature * (x_norm[i] ** 2)
        
        # Saddle point contributions with path-dependent weights
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(3):
                saddle_x = self.saddle_points[i, j]
                weight = self.path_weights[i]
                # Path-dependent influence of saddle points
                distance = np.abs(x_norm[i] - saddle_x)
                saddle_term += weight * np.exp(-distance ** 2) * np.sin(2 * np.pi * x_norm[i])
        
        # Gradient modulation with varying strengths
        gradient_term = 0.0
        for i in range(self.dim):
            strength = self.gradient_strengths[i]
            gradient_term += strength * np.sin(x_norm[i]) * np.cos(x_norm[i])
        
        # Cross-dimensional interaction with path-dependent coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Path-dependent coupling based on x values
                coupling_strength = (1.0 + 0.3 * np.sin(x_norm[i] + x_norm[j]))
                interaction_term += coupling_strength * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                                  np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Combined fitness function
        combined = quadratic_term + saddle_term + gradient_term + interaction_term
        
        # Add noise to make it more challenging
        noise = 0.01 * np.random.normal(0, 1)
        
        return combined + noise