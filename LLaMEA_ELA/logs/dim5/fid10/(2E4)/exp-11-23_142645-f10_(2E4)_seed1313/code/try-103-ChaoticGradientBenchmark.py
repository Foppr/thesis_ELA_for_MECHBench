import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interactions with dynamic coupling and phase modulation
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                rate = 0.6 + 0.4 * np.sin(i * 0.6) * np.cos(j * 0.4) * np.sin(0.25 * (i + j))
                phase = 0.6 * np.sin(i * 0.9) + 0.2 * np.cos(j * 0.7)
                chaotic_interaction += np.exp(-rate * dist) * np.sin(3.5 * (x[i] + x[j]) + phase)
        
        # Multi-frequency trigonometric wave interference with amplitude modulation and spatial coupling
        wave_interference = np.sum(np.sin(2.5 * x) * np.cos(4.5 * x) * np.sin(6.5 * x) * np.cos(1.5 * x) * 
                                  (1.0 + 0.25 * np.sin(0.4 * x)) * np.exp(-0.12 * np.abs(x)))
        
        # Enhanced adaptive noise injection with position-dependent amplitude and frequency
        noise = 0.0
        for i in range(self.dim):
            amplitude = 0.18 + 0.06 * (x[i] / 5.0)**2
            frequency = 13.0 + 3.0 * np.sin(0.35 * x[i])
            noise += amplitude * np.sin(frequency * x[i] + i * 0.4) * np.cos(7.5 * x[i] - i)
        
        # Multi-scale harmonic component with variable amplitudes, frequencies, and spatial correlation
        harmonic = np.sum((1.0 + 0.25 * np.sin(x)) * np.exp(-0.35 * x**2) * 
                          np.sin(2.5 * x) * np.cos(1.8 * x) * (1.0 + 0.12 * np.cos(0.6 * x)))
        
        # Novel asymmetric conditioning with exponential scaling and threshold adaptation
        condition = np.sum(np.exp(0.35 * np.abs(x)) * np.sin(1.8 * x)**2 + 
                          0.45 * np.sin(0.7 * x) * np.cos(1.1 * x))
        
        # Cross-dimensional coupling terms with polynomial interaction and nonlinear transformation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced range coupling
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(0.4 * (x[i] + x[j])) * np.exp(-0.15 * abs(x[i] - x[j]))
        
        # Combined fitness value with weighted components and additional cross-dimensional influence
        return 0.35 * chaotic_interaction + 0.3 * wave_interference + 0.12 * noise + 0.14 * harmonic + 0.05 * condition + 0.04 * cross_terms