import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Elliptic quadratic term with dimensionally adaptive scaling
        elliptic_term = np.sum((x_normalized ** 2) * (1 + 0.5 * np.sin(np.arange(self.dim) * 0.3)))
        
        # Rotational component with varying angles per dimension
        rotation_term = 0.0
        for i in range(self.dim):
            angle = 0.2 * np.pi * (i + 1) * np.cos(0.1 * i)
            x_rot = x_normalized[i] * np.cos(angle) - x_normalized[(i+1) % self.dim] * np.sin(angle)
            y_rot = x_normalized[i] * np.sin(angle) + x_normalized[(i+1) % self.dim] * np.cos(angle)
            rotation_term += x_rot**2 + y_rot**2
        
        # Saddle point structure with alternating signs
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (-1)**i * x_normalized[i]**4 + 0.5 * x_normalized[i]**2
        
        # Adaptive noise component that increases with dimension
        noise_term = 0.0
        np.random.seed(42)
        for i in range(self.dim):
            noise_term += np.random.normal(0, 0.1 * (1 + 0.05 * i)) * x_normalized[i]
        
        # Cross-term interaction with exponential decay weighting
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j))
                cross_term += weight * x_normalized[i] * x_normalized[j] * np.sin(2 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Dynamic scaling based on problem dimension
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (0.4 * elliptic_term + 
                              0.3 * rotation_term + 
                              0.2 * saddle_term + 
                              0.1 * noise_term + 
                              0.5 * cross_term)