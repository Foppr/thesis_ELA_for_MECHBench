import numpy as np

class HyperChaoticFractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis with nested fractal scaling
        r = np.sqrt(np.sum(x**2))
        hyperchaotic_radial = np.sum(np.exp(-0.3 * (x**2) / (1.0 + 0.5 * np.sin(8.0 * r) * np.cos(3.0 * r))) * 
                                   np.sin(4.0 * r + 0.4 * np.sin(9.0 * r)) * 
                                   np.cos(2.5 * r + 0.3 * np.cos(6.0 * r))) / self.dim
        
        # Nested fractal gradient field with multi-scale asymmetry
        nested_fractal = np.sum(np.abs(x)**1.7 * np.sin(x * np.cos(x)) * 
                               np.exp(-0.15 * np.abs(x)) * 
                               (1.0 + 0.3 * np.sin(4.0 * np.sum(x**2)) * np.cos(2.0 * r))) / self.dim
        
        # Dynamic quantum noise with entanglement modulation
        quantum_noise = np.sum(np.sin(x * (1.0 + 0.5 * np.sin(0.4 * r) * np.cos(0.3 * r))) * 
                             np.cos(x * (1.0 + 0.4 * np.cos(0.5 * r) * np.sin(0.2 * r))) * 
                             np.exp(-0.08 * r**2)) / self.dim
        
        # Cross-term quantum entanglement with fractal coupling
        entanglement = np.sum(np.sin(x[:-1] * x[1:] * (1.0 + 0.2 * np.sin(3.0 * np.sum(x)) * np.cos(2.0 * r))) * 
                            np.cos(x[:-1] + x[1:] + 0.4 * np.cos(4.0 * r) * np.sin(3.0 * np.sum(x)))) / (self.dim - 1)
        
        # Multi-scale fractal interference with hyperchaotic phase modulation
        multi_fractal = np.sum(np.sin(7.0 * x) * np.cos(5.0 * x) * 
                              np.exp(-0.05 * np.sum(x**2)) * 
                              (1.0 + 0.2 * np.sin(3.0 * r) * np.cos(2.0 * r))) / self.dim
        
        # Adaptive quantum conditioning with nested scaling
        quantum_cond = np.sum((x**2.5) * (1.0 + 0.6 * np.sin(0.7 * np.sum(x**2)) * np.cos(0.5 * r)) * 
                            np.cos(3.0 * x) * np.exp(-0.12 * np.abs(x))) / self.dim
        
        # Saddle-point with hyperchaotic harmonic components and entanglement
        hyper_saddle = np.sum(x**4 * np.cos(x) - x**5 * np.sin(x) + 
                            0.7 * x**3 * np.tan(x/4.0) * np.exp(-0.02 * r**2) * 
                            (1.0 + 0.2 * np.sin(5.0 * r))) / (self.dim * 15.0)
        
        # Quantum entanglement interference with phase coupling
        entangled_interference = np.sum(np.sin(x * np.cos(x * np.sin(x))) * 
                                      np.cos(x * np.sin(x * np.cos(x))) * 
                                      np.exp(-0.03 * r**2) * 
                                      (1.0 + 0.25 * np.sin(5.0 * r) * np.cos(4.0 * r))) / self.dim
        
        # Combined weighted sum of all components
        total = 0.20 * hyperchaotic_radial + 0.18 * nested_fractal + 0.15 * quantum_noise + 0.13 * entanglement + \
                0.12 * multi_fractal + 0.10 * quantum_cond + 0.08 * hyper_saddle + 0.04 * entangled_interference
        
        return total