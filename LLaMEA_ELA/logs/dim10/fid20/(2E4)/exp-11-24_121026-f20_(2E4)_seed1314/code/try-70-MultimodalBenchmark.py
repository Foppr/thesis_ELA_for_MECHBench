import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency trigonometric terms with varying amplitudes
        f2 = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm)**3)
        
        # Exponential barrier terms with variable decay rates
        f3 = np.sum(np.exp(-x_norm**2 * (1 + 0.5 * np.sin(10 * x_norm))) - 1.0)
        
        # Polynomial with sinusoidal modulation for additional complexity
        f4 = np.sum((x_norm**5 + 0.5 * x_norm**3) * np.sin(15 * x_norm))
        
        # Adaptive chaotic term with dynamic frequency modulation
        f5 = np.sum(np.sin(np.pi * x_norm * (1 + 0.3 * np.sin(20 * x_norm)))**4)
        
        # Mixed exponential and polynomial terms for ruggedness
        f6 = np.sum(np.exp(-x_norm**4) * (x_norm**2 + 0.3 * x_norm))
        
        # Additional high-frequency component with amplitude modulation
        f7 = 0.5 * np.sum(np.sin(40 * x_norm**2) * np.cos(12 * x_norm)**2)
        
        # Fourth-order polynomial with random-like coefficients
        f8 = 0.2 * np.sum((x_norm**4 + 0.7 * x_norm**3 - 0.5 * x_norm**2 + 0.2 * x_norm)**2)
        
        # Variable frequency sinusoidal modulation
        f9 = 0.3 * np.sum(np.sin(20 * x_norm * np.cos(8 * x_norm))**3)
        
        # Combined exponential and trigonometric term
        f10 = 0.15 * np.sum(np.exp(-x_norm**2) * np.sin(18 * x_norm)**2)
        
        return f1 + 0.4 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.1 * f6 + 0.08 * f7 + 0.06 * f8 + 0.05 * f9 + 0.04 * f10