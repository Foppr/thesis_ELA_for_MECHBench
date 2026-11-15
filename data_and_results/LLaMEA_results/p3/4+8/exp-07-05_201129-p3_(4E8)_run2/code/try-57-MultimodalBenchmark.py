import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with enhanced chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = r * (1.0 + 0.7 * np.sin(15 * r) * np.cos(8 * r) + 0.3 * np.sin(25 * r))
        
        # Nested sinusoidal terms with varying frequencies, amplitudes, and phase shifts
        nested = 0.0
        for i in range(1, min(7, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 3)
            phase = i * np.pi / 4
            nested += amp * np.sin(freq * np.pi * x_normalized[i-1] + phase) * np.cos(freq * np.pi * r + phase)
        
        # Enhanced gradient-dependent conditioning with exponential scaling
        grad_cond = 0.0
        for i in range(self.dim):
            grad_cond += (x_normalized[i]**2) * (1.0 + 0.2 * np.exp(np.abs(x_normalized[i])))
        
        # Chaotic interaction term with modified frequency and amplitude
        chaotic = np.sum(np.sin(25 * x_normalized) * np.cos(20 * x_normalized)) * np.exp(-r**2 * 0.5)
        
        # Additional harmonic interaction term for increased complexity
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += 0.1 * np.sin(30 * x_normalized[i]) * np.cos(10 * x_normalized[i])
        
        # Global minimum at origin with additional local optima
        return radial + 0.4 * nested + 0.15 * grad_cond + 0.08 * chaotic + 0.05 * harmonic + 1.0