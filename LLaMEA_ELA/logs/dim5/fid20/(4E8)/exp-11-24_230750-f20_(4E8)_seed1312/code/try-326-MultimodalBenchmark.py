import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable polynomial valley component with varying exponents
        valleys = 0.0
        for i in range(self.dim):
            exp_factor = 2 + 2 * np.sin(0.5 * x[i])
            valleys += (x[i]**exp_factor) / (1.0 + 0.1 * np.abs(x[i]))
        
        # Periodic modulation with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.cos(0.3 * x[i])
            amp = 1.0 + 0.8 * np.sin(0.4 * x[i]**2)
            periodic += amp * np.sin(freq * x[i] + 0.5 * np.cos(2.0 * x[i]))
        
        # Cross-dimensional interference with sinusoidal coupling
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                interference += coupling
        
        # Multi-scale chaotic component with logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            r = 3.8 + 0.2 * np.sin(0.6 * x[i])
            chaotic += r * x[i] * (1 - x[i]) * np.sin(3.0 * x[i])
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return (0.3 * valleys + 0.3 * periodic + 0.2 * interference + 0.2 * chaotic) * scale_factor