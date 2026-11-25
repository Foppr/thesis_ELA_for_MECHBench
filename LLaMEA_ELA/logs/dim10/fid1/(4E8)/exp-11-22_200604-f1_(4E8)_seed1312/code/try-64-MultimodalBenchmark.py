import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term with varying coefficients
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes and chaotic modulations
        f2 = 0.6 * np.sum(np.sin(20 * np.pi * x_norm * np.cos(5 * x_norm)))
        
        # Add a quartic penalty term to create deeper valleys
        f3 = 0.1 * np.sum(x_norm**4)
        
        # Add an additional cubic term with non-uniform weights and chaotic interactions
        f4 = 0.15 * np.sum(x_norm**3 * np.sin(7 * x_norm))
        
        # Add a secondary trigonometric component with different frequency, amplitude, and cross-dimensional coupling
        f5 = 0.25 * np.sum(np.cos(15 * np.pi * x_norm**2 + 0.5 * np.sin(3 * x_norm)))
        
        # Add a cross-term interaction with higher-order polynomial coupling and chaotic modulations
        f6 = 0.08 * np.sum(x_norm[:-1] * x_norm[1:] * (x_norm[:-1]**3 + x_norm[1:]**3) * np.sin(4 * (x_norm[:-1] + x_norm[1:])))
        
        # Add a fifth-order polynomial term with non-linear frequency modulation
        f7 = 0.05 * np.sum(x_norm**5 * np.cos(6 * x_norm))
        
        # Add a sixth-order polynomial term to increase complexity and create more local minima
        f8 = 0.03 * np.sum(x_norm**6 * np.sin(8 * x_norm))
        
        # Add a chaotic sine-wave interaction between all dimensions
        f9 = 0.1 * np.sum(np.sin(25 * np.pi * np.prod(x_norm, axis=0)))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
        
        return result