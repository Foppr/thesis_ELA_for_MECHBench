import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for global conditioning
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        self.rotation = self.rotation / np.linalg.norm(self.rotation, axis=0)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation for global conditioning
        x_rot = np.dot(self.rotation, x_norm)
        
        # Base quadratic term
        f1 = np.sum(x_rot**2)
        
        # Exponential barrier terms to create rugged landscape
        f2 = np.sum(np.exp(-5.0 * np.abs(x_rot)))
        
        # Sinusoidal modulation with varying frequencies
        f3 = np.sum(np.sin(10 * np.pi * x_rot) * np.cos(5 * np.pi * x_rot))
        
        # Chaotic component using logistic map-like behavior with noise
        chaotic = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic += 4 * 0.5 * (1 - 0.5)
            else:
                chaotic += 4 * x_rot[i-1] * (1 - x_rot[i-1])
        
        # Add noise to chaotic component for increased complexity
        chaotic += np.random.normal(0, 0.1)
        f4 = chaotic
        
        # Add a global sinusoidal modulation term
        global_mod = np.sin(np.sum(x_rot**2))
        
        # Combine all terms with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.4 * f3 + 0.1 * f4 + 0.2 * global_mod