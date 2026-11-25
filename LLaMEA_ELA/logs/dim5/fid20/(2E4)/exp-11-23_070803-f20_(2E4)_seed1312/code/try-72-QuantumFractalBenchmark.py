import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Quantum harmonic oscillator potential with fractal scaling
        quantum_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal frequency modulation based on position
            freq = 1.0 + 0.5 * np.sin(xi * np.pi * 4) * np.cos(xi * np.pi * 2)
            quantum_term += 0.5 * freq * xi**2 + 0.3 * xi**4
        
        # Fractal basin structure with recursive scaling
        basin_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Recursive fractal basin with varying depth
            depth = 1.0 + 0.3 * np.sin(xi * np.pi * 8) * np.cos(xi * np.pi * 4)
            basin_term += depth * (xi**6 + 0.7 * xi**5 + 0.4 * xi**3)
        
        # Adaptive gradient modulation with position-dependent weights
        grad_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive weight based on local curvature
            weight = 1.0 + 0.6 * np.sin(xi * np.pi * 3) * np.cos(xi * np.pi * 6)
            grad_term += weight * (xi**7 + 0.5 * xi**6 - 0.3 * xi**4)
        
        # Cross-dimensional fractal coupling with varying strength
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength that varies with distance
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = 0.8 + 0.4 * np.sin(dist * np.pi * 5)
                cross_term += coupling_strength * (x_norm[i]**3) * (x_norm[j]**2) * np.exp(-dist**2)
        
        # Multi-scale oscillatory component with varying frequencies
        oscillatory_term = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple frequency components
            freq1 = 2.0 + 0.5 * np.sin(xi * np.pi)
            freq2 = 3.0 + 0.3 * np.cos(xi * np.pi * 2)
            freq3 = 4.0 + 0.4 * np.sin(xi * np.pi * 3)
            oscillatory_term += (np.sin(freq1 * xi) + 0.5 * np.cos(freq2 * xi) + 0.3 * np.sin(freq3 * xi)) * \
                              (1 + 0.2 * np.cos(2 * xi))
        
        # Combine all components with adjusted weights
        result = 1.5 * quantum_term + 1.2 * basin_term + 1.3 * grad_term + \
                0.8 * cross_term + 1.1 * oscillatory_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise