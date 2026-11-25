import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic rotation angles and barrier parameters
        np.random.seed(42)
        self.rotation_angles = np.random.uniform(-np.pi, np.pi, dim)
        self.barrier_strengths = 2.0 + np.random.rand(dim) * 3.0
        self.saddle_depths = 1.0 + np.random.rand(dim) * 2.0
        self.nest_levels = 3 + np.random.randint(0, 3, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to input
        rotated_x = np.zeros_like(x)
        for i in range(self.dim):
            cos_a = np.cos(self.rotation_angles[i])
            sin_a = np.sin(self.rotation_angles[i])
            rotated_x[i] = x[i] * cos_a - x[(i+1) % self.dim] * sin_a
            
        # Compute nested saddle potential
        saddle_potential = 0.0
        for i in range(self.dim):
            depth = self.saddle_depths[i]
            nest_level = self.nest_levels[i]
            saddle_term = (rotated_x[i]**2 - depth)**2 + 0.1 * rotated_x[i]**4
            for _ in range(nest_level):
                saddle_term = (saddle_term - depth)**2 + 0.1 * saddle_term**4
            saddle_potential += saddle_term
            
        # Add logarithmic barrier terms
        barrier_terms = 0.0
        for i in range(self.dim):
            strength = self.barrier_strengths[i]
            barrier_terms += strength * (np.log(1 + np.abs(rotated_x[i])) + 
                                        0.5 * np.log(1 + rotated_x[i]**2))
            
        # Add chaotic coupling between dimensions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            chaotic_coupling += np.sin(rotated_x[i] * rotated_x[j]) * \
                               np.cos(0.5 * rotated_x[k]**2 + 0.3 * rotated_x[i])
            
        # Combine all components with varying weights
        result = 0.3 * np.sum(rotated_x**2) + 0.4 * saddle_potential + \
                 0.2 * barrier_terms + 0.1 * chaotic_coupling
        
        return result