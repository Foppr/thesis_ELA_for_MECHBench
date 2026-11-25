import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial terms with higher degrees and interaction effects
        f1 = np.sum(0.8 * x_norm**6 + 0.5 * x_norm**5 + 0.3 * x_norm**4 + 0.1 * x_norm**3)
        
        # Slightly modified trigonometric components with altered amplitudes and frequencies
        f2 = np.sum(1.6 * np.sin(11 * np.pi * x_norm) + 0.7 * np.sin(16 * np.pi * x_norm) + 
                   0.3 * np.sin(21 * np.pi * x_norm) + 0.15 * np.sin(26 * np.pi * x_norm))
        
        # Modified exponential decay terms to alter gradient characteristics
        f3 = np.sum(np.exp(-2.2 * x_norm**2) + 0.4 * np.exp(-0.6 * x_norm**2) - 1.4)
        
        # Revised cross-dimensional interaction terms with different coupling strength
        f4 = np.sum((x_norm[:-1] ** 2.5) * (x_norm[1:] ** 2.8) * np.cos(np.pi * x_norm[:-1] * x_norm[1:] * 0.5))
        
        # Adjusted radial symmetry components with modified influence
        f5 = np.sum(0.35 * np.exp(-np.sum(x_norm**2)) * np.sin(3.2 * np.pi * np.sum(x_norm**2)))
        
        # Combine all components with updated weights
        weight1, weight2, weight3, weight4, weight5 = 0.72, 0.38, 0.27, 0.16, 0.11
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5