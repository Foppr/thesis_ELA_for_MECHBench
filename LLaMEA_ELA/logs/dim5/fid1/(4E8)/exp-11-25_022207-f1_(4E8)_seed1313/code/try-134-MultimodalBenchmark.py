import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component with varying parameters
        logistic = 0.0
        r_values = [3.5, 3.8, 3.9, 4.0]
        for i in range(min(self.dim, len(r_values))):
            logistic += r_values[i] * x_norm[i] * (1 - x_norm[i])
        
        # Multi-scale Gaussian peaks with varying amplitudes and widths
        gaussian = 0.0
        peaks = [(0.2, 0.1), (-0.3, 0.05), (0.5, 0.15), (-0.6, 0.08)]
        for i in range(self.dim):
            for amp, width in peaks:
                gaussian += amp * np.exp(-0.5 * ((x_norm[i] - amp) / width)**2)
        
        # Gradient-asymmetric corridor structure with exponential scaling
        corridor = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            corridor += np.exp(-0.5 * diff**2) * np.tanh(2 * diff)
        
        # Non-separable polynomial interactions with cross-dimensional coupling
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            poly_interaction += (x_norm[i]**2 + x_norm[i+1]**2) * \
                              (x_norm[i] * x_norm[i+1]) * \
                              np.exp(-0.1 * (x_norm[i] - x_norm[i+1])**2)
        
        # Multi-scale harmonic modulation with frequency-dependent amplitudes
        harmonic = 0.0
        frequencies = [2, 5, 8, 12]
        for i in range(self.dim):
            for freq in frequencies:
                harmonic += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric saddle point structure with variable repulsion
        saddle = 0.0
        for i in range(self.dim - 1):
            if x_norm[i] > x_norm[i+1]:
                saddle += (x_norm[i]**2 - x_norm[i+1]**2)**2 * np.exp(-0.5 * (x_norm[i] + x_norm[i+1])**2)
            else:
                saddle += (x_norm[i+1]**2 - x_norm[i]**2)**2 * np.exp(-0.5 * (x_norm[i] + x_norm[i+1])**2)
        
        # Add noise term with controlled variance
        noise = 0.05 * np.random.normal(0, 1)
        
        return logistic + gaussian + corridor + poly_interaction + harmonic + saddle + noise