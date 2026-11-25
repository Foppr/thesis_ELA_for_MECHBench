import numpy as np

class RotatingMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial harmonic term with varying frequencies and amplitudes
        radial_harmonic = 0.0
        for i in range(self.dim):
            radial_harmonic += (1.0 + 0.5 * np.sin(2.0 * x[i])) * (x[i]**2 + 0.1 * x[i]**4)
            
        # Angular rotation component with periodic dependencies
        angle = np.arctan2(x[1], x[0]) if self.dim >= 2 else 0.0
        rotation_term = 0.0
        for i in range(self.dim):
            rotation_term += np.sin(angle + i * 0.5) * np.cos(angle + i * 0.7) * x[i]**2
            
        # Multi-scale periodic grid with adaptive frequencies and amplitudes
        grid_terms = 0.0
        for i in range(self.dim):
            grid_terms += (2.0 + np.sin(3.0 * x[i])) * np.cos(4.0 * x[i]) + \
                         (1.5 + np.cos(2.5 * x[i])) * np.sin(3.5 * x[i]) + \
                         0.8 * np.sin(5.0 * x[i]) * np.cos(6.0 * x[i])
            
        # Cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.3 * np.sin((i + j) * 0.3)
                cross_coupling += weight * np.sin(2.0 * x[i]) * np.cos(2.0 * x[j])
                
        # Adaptive conditioning with exponential scaling
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1.0 + 0.2 * np.exp(-x[i]**2)) * x[i]**3
            
        # Fractal-like interference pattern with multiple overlapping sine waves
        interference = 0.0
        for i in range(self.dim):
            interference += np.sin(10.0 * x[i] + np.sin(5.0 * x[i])) + \
                          0.5 * np.cos(8.0 * x[i] + np.cos(4.0 * x[i]))
            
        return radial_harmonic + rotation_term + grid_terms + cross_coupling + conditioning + interference