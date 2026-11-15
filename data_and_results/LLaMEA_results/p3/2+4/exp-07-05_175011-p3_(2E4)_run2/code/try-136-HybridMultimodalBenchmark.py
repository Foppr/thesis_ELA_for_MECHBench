import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency weights for consistency
        self.freq_weights = np.arange(1, dim + 1) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        poly_base = np.sum((x_norm ** (2 + np.arange(self.dim) % 4)) * self.freq_weights)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_components = np.sum(np.sin(self.freq_weights * x_norm) * np.cos(self.freq_weights * x_norm))
        
        # Radial basis function with localized sharp minima
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-5.0 * np.sum((x_norm - np.sin(i * 0.5))**2)) * np.sin(10 * x_norm[i])
        
        # Adaptive conditioning based on dimensionality
        conditioning = np.sum(np.abs(x_norm) ** (1.5 + self.dim / 10.0))
        
        # Localized sharp minima with Gaussian peaks
        sharp_minima = 0.0
        for i in range(self.dim):
            peak_pos = np.sin(i * 0.7) * 0.5
            sharp_minima += np.exp(-10.0 * (x_norm[i] - peak_pos)**2) * np.cos(15 * (x_norm[i] - peak_pos))
        
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(3 * (x_norm[i] + x_norm[j])) * np.cos(2 * (x_norm[i] - x_norm[j]))
        
        # Global oscillation with amplitude modulation
        global_osc = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * (1 + 0.2 * np.sin(5 * x_norm)))
        
        # Combine all components with carefully tuned weights
        return 0.5 * poly_base + 1.2 * trig_components + 0.8 * rbf + 0.6 * conditioning + 1.0 * sharp_minima + 0.7 * cross_interaction + 1.5 * global_osc