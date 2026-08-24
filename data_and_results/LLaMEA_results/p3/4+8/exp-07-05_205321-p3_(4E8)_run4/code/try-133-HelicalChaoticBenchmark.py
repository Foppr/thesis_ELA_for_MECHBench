import numpy as np

class HelicalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Helical component creating spiral-like structure in high dimensions
        helix = 0.0
        for i in range(self.dim):
            helix += np.sin(3 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[(i + 1) % self.dim])
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(11 * np.pi * x_norm[i]) * np.cos(11 * np.pi * x_norm[i]**2)
        
        # Saddle point component with alternating signs
        saddle = 0.0
        for i in range(self.dim):
            saddle += (-1)**i * np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Radial harmonic component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(5 * r) * np.cos(3 * r) + 0.5 * np.sin(7 * r)
        
        # Cross-dimensional interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(4 * np.pi * x_norm[i]) * np.sin(4 * np.pi * x_norm[j])
        
        # Combine all components with different weights
        return 0.4 * helix + 0.3 * chaotic + 0.2 * saddle + 0.05 * radial + 0.05 * interaction + 1.0