import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like self-similar structure with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                fractal += np.sin(10 * distance) * np.cos(5 * distance) * np.exp(-0.1 * distance**2)
        
        # Quantum interference pattern with complex phase interactions
        quantum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_diff = x_norm[i] + x_norm[j]
                quantum += np.sin(3 * phase_diff) * np.cos(7 * phase_diff) * np.exp(-0.05 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Adaptive conditioning based on dimensionality and input magnitude
        adaptive = np.sum(np.sin(15 * x_norm) * np.cos(10 * x_norm) * (1 + 0.5 * np.abs(x_norm)))
        
        # Multi-scale oscillation with exponentially varying frequencies
        multi_scale = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            multi_scale += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.exp(-0.02 * x_norm[i]**2)
        
        # Peak attraction with logarithmic basin and chaotic perturbation
        peak_attraction = np.sum(np.exp(-0.5 * (x_norm - 0.3)**2) * np.sin(20 * x_norm)**2)
        
        # Cross-dimensional coupling with asymmetric interaction weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x_norm[i]**2 + x_norm[j]**2) * np.sin(2 * (x_norm[i] - x_norm[j])) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Combine all components with dimensionality-dependent weights
        return 1.2 * fractal + 1.8 * quantum + 0.9 * adaptive + 1.5 * multi_scale + 1.1 * peak_attraction + 0.7 * coupling