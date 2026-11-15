import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive scaling
        rbfs = []
        for i in range(1, min(6, self.dim + 1)):
            center = np.random.uniform(-4.0, 4.0, self.dim)
            sigma = 0.5 + 0.5 * np.sin(i * 0.7)
            rbfs.append(np.exp(-np.sum((x - center)**2) / (2 * sigma**2)))
        
        # Sinusoidal oscillation component
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                         (1 + 0.3 * np.sin(np.sum(x**2)))) / self.dim
        
        # Adaptive conditioning component
        cond_weights = np.array([1.0 + 0.5 * np.sin(i * 0.3) for i in range(self.dim)])
        cond_term = np.sum(cond_weights * x**2) / self.dim
        
        # Multimodal coupling term
        multi_term = np.sum(np.sin(5 * np.pi * x) * np.cos(4 * np.pi * x) * 
                           (1 + 0.2 * np.sin(np.sum(x**3)))) / self.dim
        
        # Global minimum at origin with additional noise
        result = (0.5 * cond_term + 
                 0.3 * sin_term + 
                 0.2 * multi_term + 
                 0.1 * np.sum(np.array(rbfs)) if rbfs else 0)
        
        # Add small random noise to make it truly black-box
        noise = 0.001 * np.random.randn()
        
        return result + noise