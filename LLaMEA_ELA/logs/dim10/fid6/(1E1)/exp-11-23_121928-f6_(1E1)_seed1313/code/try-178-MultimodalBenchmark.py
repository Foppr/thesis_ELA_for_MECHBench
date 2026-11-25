import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        f1 = np.sum(x_norm**4 + 0.3 * x_norm**6 + 0.1 * x_norm**8)
        
        # Trigonometric terms with multiple frequencies and phase shifts
        f2 = np.sum(np.sin(5.0 * x_norm) * np.cos(3.0 * x_norm) + 
                   np.sin(7.0 * x_norm) * np.cos(4.0 * x_norm) + 
                   np.sin(9.0 * x_norm) * np.cos(2.0 * x_norm))
        
        # Exponential interaction terms with cross-dimensional dependencies
        f3 = np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(2.0 * np.pi * x_norm) * 
                   np.cos(1.5 * np.pi * x_norm) * (1.0 + 0.2 * np.sin(self.dim * x_norm)))
        
        # Cross-dimensional interaction using pairwise products
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += (x_norm[i] * x_norm[j]) * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # Adaptive scaling factor based on dimensionality and input magnitude
        scale = 1.0 + 0.5 * np.log(self.dim + 1) + 0.3 * np.mean(np.abs(x_norm))
        
        # Fractal-like recursive component
        f5 = np.sum(np.sin(np.pi * x_norm * np.sin(2.0 * np.pi * x_norm)) * 
                   np.cos(np.pi * x_norm * np.cos(1.5 * np.pi * x_norm)))
        
        # Hybrid term combining logarithmic and trigonometric components
        f6 = np.sum(np.log(np.abs(x_norm) + 0.5) * np.sin(3.0 * np.pi * x_norm))
        
        # Additional chaotic component with dynamic frequency modulation
        freq_mod = np.sum(np.sin(2.5 * np.pi * x_norm * (1.0 + 0.3 * np.cos(self.dim * x_norm))) * 
                         np.cos(4.0 * np.pi * x_norm**2))
        
        # Combine all terms with appropriate weights
        result = scale * (0.6 * f1 + 0.3 * f2 - 0.2 * f3 + 0.1 * f4 + 0.05 * f5 + 0.03 * f6 + 0.02 * freq_mod)
        
        # Add a small penalty for large values to encourage convergence
        penalty = 0.01 * np.sum(x_norm**10)
        
        return result + penalty