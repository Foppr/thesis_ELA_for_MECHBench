import numpy as np

class AdaptiveTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Periodic trigonometric components with varying frequencies
        periodic = np.sum(np.sin(2 * np.pi * x_scaled) + 
                         0.7 * np.sin(4 * np.pi * x_scaled) + 
                         0.4 * np.sin(8 * np.pi * x_scaled) + 
                         0.2 * np.sin(16 * np.pi * x_scaled))
        
        # Exponential decay interactions between dimensions
        decay_interaction = 0.0
        for i in range(self.dim - 1):
            decay_interaction += np.exp(-0.5 * (x_scaled[i] - x_scaled[i+1])**2) * (i + 1)
        
        # Adaptive dimensionality scaling based on position
        adaptive_scaling = np.sum((1 + 0.5 * np.abs(x_scaled)) * np.cos(3 * np.pi * x_scaled))
        
        # Multi-scale fractal-like structure with self-similarity
        fractal_structure = 0.0
        for scale in [2, 4, 8]:
            fractal_structure += 0.3 * np.sum(np.sin(scale * np.pi * x_scaled) * 
                                            np.cos(scale * np.pi * x_scaled))
        
        # Cross-dimensional coupling with polynomial interactions
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            poly_coupling += (x_scaled[i]**2 + x_scaled[i+1]**2 + x_scaled[i+2]**2) * \
                           np.sin(2 * np.pi * (x_scaled[i] + x_scaled[i+1] + x_scaled[i+2]))
        
        # Gaussian hill structure with multiple peaks
        gaussian_peaks = 0.0
        for i in range(0, self.dim, 2):
            if i < self.dim:
                gaussian_peaks += np.exp(-0.5 * (x_scaled[i] - 0.5)**2) * \
                                np.exp(-0.5 * (x_scaled[i] + 0.5)**2)
        
        # Combined landscape with optimized weights
        return (0.3 * periodic + 0.25 * decay_interaction + 0.2 * adaptive_scaling + 
                0.15 * fractal_structure + 0.08 * poly_coupling + 0.02 * gaussian_peaks)