import numpy as np

class FractalQuantumRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for each dimension with quantum-like frequencies
        self.fractal_params = [np.sin(i * 2.1 + 1.7) * 4.0 + 3.0 for i in range(dim)]
        self.quantum_params = [np.cos(i * 1.3 + 0.9) * 2.5 + 2.0 for i in range(dim)]
        self.ridge_params = [np.sin(i * 0.7 + 1.2) * 1.8 + 1.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based chaos component with self-similar patterns
        fractal = 0.0
        for i in range(self.dim):
            scale = self.fractal_params[i]
            fractal += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.5)
        
        # Quantum-like interference pattern component
        quantum = 0.0
        for i in range(self.dim):
            freq = self.quantum_params[i]
            quantum += np.sin(x[i] * freq + np.sin(x[i] * freq * 0.3)) * np.cos(x[i] * freq * 0.7)
        
        # Adaptive ridge structure with dynamic curvature
        ridge = 0.0
        for i in range(self.dim):
            curvature = self.ridge_params[i]
            ridge += (x[i] ** 2 + curvature * np.sin(x[i])) ** 1.5
        
        # Cross-dimensional quantum coupling with fractal modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_i = 0.8 + 0.2 * np.sin(0.4 * (i + j) + 1.7)
                mod_j = 0.6 + 0.4 * np.cos(0.2 * (i - j) + 1.9)
                coupling += (x[i] ** 3 + x[j] ** 3) * mod_i * mod_j
        
        # Adaptive noise injection with quantum amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            amp = 0.2 + 0.3 * np.sin(0.8 * i + 1.4)
            noise += amp * np.random.normal(0, 1)
        
        # Combined function with quantum scaling factors
        total = 1.5 * fractal + 1.3 * quantum + 0.9 * ridge + 0.7 * coupling + 0.4 * noise
        
        return total