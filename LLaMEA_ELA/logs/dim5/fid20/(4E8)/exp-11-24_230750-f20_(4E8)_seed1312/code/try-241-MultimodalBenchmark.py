import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator-inspired component with time-varying frequencies
        quantum = 0.0
        for i in range(self.dim):
            freq = 2 + 1.5 * np.sin(0.3 * i + np.sum(x))
            quantum += (x[i]**2) * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Fractal-like self-similar structure with modified logistic maps and cubic couplings
        fractal = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.05 * np.sin(0.7 * i)
            if i == 0:
                val = x[i]
            else:
                val = x[i-1]
            fractal += (x[i] - r * val * (1 - val))**3
        
        # Multi-scale Gaussian peaks with adaptive widths and dynamic positions
        gaussian_peaks = 0.0
        scales = [0.2, 0.5, 1.0, 2.0]
        for scale in scales:
            for i in range(self.dim):
                pos = 2 * np.sin(scale * i) + 0.5 * np.cos(0.3 * scale * i)
                width = 0.3 + 0.7 * np.abs(np.sin(0.2 * i))
                gaussian_peaks += np.exp(-0.5 * ((x[i] - pos) / width)**2) * np.sin(scale * x[i])
        
        # Adaptive penalty corridors with hyperbolic tangent scaling
        penalty_corridors = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_corridors += np.tanh(dist_from_center - 2.5) * np.exp(-0.3 * dist_from_center)
        
        # Enhanced cross-dimensional interactions with quantum coupling terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                distance = np.abs(x[i] - x[j])
                cross_interaction += coupling * np.exp(-0.2 * distance**2)
        
        # Log-periodic oscillatory component with multi-scale modulation
        log_osc = 0.0
        for i in range(self.dim):
            log_osc += np.sin(np.log(1 + np.abs(x[i])) * x[i]) * np.cos(np.log(1 + np.abs(x[i])) * x[i])
        
        # Combined fitness function with increased complexity and discrimination power
        return 0.25 * quantum + 0.20 * fractal + 0.20 * gaussian_peaks + 0.15 * penalty_corridors + 0.10 * cross_interaction + 0.10 * log_osc