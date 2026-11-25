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
                rate = 0.7 + 0.3 * np.sin(i * 0.5) * np.cos(j * 0.3) * np.sin(0.2 * (i + j))
                phase = 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(j * 0.6)
                chaotic_interaction += np.exp(-rate * dist) * np.sin(4.0 * (x[i] + x[j]) + phase)
        
        # Multi-frequency trigonometric wave interference with amplitude modulation and spatial coupling
        wave_interference = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x) * np.sin(7.0 * x) * np.cos(2.0 * x) * 
                                  (1.0 + 0.2 * np.sin(0.5 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Enhanced adaptive noise injection with position-dependent amplitude and frequency
        noise = 0.0
        for i in range(self.dim):
            amplitude = 0.15 + 0.08 * (x[i] / 5.0)**2
            frequency = 12.0 + 4.0 * np.sin(0.3 * x[i])
            noise += amplitude * np.sin(frequency * x[i] + i * 0.5) * np.cos(8.0 * x[i] - i)
        
        # Multi-scale harmonic component with variable amplitudes, frequencies, and spatial correlation
        harmonic = np.sum((1.0 + 0.3 * np.sin(x)) * np.exp(-0.4 * x**2) * 
                          np.sin(3.0 * x) * np.cos(1.5 * x) * (1.0 + 0.1 * np.cos(0.7 * x)))
        
        # Novel asymmetric conditioning with exponential scaling and threshold adaptation
        condition = np.sum(np.exp(0.4 * np.abs(x)) * np.sin(2.0 * x)**2 + 
                          0.5 * np.sin(0.8 * x) * np.cos(1.2 * x))
        
        # Cross-dimensional coupling terms with polynomial interaction and nonlinear transformation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended range coupling
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] + x[j])) * np.exp(-0.1 * abs(x[i] - x[j]))
        
        # Combined fitness value with weighted components and additional cross-dimensional influence
        return 0.4 * chaotic_interaction + 0.25 * wave_interference + 0.15 * noise + 0.12 * harmonic + 0.06 * condition + 0.02 * cross_terms