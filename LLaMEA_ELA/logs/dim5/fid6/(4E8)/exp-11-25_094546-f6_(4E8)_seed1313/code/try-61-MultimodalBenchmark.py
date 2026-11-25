import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial terms with higher degrees and interaction effects
        f1 = np.sum(1.5 * x_norm**9 + 1.1 * x_norm**8 + 0.8 * x_norm**7 + 0.5 * x_norm**6 + 0.3 * x_norm**5)
        
        # Highly oscillatory trigonometric components with varying amplitudes and frequencies
        f2 = np.sum(2.5 * np.sin(15 * np.pi * x_norm) + 1.5 * np.sin(20 * np.pi * x_norm) + 
                   1.0 * np.sin(25 * np.pi * x_norm) + 0.7 * np.sin(35 * np.pi * x_norm))
        
        # Multi-scale exponential decay terms to create diverse gradient landscapes
        f3 = np.sum(np.exp(-4 * x_norm**2) + 0.8 * np.exp(-1.2 * x_norm**2) - 2.0)
        
        # Novel cross-dimensional interaction terms with non-linear coupling and higher-order effects
        f4 = np.sum((x_norm[:-1] ** 4) * (x_norm[1:] ** 5) * np.cos(np.pi * x_norm[:-1] * x_norm[1:]) + 
                   0.6 * (x_norm[:-2] ** 3) * (x_norm[1:-1] ** 4) * (x_norm[2:] ** 3))
        
        # Additional radial symmetry components with varying influence and complex phase modulation
        f5 = np.sum(0.6 * np.exp(-np.sum(x_norm**2)) * np.sin(5 * np.pi * np.sum(x_norm**2)) + 
                   0.4 * np.exp(-0.6 * np.sum(x_norm**2)) * np.cos(3 * np.pi * np.sum(x_norm**2)))
        
        # Additional chaotic component to increase landscape irregularity
        f6 = np.sum(0.3 * np.sin(50 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)) + 
                   0.2 * np.cos(40 * np.pi * x_norm) * np.exp(-0.3 * np.sum(x_norm**2)))
        
        # Combine all components with adaptive weights based on dimensionality
        weight1, weight2, weight3, weight4, weight5, weight6 = 0.9, 0.6, 0.4, 0.3, 0.2, 0.1
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5 + weight6 * f6