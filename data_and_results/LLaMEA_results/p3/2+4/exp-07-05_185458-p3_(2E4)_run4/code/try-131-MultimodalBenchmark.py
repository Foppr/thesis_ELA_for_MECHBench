import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-inspired oscillatory component with adaptive frequencies
        quantum = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * (1 + 0.5 * np.sin(i))
            amp = 1.0 + 0.3 * np.cos(i)
            quantum += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Adaptive polynomial interactions with dimension-dependent exponents
        poly = 0.0
        for i in range(self.dim):
            exp = 2 + 2 * np.sin(i * np.pi / self.dim)
            poly += (x_norm[i]**exp) * np.cos(x_norm[(i+1) % self.dim]) * np.sin(x_norm[(i+2) % self.dim])
        
        # Spherical harmonic component with increasing degree
        spherical = 0.0
        for i in range(self.dim):
            degree = i + 1
            spherical += np.cos(degree * np.arctan2(x_norm[i], x_norm[(i+1) % self.dim]))
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(x_norm[i] * x_norm[j])
        
        # Adaptive chaotic modulation with dynamic amplitude
        chaotic = 0.0
        for i in range(self.dim):
            amp = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            chaotic += amp * np.sin(10 * x_norm[i] + np.cos(5 * x_norm[i]))
        
        # High-frequency noise component with dimensionality scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i]) * (1 + 0.1 * i)
        
        # Final combined function with weighted components
        return 0.8 * quantum + 0.6 * poly + 0.4 * spherical + 0.3 * coupling + 0.2 * chaotic + 0.1 * noise + 0.05 * np.sum(x_norm**2)