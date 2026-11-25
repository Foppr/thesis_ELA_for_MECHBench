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
                rate = 0.5 + 0.3 * np.sin(i * 0.7) * np.cos(j * 0.4)
                exp_interaction += np.exp(-rate * dist) * np.sin(3.0 * (x[i] + x[j]))
        
        # Trigonometric wave interference with frequency modulation and phase shifts
        wave_interference = np.sum(np.sin(2.5 * x) * np.cos(4.2 * x) * np.sin(6.1 * x) * np.cos(3.8 * x))
        
        # Adaptive noise injection with amplitude scaling based on position
        noise = 0.0
        for i in range(self.dim):
            amplitude = 0.1 + 0.05 * (x[i] / 5.0)**2
            noise += amplitude * np.sin(10.0 * x[i] + i) * np.cos(7.0 * x[i] - i)
        
        # Multi-scale harmonic component with variable amplitudes and frequencies
        harmonic = np.sum((0.8 + 0.2 * np.sin(x)) * np.exp(-0.5 * x**2) * np.sin(2.0 * x))
        
        # Asymmetric conditioning with exponential scaling and threshold adaptation
        condition = np.sum(np.exp(0.3 * np.abs(x)) * np.sin(1.5 * x)**2)
        
        # Combined fitness value with weighted components
        return 0.3 * exp_interaction + 0.25 * wave_interference + 0.2 * noise + 0.15 * harmonic + 0.1 * condition