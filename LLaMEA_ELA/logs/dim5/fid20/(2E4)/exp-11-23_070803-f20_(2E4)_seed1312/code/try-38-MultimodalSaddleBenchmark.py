import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_term = 0
        for i in range(self.dim):
            sin_term += np.sin(8 * x_norm[i]) * np.cos(6 * x_norm[i]) + \
                       np.sin(12 * x_norm[i]**3) * np.cos(9 * x_norm[i]**3)
        
        # Radial basis function component with asymmetric peaks and valleys
        rbf_term = 0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i]
            # Asymmetric Gaussian with different variances
            variance = 0.2 + 0.3 * (i % 2)  # Alternate between two variances
            diff = x_norm[i] - center
            rbf_term += np.exp(-0.5 * (diff**2) / variance) * (1 + 0.5 * np.sin(5 * diff))
        
        # Asymmetric saddle point component with polynomial and exponential terms
        saddle_term = 0
        for i in range(self.dim):
            # Create asymmetric behavior using sign function
            asym_factor = np.sign(x_norm[i]) * 0.3 + 1.0
            saddle_term += (x_norm[i]**4 - 2 * x_norm[i]**2) * asym_factor + \
                          0.5 * np.exp(-0.5 * x_norm[i]**2) * np.cos(3 * x_norm[i])
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling strength decreases with distance
                coupling_strength = 1.0 / (1 + 0.1 * np.abs(i - j))
                cross_term += coupling_strength * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[j])
        
        # Combine all components with different weights and add noise
        result = 1.5 * sin_term + 2.0 * rbf_term + 1.8 * saddle_term + 0.8 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise