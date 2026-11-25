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
            sin_term += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) + \
                       np.sin(15 * x_norm[i]**3) * np.cos(11 * x_norm[i]**3)
        
        # Radial basis function component with asymmetric peaks and valleys
        rbf_term = 0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i]
            # Asymmetric Gaussian with different variances
            variance = 0.15 + 0.35 * (i % 2)  # Alternate between two variances
            diff = x_norm[i] - center
            rbf_term += np.exp(-0.5 * (diff**2) / variance) * (1 + 0.6 * np.sin(6 * diff))
        
        # Asymmetric saddle point component with polynomial and exponential terms
        saddle_term = 0
        for i in range(self.dim):
            # Create asymmetric behavior using sign function
            asym_factor = np.sign(x_norm[i]) * 0.4 + 1.0
            saddle_term += (x_norm[i]**5 - 2.5 * x_norm[i]**3) * asym_factor + \
                          0.6 * np.exp(-0.4 * x_norm[i]**2) * np.cos(4 * x_norm[i])
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling strength decreases with distance
                coupling_strength = 1.0 / (1 + 0.15 * np.abs(i - j))
                cross_term += coupling_strength * np.sin(5 * x_norm[i]) * np.cos(4 * x_norm[j])
        
        # Additional quadratic cross-term for increased conditioning
        quad_cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.5 / (1 + 0.05 * np.abs(i - j))
                quad_cross_term += coupling_strength * x_norm[i]**2 * x_norm[j]**2
        
        # Combine all components with different weights and add noise
        result = 1.8 * sin_term + 2.3 * rbf_term + 2.1 * saddle_term + 1.0 * cross_term + 0.6 * quad_cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise