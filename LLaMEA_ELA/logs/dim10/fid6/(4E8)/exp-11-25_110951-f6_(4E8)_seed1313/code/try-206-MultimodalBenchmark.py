import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-based self-similar components with logarithmic spiral patterns
        fractal_term = 0.0
        for i in range(self.dim):
            # Logarithmic spiral pattern with varying scales
            r = np.sqrt(x_norm[i]**2 + 0.1)
            theta = np.arctan2(x_norm[i], 0.1)
            spiral_component = np.sin(5 * r) * np.cos(3 * theta) + \
                              0.5 * np.cos(7 * r) * np.sin(4 * theta)
            fractal_term += spiral_component
        
        # Multi-resolution harmonic modulations with varying frequencies
        harmonic_term = 0.0
        for i in range(self.dim):
            # Combine multiple frequencies with different amplitudes
            harmonic_term += (1.0 + 0.5 * np.sin(2 * x_norm[i])) * \
                           (0.8 + 0.3 * np.cos(4 * x_norm[i])) * \
                           (0.6 + 0.4 * np.sin(8 * x_norm[i]))
        
        # Cross-dimensional interaction with scale-invariant coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-invariant interaction using distance metrics
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_term += np.sin(10 * dist) * np.exp(-dist**2)
        
        # Multi-scale ridge structures with fractal dimensionality
        ridge_term = 0.0
        for i in range(self.dim):
            # Create ridges with varying widths and heights
            ridge_term += np.exp(-0.5 * (x_norm[i] - 0.5)**2) * \
                         np.sin(15 * x_norm[i]) + \
                         0.3 * np.exp(-0.3 * (x_norm[i] + 0.3)**2) * \
                         np.cos(12 * x_norm[i])
        
        # Boundary-sensitive fractal components
        boundary_term = 0.0
        for i in range(self.dim):
            # Fractal behavior near boundaries with exponential decay
            boundary_term += (np.exp(-x_norm[i]**2) * np.sin(3 * x_norm[i]) + 
                             0.5 * np.exp(-(x_norm[i] - 1)**2) * np.cos(5 * x_norm[i]))
        
        # Long-range correlation with multi-scale memory effects
        memory_term = 0.0
        for i in range(self.dim):
            # Incorporate influence from distant dimensions
            for j in range(self.dim):
                if i != j:
                    memory_term += np.sin(2 * (x_norm[i] - x_norm[j])) / (1 + abs(i - j))
        
        # Final combined function with weighted contributions
        return 0.3 * fractal_term + 0.25 * harmonic_term + 0.2 * cross_term + \
               0.1 * ridge_term + 0.1 * boundary_term + 0.05 * memory_term