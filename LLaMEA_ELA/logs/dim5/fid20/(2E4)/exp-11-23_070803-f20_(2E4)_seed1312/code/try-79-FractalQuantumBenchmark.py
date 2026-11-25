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
            for k in range(1, 7):  # Increased recursion depth
                fractal_term += (0.85 ** k) * np.sin(2 ** k * np.pi * xi) * np.cos(3 ** k * xi)
        
        # Quantum harmonic oscillator potential with complex coupling
        quantum_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Modified potential with additional nonlinear terms
            quantum_term += (xi**2 + 0.6 * np.sin(4 * xi) + 0.4 * np.cos(6 * xi)) * \
                           (1 + 0.3 * np.sin(2 * xi) * np.cos(3 * xi) + 0.1 * xi**3)
        
        # Adaptive gradient field with dimension-dependent modulation
        grad_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Modified modulation factor
            mod_factor = 1.0 + 0.7 * np.sin(i * np.pi / self.dim)  # Increased modulation
            grad_term += (xi**4 + 0.9 * xi**3 - 0.7 * xi**2 + 0.1 * xi) * mod_factor
            
        # Cross-dimensional coupling with fractal scaling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified distance metric
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_dist = dist * (1 + 0.4 * np.sin(5 * dist))  # Increased coupling strength
                coupling = np.exp(-fractal_dist**2) * (1 + 0.5 * np.cos(7 * fractal_dist))  # Stronger coupling
                cross_term += coupling * (x_norm[i]**2 + x_norm[j]**2)
        
        # Multi-scale periodic modulation with varying amplitudes
        periodic_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Additional frequency component and modified amplitudes
            periodic_term += (0.6 * np.sin(2 * xi) + 0.4 * np.sin(5 * xi) + 
                             0.3 * np.sin(8 * xi) + 0.2 * np.sin(10 * xi)) * (1 + 0.15 * np.cos(3 * xi))
        
        # Combine all components with adjusted weights
        result = 1.7 * fractal_term + 1.4 * quantum_term + 1.1 * grad_term + \
                0.9 * cross_term + 1.5 * periodic_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise