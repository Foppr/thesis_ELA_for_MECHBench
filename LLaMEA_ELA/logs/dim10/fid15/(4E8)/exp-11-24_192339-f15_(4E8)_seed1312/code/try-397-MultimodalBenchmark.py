import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient component with quantum-like interference
        chaotic_grad = 0
        for i in range(self.dim):
            # Quantum-inspired oscillatory modulation
            quantum_mod = np.sin(x[i] * np.pi * (1 + 0.3 * np.sin(2 * x[i] + 0.5 * self.dim)))
            chaotic_grad += quantum_mod * np.cos(1.5 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Modified ridge structure with adaptive scaling
        ridge = 0
        for i in range(self.dim):
            # Fractal-inspired scaling factor
            fractal_scale = 1.0 + 0.4 * np.sin(0.8 * x[i] + self.dim * 0.25) * np.cos(0.6 * x[i])
            ridge += (x[i]**2) * fractal_scale * np.exp(-0.15 * x[i]**2)
        
        # Saddle point structure with multi-dimensional coupling and dynamic phase
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Dynamic phase modulation based on dimension
                phase = 0.5 * np.sin(0.4 * (x[i] + x[j]) + self.dim * 0.3)
                saddle += (x[i] * x[j]) * np.sin(0.4 * (x[i]**2 + x[j]**2) + phase)
        
        # Quantum-inspired harmonic interference with time-varying frequencies
        harmonic = 0
        for i in range(self.dim):
            # Time-varying frequency based on dimension
            freq = 1.2 + 0.6 * np.sin(0.8 * x[i] + self.dim * 0.4) * np.cos(0.3 * x[i])
            harmonic += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.08 * x[i]**2)
        
        # Adaptive fractal scaling component
        fractal = 0
        for i in range(self.dim):
            # Multi-scale fractal modulation
            scale_factor = 1.0 + 0.5 * np.sin(0.6 * x[i] + self.dim * 0.3) * np.cos(0.4 * x[i])
            fractal += np.log(1 + x[i]**2) * scale_factor * np.exp(-0.2 * x[i]**2)
        
        # Combined landscape with dynamic weights and enhanced non-separability
        weight1 = 0.35 + 0.15 * np.sin(self.dim * 0.2)
        weight2 = 0.25 + 0.15 * np.cos(self.dim * 0.25)
        weight3 = 0.2 + 0.15 * np.sin(self.dim * 0.3)
        weight4 = 0.2 + 0.15 * np.cos(self.dim * 0.35)
        
        return weight1 * chaotic_grad + weight2 * ridge + weight3 * saddle + weight4 * fractal