import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-inspired oscillatory components with adaptive frequency
        fractal = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * x[i] + self.dim * 0.2)
            amp = 1.0 + 0.3 * np.cos(0.6 * x[i] + self.dim * 0.3)
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic ridge structures with varying curvature and height
        ridges = 0
        for i in range(self.dim):
            height = 1.0 + 0.4 * np.sin(0.5 * x[i] + self.dim * 0.25)
            width = 0.8 + 0.2 * np.cos(0.3 * x[i])
            curvature = 1.0 + 0.3 * np.sin(0.7 * x[i] + self.dim * 0.1)
            ridge = height * np.exp(-0.5 * ((x[i] - 1.0) / width)**2 * curvature)
            ridges += ridge
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling_factor = np.exp(-0.2 * distance**2)
                coupling += coupling_factor * (x[i]**2 + x[j]**2)
        
        # Adaptive multimodal structure with quantum-like tunneling
        quantum = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 2.5)**2) * np.sin(4.0 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 2.5)**2) * np.cos(3.0 * x[i])
            term3 = np.exp(-0.3 * x[i]**2) * np.sin(5.0 * x[i]**2)
            tunneling = 0.15 * np.sin(6.0 * x[i]) * np.exp(-0.1 * (x[i] - 1.0)**2)
            quantum += term1 + term2 + term3 + tunneling
        
        # Time-varying chaotic modulation
        chaotic = 0
        for i in range(self.dim):
            phase = np.sin(0.6 * x[i] + self.dim * 0.2)
            modulator = 1.0 + 0.5 * np.cos(0.4 * x[i] + self.dim * 0.3)
            chaotic += modulator * np.sin(phase * x[i]) * np.exp(-0.08 * x[i]**2)
        
        # Combine all components with optimized weights
        return 0.25 * fractal + 0.20 * ridges + 0.25 * coupling + 0.20 * quantum + 0.10 * chaotic