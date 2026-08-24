import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic term for conditioning and global minimum
        quadratic = np.sum(x_norm**2)
        
        # Enhanced oscillatory sinusoidal terms with exponential growth and adaptive frequency
        oscillatory = np.sum(np.sin(15 * np.pi * x_norm) * np.exp(3 * np.abs(x_norm)))
        
        # Non-separable interaction term using Gaussian-like decay with dynamic scaling
        interaction = np.exp(-np.sum(x_norm**2) / (2 * (self.dim + 1)))
        
        # Saddle point structure with mixed polynomial terms and cross-terms
        saddle = np.sum(x_norm**4) - 0.3 * np.sum(x_norm**2) + 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Add a secondary multimodal component with sharper peaks
        secondary = np.sum(np.sin(20 * np.pi * x_norm) * np.exp(1.5 * np.abs(x_norm)))
        
        # Combine all components with varying weights
        return 0.4 * quadratic + 2.5 * oscillatory + 0.15 * interaction + 0.25 * saddle + 0.3 * secondary