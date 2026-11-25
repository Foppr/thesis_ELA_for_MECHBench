import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with sinusoidal modulation
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            center_idx = i % len(centers)
            center = centers[center_idx]
            distance = np.abs(x_norm[i] - center)
            rbf_sum += np.exp(-5.0 * distance**2) * np.sin(10 * x_norm[i])
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                coupling = (1 + 0.5 * np.sin(x_norm[i] * x_norm[j] * 8.0))
                cross_term += coupling * np.exp(-distance * 3.0) * (x_norm[i]**2 + x_norm[j]**2)
        
        # Multi-frequency sinusoidal oscillations with adaptive amplitudes
        sin_sum = 0.0
        frequencies = [1.0, 3.0, 7.0, 11.0]
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            freq = frequencies[freq_idx]
            sin_sum += np.sin(x_norm[i] * freq * np.pi) * np.cos(x_norm[i] * freq * np.pi / 3.0)
        
        # Saddle-point like behavior with hyperbolic tangent conditioning
        saddle_sum = 0.0
        for i in range(self.dim):
            saddle_sum += (np.tanh(x_norm[i]) ** 2) * (x_norm[i]**4 - 3 * x_norm[i]**2 + 2)
        
        # Chaotic modulation with dynamic scaling based on input magnitude
        chaos_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm**2) * 5.0)
        
        # Combine all terms with adaptive weighting
        result = 0.3 * rbf_sum + 0.25 * cross_term + 0.2 * sin_sum + 0.25 * saddle_sum
        
        return result * chaos_factor * (1 + 0.1 * np.sum(np.abs(x_norm)))