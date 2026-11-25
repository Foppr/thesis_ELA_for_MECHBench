import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay interaction terms with varying rates and coupling strengths
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                rate = 0.7 + 0.3 * np.cos(i * 0.5) * np.sin(j * 0.6)
                exp_interaction += np.exp(-rate * dist) * np.cos(2.0 * (x[i] - x[j]))
        
        # Trigonometric wave interference with frequency modulation and phase shifts
        wave_interference = np.sum(np.cos(3.0 * x) * np.sin(5.0 * x) * np.cos(7.0 * x) * np.sin(4.0 * x))
        
        # Adaptive noise injection with amplitude scaling based on position
        noise = 0.0
        for i in range(self.dim):
            amplitude = 0.15 + 0.03 * (x[i] / 5.0)**3
            noise += amplitude * np.cos(12.0 * x[i] + i) * np.sin(8.0 * x[i] - i)
        
        # Multi-scale harmonic component with variable amplitudes and frequencies
        harmonic = np.sum((0.9 + 0.1 * np.cos(x)) * np.exp(-0.3 * x**2) * np.cos(3.0 * x))
        
        # Asymmetric conditioning with exponential scaling and threshold adaptation
        condition = np.sum(np.exp(0.4 * np.abs(x)) * np.cos(2.0 * x)**2)
        
        # Combined fitness value with weighted components
        return 0.25 * exp_interaction + 0.3 * wave_interference + 0.25 * noise + 0.15 * harmonic + 0.05 * condition