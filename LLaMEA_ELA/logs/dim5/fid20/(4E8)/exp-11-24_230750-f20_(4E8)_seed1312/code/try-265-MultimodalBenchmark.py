import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component
        quantum = 0.0
        for i in range(self.dim):
            quantum += (np.sin(x[i]) * np.cos(x[i])) ** 2 + 0.1 * x[i] ** 4
        
        # Enhanced chaotic fractal gradient structure with higher frequency modulation
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(3 ** (i+1) * x[i]) * np.cos(3 ** (i+1) * x[i])
        
        # Multi-scale Gaussian peaks with dynamic centers and widths
        gaussian = 0.0
        scales = [1.0, 0.5, 2.0]
        for i in range(self.dim):
            for scale in scales:
                center = scale * np.sin(x[i])
                width = 0.5 + 0.5 * np.cos(x[i])
                gaussian += np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Modified cross-dimensional coupling with stronger exponential interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross += np.exp(-0.3 * ((x[i] - x[j]) ** 2)) * (x[i] ** 2 + x[j] ** 2)
        
        # Dynamic multi-scale resonance peaks with logarithmic scaling
        resonance = 0.0
        for i in range(self.dim):
            resonance += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.log(np.abs(x[i]) + 1)
        
        # Enhanced asymmetric gradient deception through polynomial and trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            deception += (x[i] ** 3 - 2 * x[i] ** 2 + x[i]) * np.sin(2 * x[i])
        
        # Combine all components with slightly altered weights
        return 0.25 * quantum + 0.18 * fractal + 0.22 * gaussian + 0.22 * cross + 0.1 * resonance + 0.03 * deception