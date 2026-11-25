import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like recursive structure with harmonic modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Base fractal component with recursive scaling
            fractal_term = np.sin(3 * xi) * np.cos(7 * xi) + 0.5 * np.sin(9 * xi) * np.cos(13 * xi)
            
            # Dynamic harmonic modulation based on position
            modulation = 1.0 + 0.3 * np.sin(2 * xi) * np.cos(4 * xi)
            
            # Self-similar coupling with previous dimensions
            coupling = 0.0
            if i > 0:
                coupling = 0.2 * np.sin(x[i-1] * xi) * np.exp(-0.5 * (xi - x[i-1])**2)
            
            result += modulation * fractal_term + coupling
            
        # Gradient inversion component
        gradient_inversion = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create deceptive valleys by inverting gradients
            gradient_inversion += (xi**3) * np.cos(5 * xi) * np.sin(2 * xi)
            
        # Multi-scale periodicity with varying frequencies
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            periodicity += (i + 1) * np.sin((i + 1) * xi) * np.cos((i + 1) * xi)
            
        # Cross-dimensional fractal coupling with recursive structure
        cross_fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive coupling that depends on previous dimensions
                cross_fractal += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                                np.exp(-0.1 * (x[i]**2 + x[j]**2)) * \
                                (1.0 + 0.1 * np.sin(x[i] + x[j]))
        
        # Combine all components with different weights
        result = 0.8 * result + 0.3 * gradient_inversion + 0.4 * periodicity + 0.7 * cross_fractal
        
        # Add penalty for distance from origin to encourage convergence to global minimum
        result += 0.1 * np.sum(x**6) + 0.05 * np.sum(np.abs(x)**3)
        
        return result