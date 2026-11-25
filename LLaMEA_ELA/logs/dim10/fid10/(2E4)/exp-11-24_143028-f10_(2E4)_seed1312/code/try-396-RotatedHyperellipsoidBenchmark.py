import numpy as np

class RotatedHyperellipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrices for each dimension
        self.rotation_matrices = []
        for _ in range(dim):
            # Create random orthogonal matrix
            A = np.random.randn(dim, dim)
            Q, _ = np.linalg.qr(A)
            self.rotation_matrices.append(Q)
        
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        self.adaptive_exponents = np.random.uniform(1.5, 3.0, dim)
        
        # Saddle point parameters
        self.saddle_centers = np.random.uniform(-2.0, 2.0, dim)
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        
        # Interaction weights between dimensions
        self.interaction_weights = np.random.uniform(0.1, 1.0, (dim, dim))
        np.fill_diagonal(self.interaction_weights, 0.0)
        
        # Global scaling and noise parameters
        self.global_scale = np.random.uniform(0.5, 2.0)
        self.noise_level = np.random.uniform(0.001, 0.01)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to each dimension
        rotated_x = np.zeros_like(x)
        for i in range(self.dim):
            rotated_x[i] = np.dot(self.rotation_matrices[i], x)
        
        # Compute hyperellipsoid terms with adaptive conditioning
        fitness = 0.0
        for i in range(self.dim):
            # Base hyperellipsoid term with conditioning
            term = (rotated_x[i]**2) * self.conditioning_factors[i]
            
            # Add adaptive exponentiation for nonlinearity
            term *= (abs(rotated_x[i]) + 1e-8)**(self.adaptive_exponents[i] - 2)
            
            # Add saddle point influence
            saddle_influence = self.saddle_strengths[i] * (rotated_x[i] - self.saddle_centers[i])**2
            
            # Add interaction terms with other dimensions
            interaction_term = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction_term += self.interaction_weights[i, j] * rotated_x[i] * rotated_x[j]
            
            fitness += term + saddle_influence + interaction_term
        
        # Apply global scaling and add noise
        fitness = fitness * self.global_scale
        noise = np.random.normal(0, self.noise_level)
        
        return fitness + noise