import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive scaling
        rbfs = []
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        if self.dim < 5:
            centers = np.pad(centers, (0, self.dim - len(centers)), mode='constant')
        
        for i, center in enumerate(centers):
            if i < len(centers):
                sigma = 0.5 + 0.3 * np.sin(i * 1.5)
                rbfs.append(np.exp(-np.sum((x - center)**2) / (2 * sigma**2)))
        
        rbf_term = np.sum(rbfs) / len(rbfs) if rbfs else 0
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                         np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x)) / self.dim
        
        # Adaptive conditioning component
        conditioning = np.sum((1 + 0.1 * np.sin(self.dim * 0.5)) * x**2 + 
                             (0.5 + 0.2 * np.cos(self.dim * 0.7)) * x**3) / self.dim
        
        # Cross-dimensional coupling with adaptive weights
        coupling = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.0 + 0.5 * np.sin(i * 0.8 + self.dim * 0.3)
                coupling += weight * np.abs(x[i] - x[i+1])**2
        
        # Noise component for added complexity
        noise = 0.01 * np.random.rand()
        
        # Combine all terms with adaptive weights
        weights = [0.3 + 0.1 * np.sin(self.dim * 0.4), 
                  0.4 + 0.1 * np.cos(self.dim * 0.6), 
                  0.2 + 0.1 * np.sin(self.dim * 0.8),
                  0.1 + 0.05 * np.cos(self.dim * 1.0)]
        
        result = (weights[0] * rbf_term + 
                 weights[1] * sin_term + 
                 weights[2] * conditioning + 
                 weights[3] * coupling)
        
        return result + noise