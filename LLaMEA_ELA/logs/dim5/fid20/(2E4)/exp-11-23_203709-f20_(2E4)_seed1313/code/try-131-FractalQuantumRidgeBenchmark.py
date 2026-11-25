import numpy as np

class FractalQuantumRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for each dimension
        self.fractal_params = [np.sin(i * 0.5 + 1.0) * 2.0 + 3.0 for i in range(dim)]
        self.quantum_params = [np.cos(i * 0.4 + 1.2) * 1.5 + 2.5 for i in range(dim)]
        self.ridge_params = [np.sin(i * 0.6 + 1.1) * 0.8 + 1.2 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like terrain component with varying scaling factors
        fractal = 0.0
        for i in range(self.dim):
            scale = self.fractal_params[i]
            fractal += scale * np.sin(x[i] * scale) * np.cos(x[i] * 0.5 * scale)
        
        # Quantum interference pattern with phase modulation
        quantum = 0.0
        for i in range(self.dim):
            phase = self.quantum_params[i]
            quantum += np.sin(x[i] * phase + np.pi/4) * np.cos(x[i] * phase) + \
                       np.cos(x[i] * phase + np.pi/3) * np.sin(x[i] * phase)
        
        # Adaptive ridge structure with dynamic curvature
        ridge = 0.0
        for i in range(self.dim):
            curvature = self.ridge_params[i]
            ridge += (x[i] ** 2 + curvature * np.sin(x[i])) ** 1.5
        
        # Cross-dimensional coupling with fractal-like interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])) * \
                           (self.fractal_params[i] + self.fractal_params[j])
        
        # Combined function with dynamic weighting
        total = 0.8 * fractal + 1.2 * quantum + 0.9 * ridge + 0.7 * coupling
        
        return total