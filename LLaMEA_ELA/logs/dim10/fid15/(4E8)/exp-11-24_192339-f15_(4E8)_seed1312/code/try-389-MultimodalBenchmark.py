import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-inspired oscillatory components with dynamic frequency
        fractal = 0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.5 * x[i] + self.dim * 0.3)
            amp = 1.2 + 0.4 * np.cos(0.7 * x[i] + self.dim * 0.4)
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.15 * x[i]**2)
        
        # Modified ridge structures with adaptive curvature and height
        ridges = 0
        for i in range(self.dim):
            height = 1.5 + 0.5 * np.sin(0.6 * x[i] + self.dim * 0.3)
            width = 0.9 + 0.3 * np.cos(0.4 * x[i])
            curvature = 1.2 + 0.4 * np.sin(0.8 * x[i] + self.dim * 0.2)
            ridge = height * np.exp(-0.5 * ((x[i] - 1.5) / width)**2 * curvature)
            ridges += ridge
        
        # Enhanced cross-dimensional coupling with multi-scale exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling_factor = np.exp(-0.3 * distance**2)
                coupling += coupling_factor * (x[i]**2 + x[j]**2) * np.sin(0.5 * distance)
        
        # Quantum-inspired oscillatory components with enhanced tunneling
        quantum = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3.5 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(2.5 * x[i])
            term3 = np.exp(-0.35 * x[i]**2) * np.sin(4.5 * x[i]**2)
            tunneling = 0.2 * np.sin(7.0 * x[i]) * np.exp(-0.15 * (x[i] - 1.0)**2)
            quantum += term1 + term2 + term3 + tunneling
        
        # Enhanced chaotic modulation with time-varying phase
        chaotic = 0
        for i in range(self.dim):
            phase = np.sin(0.7 * x[i] + self.dim * 0.25)
            modulator = 1.2 + 0.6 * np.cos(0.5 * x[i] + self.dim * 0.35)
            chaotic += modulator * np.sin(phase * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add cross-dimensional interaction with polynomial coupling
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] * x[j])**2 * np.sin(0.3 * (x[i] + x[j]))
        
        # Combine all components with optimized weights and scaling factors
        return 0.3 * fractal + 0.25 * ridges + 0.2 * coupling + 0.15 * quantum + 0.08 * chaotic + 0.02 * poly_interaction