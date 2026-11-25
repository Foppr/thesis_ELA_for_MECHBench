import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay interaction terms with dynamic coupling and phase modulation
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                rate = 0.6 + 0.4 * np.sin(i * 0.4) * np.cos(j * 0.2) * np.sin(0.15 * (i + j))
                phase = 0.4 * np.sin(i * 0.7) + 0.2 * np.cos(j * 0.5)
                exp_interaction += np.exp(-rate * dist) * np.sin(3.5 * (x[i] + x[j]) + phase)
        
        # Multi-frequency trigonometric wave interference with amplitude modulation and spatial coupling
        wave_interference = np.sum(np.sin(2.5 * x) * np.cos(4.5 * x) * np.sin(6.5 * x) * np.cos(1.5 * x) * 
                                  (1.0 + 0.15 * np.sin(0.4 * x)) * np.exp(-0.08 * np.abs(x)))
        
        # Enhanced adaptive noise injection with position-dependent amplitude and frequency
        noise = 0.0
        for i in range(self.dim):
            amplitude = 0.12 + 0.06 * (x[i] / 5.0)**2
            frequency = 10.0 + 3.0 * np.sin(0.25 * x[i])
            noise += amplitude * np.sin(frequency * x[i] + i * 0.4) * np.cos(7.0 * x[i] - i)
        
        # Multi-scale harmonic component with variable amplitudes, frequencies, and spatial correlation
        harmonic = np.sum((1.0 + 0.25 * np.sin(x)) * np.exp(-0.3 * x**2) * 
                          np.sin(2.5 * x) * np.cos(1.0 * x) * (1.0 + 0.08 * np.cos(0.6 * x)))
        
        # Novel asymmetric conditioning with exponential scaling and threshold adaptation
        condition = np.sum(np.exp(0.3 * np.abs(x)) * np.sin(1.5 * x)**2 + 
                          0.4 * np.sin(0.7 * x) * np.cos(1.0 * x))
        
        # Cross-dimensional coupling terms with polynomial interaction and nonlinear transformation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited range coupling
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(0.4 * (x[i] + x[j])) * np.exp(-0.08 * abs(x[i] - x[j]))
        
        # Combined fitness value with weighted components and additional cross-dimensional influence
        return 0.35 * exp_interaction + 0.2 * wave_interference + 0.18 * noise + 0.17 * harmonic + 0.08 * condition + 0.02 * cross_terms