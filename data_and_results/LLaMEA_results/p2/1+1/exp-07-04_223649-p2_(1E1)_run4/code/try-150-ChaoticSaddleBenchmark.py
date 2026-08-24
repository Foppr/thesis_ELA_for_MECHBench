import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.linalg.qr(self.rotation_matrix)[0]
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create rotation-invariance challenge
        x_rot = self.rotation_matrix @ x
        
        # Base quadratic term
        result = np.sum(x_rot**2)
        
        # Nested saddle point structure with exponential decay
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.exp(-0.1 * (x_rot[i] - 1.0)**2) * np.sin(3.0 * x_rot[i])
            saddle_term += np.exp(-0.05 * (x_rot[i] + 2.0)**2) * np.cos(2.0 * x_rot[i])
            
        # Chaotic interaction using logistic map-like terms
        chaotic = 0.0
        for i in range(self.dim - 1):
            chaotic += np.sin(x_rot[i] * x_rot[i+1]) * np.exp(-0.01 * (x_rot[i] - x_rot[i+1])**2)
            
        # Exponential decay coupling with sinusoidal modulation
        decay_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_rot[i] - x_rot[j])
                decay_coupling += np.exp(-0.2 * dist) * np.sin(0.5 * dist)
                
        # High-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(10.0 * x_rot[i]) * np.cos(8.0 * x_rot[i])
            
        # Combine all components
        result = result + saddle_term + chaotic + decay_coupling + high_freq
        
        return result