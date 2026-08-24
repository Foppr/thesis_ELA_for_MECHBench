import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with varying widths
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_sum += np.exp(-0.5 * np.sum((x_norm - np.sin(i * np.pi / self.dim))**2))
        
        # Polynomial interaction terms with mixed degrees
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + x_norm[j]**2) * np.sin(2 * (x_norm[i] - x_norm[j]))
        
        # Sine wave modulation with varying amplitudes and frequencies
        sine_modulation = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Cross-terms with hyperbolic tangent scaling
        tanh_cross = 0.0
        for i in range(self.dim - 1):
            tanh_cross += np.tanh(x_norm[i] + x_norm[i+1]) * np.tanh(x_norm[i] - x_norm[i+1])
        
        # Global optimum at origin with high-frequency oscillation
        high_freq = np.sum(np.sin(20 * x_norm)**2 + np.cos(20 * x_norm)**2)
        
        # Combine all components with different weights
        return 1.2 * rbf_sum + 1.5 * poly_interaction + 0.8 * sine_modulation + 0.9 * tanh_cross + 1.3 * high_freq