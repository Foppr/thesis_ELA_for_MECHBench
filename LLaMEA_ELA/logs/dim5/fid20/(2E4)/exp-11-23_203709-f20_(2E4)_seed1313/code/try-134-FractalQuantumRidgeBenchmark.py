import numpy as np

class FractalQuantumRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimensions and quantum parameters
        self.fractal_dims = [0.5 + 0.3 * np.sin(i * 0.4 + 1.2) for i in range(dim)]
        self.quantum_params = [np.cos(i * 0.6 + 0.8) * 2.0 + 3.0 for i in range(dim)]
        self.ridge_params = [np.sin(i * 0.5 + 1.0) * 1.5 + 2.5 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based self-similarity component
        fractal = 0.0
        for i in range(self.dim):
            dim_factor = self.fractal_dims[i]
            fractal += (x[i] ** 2 + 1e-8) ** (dim_factor * 0.5) * np.sin(x[i] * 3.0)
        
        # Quantum-like interference pattern
        quantum = 0.0
        for i in range(self.dim):
            param = self.quantum_params[i]
            quantum += np.sin(param * x[i]) * np.cos(param * x[i] * 0.5) + \
                       np.sin(param * x[i] * 1.5) * np.cos(param * x[i])
        
        # Adaptive ridge structure with varying curvature
        ridge = 0.0
        for i in range(self.dim):
            param = self.ridge_params[i]
            ridge += (x[i] ** 2 + param) * np.exp(-param * x[i] ** 2)
        
        # Cross-dimensional coupling with fractal scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_i = 0.7 + 0.3 * np.sin(0.4 * (i + j) + 1.3)
                scale_j = 0.6 + 0.4 * np.cos(0.4 * (i - j) + 0.9)
                coupling += (x[i] ** 3 + x[j] ** 3) * scale_i * scale_j
        
        # Combined function with dynamic weights
        total = 1.5 * fractal + 1.0 * quantum + 0.8 * ridge + 0.6 * coupling
        
        return total