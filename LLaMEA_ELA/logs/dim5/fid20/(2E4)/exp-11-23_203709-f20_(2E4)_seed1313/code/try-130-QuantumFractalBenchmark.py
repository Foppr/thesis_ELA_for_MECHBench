import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum-like parameters for each dimension
        self.quantum_params = [np.sin(i * 0.7 + 1.0) * 2.0 + 3.0 for i in range(dim)]
        self.fractal_params = [np.cos(i * 0.5 + 0.5) * 1.5 + 2.5 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum interference component with complex phase modulation
        quantum = 0.0
        for i in range(self.dim):
            phase = self.quantum_params[i] * x[i]
            quantum += np.sin(phase) * np.cos(2 * phase) + np.cos(phase) * np.sin(2 * phase)
        
        # Fractal-like self-similarity with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scale = self.fractal_params[i]
            fractal += (x[i] ** 2 + scale) * np.sin(scale * x[i]) + (x[i] ** 3 + scale) * np.cos(scale * x[i])
        
        # Dynamic dimensional coupling with harmonic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j])) * (i + j)
        
        # Adaptive noise with fractal correlation structure
        noise = 0.0
        for i in range(self.dim):
            amp = 0.2 + 0.3 * np.sin(0.4 * i + 1.2)
            noise += amp * np.random.normal(0, 1)
        
        # Combined function with quantum-scaling factors
        total = 1.5 * quantum + 1.0 * fractal + 0.7 * coupling + 0.2 * noise
        
        return total