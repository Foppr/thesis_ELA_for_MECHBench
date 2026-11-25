import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Self-similar exponential peak structure with fractal scaling
        peak_term = 0.0
        for i in range(self.dim):
            # Create peaks with recursive scaling based on dimension
            scale = 1.0 + 0.3 * np.sin(self.dim * 0.1 + i * 0.2)
            peak = scale * np.exp(-0.5 * (x[i] - 2.0 * np.sin(i * 0.5))**2) * \
                   np.exp(-0.3 * (x[i] - 1.0)**4)
            peak_term += peak
        
        # Directional gradient field with fractal orientation
        grad_term = 0.0
        for i in range(self.dim):
            # Create directional bias with recursive pattern
            direction = np.sin(i * 0.3 + self.dim * 0.2) * np.cos(i * 0.4)
            grad = direction * (x[i] - 1.0)**3 * np.exp(-0.5 * (x[i] - 1.0)**2)
            grad_term += grad
        
        # Nested local optima with recursive positioning
        nested_term = 0.0
        for i in range(self.dim):
            # Create multiple nested valleys with varying depths
            valley1 = (x[i] - 1.0)**2 * np.exp(-0.2 * (x[i] - 1.0)**2)
            valley2 = (x[i] + 1.5)**4 * np.exp(-0.1 * (x[i] + 1.5)**2)
            # Recursive depth scaling
            depth_scale = 1.0 + 0.2 * np.sin(self.dim * 0.3 + i * 0.1)
            nested_term += depth_scale * (valley1 + valley2)
        
        # Cross-dimensional coupling with fractal strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on dimension and position
                strength = 0.5 * (1.0 + np.sin(i * 0.2 + j * 0.3 + self.dim * 0.1))
                coupling = strength * np.exp(-0.1 * (x[i] - x[j])**2) * \
                          (np.sin(x[i]) + np.cos(x[j]))
                cross_term += coupling
        
        # Scale-invariant structure with recursive dimensionality
        scale_term = 0.0
        for i in range(self.dim):
            # Create scale-invariant features using fractal-like components
            scale_factor = 1.0 + 0.1 * np.sin(self.dim * 0.4 + i * 0.3)
            scale_term += scale_factor * np.exp(-0.3 * x[i]**2) * \
                         np.sin(3.0 * x[i] + self.dim * 0.2)
        
        # Final weighted combination
        total = 0.3 * peak_term + 0.25 * grad_term + 0.2 * nested_term + \
                0.15 * cross_term + 0.1 * scale_term
        
        # Global scaling with fractal dimension effect
        global_scale = 1.0 + 0.15 * np.sin(self.dim * 0.3) * np.cos(self.dim * 0.2)
        
        return total * global_scale