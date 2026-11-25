import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Trigonometric oscillation component with varying frequencies
        trig_term = 0
        for i in range(self.dim):
            trig_term += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) + \
                        np.sin(15 * x_norm[i]**3) * np.cos(11 * x_norm[i]**3)
        
        # Radial basis function component with multiple centers
        rbf_term = 0
        centers = [
            np.array([0.6, -0.4, 0.9]),
            np.array([-0.8, 0.5, -0.7]),
            np.array([0.3, 1.0, -0.6])
        ]
        
        for i in range(min(3, self.dim)):
            center = centers[i % len(centers)]
            if i < len(center):
                diff = x_norm[i] - center[i]
                rbf_term += np.exp(-6 * diff**2) + 0.6 * np.exp(-4 * (diff - 0.6)**2)
        
        # Asymmetric saddle points with varying steepness
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**5 - 2.5 * x_norm[i]**2) * (1 + 0.4 * np.sin(6 * x_norm[i]))
        
        # Cross-term coupling with sine modulation
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(4 * (x_norm[i] + x_norm[j])) * \
                             np.exp(-0.6 * (x_norm[i] - x_norm[j])**2)
        
        # Combined function with scaling factors
        result = 1.8 * trig_term + 0.9 * rbf_term + 1.4 * saddle_term + 0.7 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise