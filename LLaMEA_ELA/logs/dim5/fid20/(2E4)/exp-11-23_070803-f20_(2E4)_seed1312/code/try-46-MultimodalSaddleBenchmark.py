import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced sinusoidal oscillation component with higher frequency interactions
        sin_term = 0
        for i in range(self.dim):
            sin_term += (np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) + 
                       np.sin(15 * x_norm[i]**2) * np.cos(11 * x_norm[i]**2)) * (1 + 0.3 * np.sin(5 * x_norm[i]))
        
        # Modified radial basis function component with varying peak shapes
        rbf_term = 0
        centers = np.linspace(-0.9, 0.9, min(6, self.dim))
        for i in range(min(6, self.dim)):
            center = centers[i]
            # Asymmetric Gaussian with varying exponents and amplitudes
            exponent = 2 + 2 * (i % 3)  # Varying exponents for different peak shapes
            variance = 0.15 + 0.25 * (i % 2)  # Alternate between two variances
            diff = x_norm[i] - center
            rbf_term += np.exp(-0.5 * (diff**exponent) / variance) * (1 + 0.4 * np.cos(4 * diff))
        
        # Improved asymmetric saddle point component with enhanced polynomial terms
        saddle_term = 0
        for i in range(self.dim):
            # Create stronger asymmetric behavior using higher-order terms
            asym_factor = np.sign(x_norm[i]) * 0.5 + 1.2
            saddle_term += (x_norm[i]**5 - 3 * x_norm[i]**3 + 2 * x_norm[i]) * asym_factor + \
                          0.7 * np.exp(-0.3 * x_norm[i]**2) * np.sin(4 * x_norm[i])
        
        # Enhanced cross-dimensional coupling with non-linear interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for higher dimensions
                # Non-linear coupling strength based on distance and input values
                coupling_strength = 1.0 / (1 + 0.2 * np.abs(i - j) + 0.1 * np.abs(x_norm[i] * x_norm[j]))
                cross_term += coupling_strength * np.sin(5 * x_norm[i]) * np.sin(4 * x_norm[j]) * (1 + 0.2 * np.cos(x_norm[i] + x_norm[j]))
        
        # Combine all components with adjusted weights and add controlled noise
        result = 2.0 * sin_term + 2.5 * rbf_term + 2.2 * saddle_term + 1.0 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise