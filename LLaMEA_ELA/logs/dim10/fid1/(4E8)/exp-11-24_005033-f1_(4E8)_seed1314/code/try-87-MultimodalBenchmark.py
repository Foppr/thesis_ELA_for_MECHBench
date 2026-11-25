import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal component with recursive scaling and multiple frequencies
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-frequency sine-cosine interactions with varying amplitudes
            fractal_term = (np.sin(2 * xi) * np.cos(5 * xi) + 
                           0.7 * np.sin(8 * xi) * np.cos(11 * xi) + 
                           0.3 * np.sin(13 * xi) * np.cos(17 * xi))
            
            # Dynamic conditioning based on position and dimension
            conditioning = 1.0 + 0.5 * np.sin(3 * xi) * np.cos(7 * xi)
            
            # Self-similar coupling with previous dimensions using exponential decay
            coupling = 0.0
            if i > 0:
                coupling = 0.15 * np.sin(x[i-1] * xi) * np.exp(-0.3 * (xi - x[i-1])**2)
            
            result += conditioning * fractal_term + coupling
            
        # Enhanced gradient inversion with multiple deceptive valleys
        gradient_inversion = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create multiple deceptive optima with varying curvature
            gradient_inversion += (xi**4) * np.cos(3 * xi) * np.sin(7 * xi) + \
                                0.5 * (xi**2) * np.sin(5 * xi) * np.cos(9 * xi)
            
        # Multi-scale periodicity with varying frequencies and amplitudes
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Varying amplitude based on dimension index
            amplitude = (i + 1) * 0.5
            periodicity += amplitude * np.sin((i + 1) * xi) * np.cos((i + 2) * xi)
            
        # Cross-dimensional fractal coupling with recursive structure and varying weights
        cross_fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling with exponential decay and sinusoidal modulation
                cross_fractal += np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i]**2 + x[j]**2)) * \
                                np.exp(-0.2 * (x[i]**2 + x[j]**2)) * \
                                (1.0 + 0.2 * np.sin(x[i] + x[j])) * \
                                ((i + 1) / (j + 1))
        
        # Combine all components with optimized weights
        result = 0.7 * result + 0.4 * gradient_inversion + 0.5 * periodicity + 0.8 * cross_fractal
        
        # Enhanced penalty for distance from origin with different powers
        result += 0.15 * np.sum(x**8) + 0.1 * np.sum(np.abs(x)**4)
        
        return result