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
        
        # Enhanced chaotic fractal gradient structure with higher frequency modulation and adaptive scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(3 ** (i+1) * x[i]) * np.cos(3 ** (i+1) * x[i]) * (1 + 0.1 * np.sin(2 * x[i]))
        
        # Multi-scale Gaussian peaks with dynamic centers, widths, and adaptive amplitudes
        gaussian = 0.0
        scales = [1.0, 0.5, 2.0]
        for i in range(self.dim):
            for scale in scales:
                center = scale * np.sin(x[i])
                width = 0.5 + 0.5 * np.cos(x[i])
                amplitude = 1.0 + 0.3 * np.sin(3 * x[i])
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Modified cross-dimensional coupling with stronger exponential interactions and adaptive weights
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 1.0 + 0.2 * np.sin(x[i] + x[j])
                cross += weight * np.exp(-0.3 * ((x[i] - x[j]) ** 2)) * (x[i] ** 2 + x[j] ** 2)
        
        # Dynamic multi-scale resonance peaks with logarithmic scaling and adaptive phase shifts, slightly modified
        resonance = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(x[i])
            resonance += np.sin(10 * x[i] + phase_shift) * np.cos(5 * x[i] + phase_shift) * np.log(np.abs(x[i]) + 1.5)
        
        # Enhanced asymmetric gradient deception through adaptive polynomial and trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            poly_term = x[i] ** 3 - 2 * x[i] ** 2 + x[i]
            trig_term = np.sin(2 * x[i]) + 0.5 * np.cos(3 * x[i])
            deception += poly_term * trig_term * (1 + 0.2 * np.sin(x[i]))
        
        # Combine all components with adjusted weights for improved algorithm discrimination
        return 0.25 * quantum + 0.20 * fractal + 0.20 * gaussian + 0.20 * cross + 0.12 * resonance + 0.03 * deception