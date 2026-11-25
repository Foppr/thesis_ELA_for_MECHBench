import numpy as np

class HybridChaoticRotatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
        # Adaptive conditioning parameters
        self.conditioning = np.logspace(0, 2, dim)
        
        # Dynamic scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        
        # Trigonometric frequencies
        self.frequencies = np.random.uniform(1, 5, dim)
        
        # Polynomial degrees
        self.degrees = np.random.randint(2, 6, dim)
        
    def f(self, x):
        # Apply rotation and conditioning
        x_rotated = self.rotation_matrix @ (x * self.scaling_factors)
        x_conditioned = x_rotated * self.conditioning
        
        # Polynomial terms with varying degrees
        polynomial_term = np.sum([np.power(x_conditioned[i], self.degrees[i]) 
                                for i in range(self.dim)])
        
        # Trigonometric components with dynamic frequencies
        trig_term = np.sum([np.sin(self.frequencies[i] * x_conditioned[i]) * 
                          np.cos(self.frequencies[i] * x_conditioned[i])
                          for i in range(self.dim)])
        
        # Radial basis function component with adaptive centers
        center_offset = np.random.uniform(-1, 1, self.dim)
        rbf_term = np.sum([np.exp(-0.5 * np.sum((x_conditioned - center_offset)**2)) 
                         for _ in range(10)])
        
        # Chaotic modulation using logistic map
        chaotic_mod = 0.0
        x_temp = x.copy()
        for i in range(self.dim):
            r = 3.9  # Logistic map parameter
            x_temp[i] = r * x_temp[i] * (1 - x_temp[i])
            chaotic_mod += np.sin(x_temp[i] * np.pi) * np.cos(x_temp[i] * np.pi)
        
        # Combined fitness with dynamic weighting
        total = 0.3 * polynomial_term + 0.4 * trig_term + 0.2 * rbf_term + 0.1 * chaotic_mod
        
        # Add global minimum offset
        total += np.sum(x**2) * 0.01
        
        return total