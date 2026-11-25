import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial terms with higher degrees and interaction effects
        f1 = np.sum(1.2 * x_norm**7 + 0.9 * x_norm**6 + 0.4 * x_norm**5 + 0.2 * x_norm**4)
        
        # Highly oscillatory trigonometric components with varying amplitudes and frequencies
        f2 = np.sum(2.0 * np.sin(12 * np.pi * x_norm) + 1.0 * np.sin(18 * np.pi * x_norm) + 
                   0.5 * np.sin(24 * np.pi * x_norm) + 0.3 * np.sin(30 * np.pi * x_norm))
        
        # Multi-scale exponential decay terms with varying rates
        f3 = np.sum(np.exp(-3 * x_norm**2) + 0.7 * np.exp(-1.0 * x_norm**2) - 1.7)
        
        # Novel cross-dimensional interaction terms with non-linear coupling and directional influence
        f4 = np.sum((x_norm[:-1] ** 3) * (x_norm[1:] ** 2) * np.sin(np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Additional radial symmetry components with varying influence and phase shifts
        f5 = np.sum(0.4 * np.exp(-np.sum(x_norm**2)) * np.cos(4 * np.pi * np.sum(x_norm**2)))
        
        # Cross-dimensional coupling with sinusoidal modulation
        f6 = np.sum(np.sin(np.pi * x_norm[:-1] + np.pi * x_norm[1:]) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Combine all components with adaptive weights based on dimensionality
        weight1, weight2, weight3, weight4, weight5, weight6 = 0.8, 0.5, 0.3, 0.2, 0.15, 0.1
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5 + weight6 * f6