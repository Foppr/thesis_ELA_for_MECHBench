import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Exponential decay terms with trigonometric modulation
        f2 = 0.3 * np.sum(np.exp(-2 * np.abs(x_norm)) * np.sin(8 * np.pi * x_norm))
        
        # Adaptive frequency sinusoidal components
        f3 = 0.25 * np.sum(np.cos(5 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * (1 + 0.5 * np.sin(3 * np.pi * x_norm)))
        
        # Higher-order polynomial with exponential weighting
        f4 = 0.2 * np.sum(x_norm**6 * np.exp(-0.5 * np.abs(x_norm)))
        
        # Cross-dimensional coupling with varying weights
        f5 = 0.15 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * (x_norm**2 + 0.2))
        
        # Non-linear interaction with polynomial decay
        f6 = 0.18 * np.sum(x_norm**3 * np.exp(-np.abs(x_norm)) * np.cos(9 * np.pi * x_norm))
        
        # Additional multi-modal component with frequency modulation
        f7 = 0.22 * np.sum(np.sin(3 * np.pi * x_norm) * np.tan(4 * np.pi * x_norm) * (1 + 0.3 * np.cos(5 * np.pi * x_norm)))
        
        # Combined polynomial and trigonometric term with adaptive parameters
        f8 = 0.12 * np.sum((x_norm**4 + 0.1) * np.sin(6 * np.pi * x_norm))
        
        # Small perturbation to enhance variability
        f9 = 0.08 * np.sum(np.exp(-3 * x_norm**2) * np.cos(10 * np.pi * x_norm))
        
        # Combine all components with carefully adjusted weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
        
        return result