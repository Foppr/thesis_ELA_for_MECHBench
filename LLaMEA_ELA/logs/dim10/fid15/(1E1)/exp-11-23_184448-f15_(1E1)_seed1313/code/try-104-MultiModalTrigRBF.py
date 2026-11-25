import numpy as np

class MultiModalTrigRBF:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Gaussian radial basis functions centered at random locations
        rbf_sum = 0.0
        num_centers = min(20, 2 * self.dim)
        np.random.seed(42)  # For reproducibility
        centers = np.random.uniform(-4.0, 4.0, (num_centers, self.dim))
        
        for i in range(num_centers):
            center = centers[i]
            sigma = 0.5 + 0.5 * np.random.rand()
            weight = 1.0 + 2.0 * np.random.rand()
            diff = x - center
            rbf_sum += weight * np.exp(-0.5 * np.sum((diff/sigma)**2))
        
        # Trigonometric interference pattern
        trig_pattern = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.random.rand()
            phase = np.pi * np.random.rand()
            trig_pattern += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
        
        # Adaptive dimension weighting based on position
        dim_weights = np.array([1.0 + 0.5 * np.sin(0.5 * i) for i in range(self.dim)])
        weighted_sum = np.sum(dim_weights * x**2)
        
        # Cross-dimension coupling with sine modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] * x[j]) * (i + j) / (self.dim**2)
        
        # Combined fitness function
        return 0.5 * rbf_sum + 0.3 * trig_pattern + 0.2 * weighted_sum + 0.1 * coupling