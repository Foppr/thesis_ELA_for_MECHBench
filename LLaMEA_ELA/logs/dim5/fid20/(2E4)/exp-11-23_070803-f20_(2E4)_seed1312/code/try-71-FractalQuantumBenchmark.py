import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Fractal component with recursive self-similarity
        fractal_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Recursive fractal pattern with diminishing returns
            for k in range(1, 6):  # Depth of recursion
                fractal_term += (0.8 ** k) * np.sin(2 ** k * np.pi * xi) * np.cos(3 ** k * xi)
        
        # Quantum harmonic oscillator potential with complex coupling
        quantum_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Complex potential with multiple frequency components
            quantum_term += (xi**2 + 0.5 * np.sin(4 * xi) + 0.3 * np.cos(6 * xi)) * \
                           (1 + 0.2 * np.sin(2 * xi) * np.cos(3 * xi))
        
        # Adaptive gradient field with dimension-dependent modulation
        grad_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dimension-specific modulation factor
            mod_factor = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            grad_term += (xi**4 + 0.8 * xi**3 - 0.6 * xi**2) * mod_factor
            
        # Cross-dimensional coupling with fractal scaling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal distance metric
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_dist = dist * (1 + 0.3 * np.sin(5 * dist))
                coupling = np.exp(-fractal_dist**2) * (1 + 0.4 * np.cos(7 * fractal_dist))
                cross_term += coupling * (x_norm[i]**2 + x_norm[j]**2)
        
        # Multi-scale periodic modulation with varying amplitudes
        periodic_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple periodic components with different frequencies and amplitudes
            periodic_term += (0.5 * np.sin(2 * xi) + 0.3 * np.sin(5 * xi) + 
                             0.2 * np.sin(8 * xi)) * (1 + 0.1 * np.cos(3 * xi))
        
        # Combine all components with adaptive weights
        result = 1.5 * fractal_term + 1.2 * quantum_term + 1.0 * grad_term + \
                0.8 * cross_term + 1.3 * periodic_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise