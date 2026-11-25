import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component with higher-order terms
        quantum = 0.0
        for i in range(self.dim):
            quantum += (np.sin(x[i]) * np.cos(x[i])) ** 2 + 0.1 * x[i] ** 4 + 0.05 * np.sin(7 * x[i]) * np.cos(7 * x[i])
        
        # Enhanced chaotic fractal gradient structure with exponential scaling and adaptive modulation
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(3 ** (i+1) * x[i]) * np.cos(3 ** (i+1) * x[i]) * (1 + 0.2 * np.sin(2 * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        
        # Multi-scale Gaussian peaks with time-varying centers, widths, and amplitudes
        gaussian = 0.0
        scales = [1.0, 0.5, 2.0, 0.3]
        for i in range(self.dim):
            for scale in scales:
                center = scale * np.sin(x[i] + 0.5 * np.cos(2 * x[i]))
                width = 0.5 + 0.5 * np.cos(x[i] + 0.3 * np.sin(3 * x[i]))
                amplitude = 1.0 + 0.5 * np.sin(3 * x[i]) * np.cos(2 * x[i])
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Modified cross-dimensional coupling with hyperbolic and exponential interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 1.0 + 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                cross += weight * np.exp(-0.5 * ((x[i] - x[j]) ** 2)) * (np.tanh(x[i]) ** 2 + np.tanh(x[j]) ** 2)
        
        # Dynamic multi-scale resonance peaks with complex phase interactions and logarithmic scaling
        resonance = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(x[i] + 0.2 * np.cos(3 * x[i]))
            resonance += np.sin(10 * x[i] + phase_shift) * np.cos(5 * x[i] + phase_shift) * np.log(np.abs(x[i]) + 1) * np.exp(-0.05 * x[i] ** 2)
        
        # Enhanced asymmetric gradient deception through higher-order polynomial-trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            poly_term = x[i] ** 5 - 3 * x[i] ** 4 + 2 * x[i] ** 3 - x[i]
            trig_term = np.sin(2 * x[i]) + 0.5 * np.cos(3 * x[i]) + 0.1 * np.sin(5 * x[i])
            deception += poly_term * trig_term * (1 + 0.3 * np.sin(x[i] + 0.2 * np.cos(2 * x[i])))
        
        # Additional chaotic interference terms for increased complexity
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.1 * np.sin(15 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.2 * x[i] ** 2)
        
        # Combine all components with adjusted weights for improved algorithm discrimination
        return 0.20 * quantum + 0.25 * fractal + 0.20 * gaussian + 0.15 * cross + 0.10 * resonance + 0.07 * deception + 0.03 * chaos