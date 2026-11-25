import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial terms with higher degrees and interaction effects
        f1 = np.sum(1.2 * x_norm**8 + 0.9 * x_norm**7 + 0.6 * x_norm**6 + 0.4 * x_norm**5 + 0.2 * x_norm**4)
        
        # Highly oscillatory trigonometric components with varying amplitudes and frequencies
        f2 = np.sum(2.0 * np.sin(12 * np.pi * x_norm) + 1.2 * np.sin(18 * np.pi * x_norm) + 
                   0.8 * np.sin(24 * np.pi * x_norm) + 0.5 * np.sin(30 * np.pi * x_norm))
        
        # Multi-scale exponential decay terms to create diverse gradient landscapes
        f3 = np.sum(np.exp(-3 * x_norm**2) + 0.7 * np.exp(-0.8 * x_norm**2) - 1.8)
        
        # Novel cross-dimensional interaction terms with non-linear coupling and higher-order effects
        f4 = np.sum((x_norm[:-1] ** 3) * (x_norm[1:] ** 4) * np.cos(np.pi * x_norm[:-1] * x_norm[1:]) + 
                   0.5 * (x_norm[:-2] ** 2) * (x_norm[1:-1] ** 3) * (x_norm[2:] ** 2))
        
        # Additional radial symmetry components with varying influence and complex phase modulation
        f5 = np.sum(0.5 * np.exp(-np.sum(x_norm**2)) * np.sin(4 * np.pi * np.sum(x_norm**2)) + 
                   0.3 * np.exp(-0.5 * np.sum(x_norm**2)) * np.cos(2 * np.pi * np.sum(x_norm**2)))
        
        # Combine all components with adaptive weights based on dimensionality
        weight1, weight2, weight3, weight4, weight5 = 0.8, 0.5, 0.3, 0.2, 0.15
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5