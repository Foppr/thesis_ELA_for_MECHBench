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
            trig_term += np.sin(8 * x_norm[i]) * np.cos(6 * x_norm[i]) + \
                        np.sin(12 * x_norm[i]**2) * np.cos(10 * x_norm[i]**2)
        
        # Radial basis function component with multiple centers
        rbf_term = 0
        centers = [np.array([0.5, -0.3, 0.8]), 
                   np.array([-0.7, 0.4, -0.6]), 
                   np.array([0.2, 0.9, -0.5])]
        
        for i in range(min(3, self.dim)):
            center = centers[i % len(centers)]
            # Use only available dimensions for each center
            c = center[:self.dim]
            diff = x_norm - c
            rbf_term += np.exp(-2.0 * np.sum(diff**2))
        
        # Asymmetric saddle point component with varying curvature
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**4 - 2 * x_norm[i]**2) * (1 + 0.3 * np.sin(5 * x_norm[i]))
        
        # Cross-term coupling with varying strength
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross_term += (x_norm[i] * x_norm[j]) / (1 + 0.5 * np.abs(x_norm[i] - x_norm[j]))
        
        # Combined function with scaling factors
        result = 1.5 * trig_term + 0.8 * rbf_term + 1.2 * saddle_term + 0.6 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise