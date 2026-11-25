import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic saddle point components with dynamic scaling
        chaotic = 0
        for i in range(self.dim):
            # Chaotic modulation with dynamic frequency and amplitude
            freq = 1.5 + 0.8 * np.sin(0.3 * x[i] + self.dim * 0.25)
            amp = 1.2 + 0.6 * np.cos(0.4 * x[i] + self.dim * 0.3)
            # Saddle point structure with exponential decay
            saddle = amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.15 * x[i]**2)
            chaotic += saddle
        
        # Modified ridge structures with adaptive curvature and height
        ridges = 0
        for i in range(self.dim):
            # Adaptive parameters based on dimension
            height = 1.5 + 0.5 * np.sin(0.6 * x[i] + self.dim * 0.3)
            width = 1.0 + 0.4 * np.cos(0.4 * x[i])
            curvature = 1.2 + 0.4 * np.sin(0.8 * x[i] + self.dim * 0.2)
            # Enhanced ridge structure with multi-scale scaling
            ridge = height * np.exp(-0.3 * ((x[i] - 1.5) / width)**2 * curvature)
            ridges += ridge
        
        # Quantum-inspired oscillatory components with tunneling effects
        quantum = 0
        for i in range(self.dim):
            # Multiple quantum-like terms with different frequencies and amplitudes
            term1 = np.exp(-0.4 * (x[i] - 2.0)**2) * np.sin(5.0 * x[i])
            term2 = np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(4.0 * x[i])
            term3 = np.exp(-0.2 * x[i]**2) * np.sin(6.0 * x[i]**2)
            # Tunneling effect with additional exponential decay
            tunneling = 0.2 * np.sin(7.0 * x[i]) * np.exp(-0.15 * (x[i] - 1.0)**2)
            quantum += term1 + term2 + term3 + tunneling
        
        # Cross-dimensional coupling with fractal-like decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-inspired distance measure
                distance = np.sqrt((x[i] - x[j])**2 + 0.1)
                coupling_factor = np.exp(-0.3 * distance**1.5)
                coupling += coupling_factor * (x[i]**2 + x[j]**2)
        
        # Enhanced multimodal structure with sinusoidal modulation
        modal = 0
        for i in range(self.dim):
            # Multi-scale sinusoidal components
            modal += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Combine all components with optimized weights and scaling
        return 0.22 * chaotic + 0.18 * ridges + 0.23 * coupling + 0.25 * quantum + 0.12 * modal