import numpy as np

class PeriodicMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal periodic components with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(0.6 * i)
            periodic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Exponential decay interactions between dimensions (modified decay rate)
        decay_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                decay_interaction += np.exp(-dist * 0.3) * np.sin(dist * 1.5)
        
        # Adaptive conditioning based on dimension index (modified factor)
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.7 * np.sin(0.4 * i + 1.5)
            conditioning += cond_factor * x[i]**4
        
        # Multi-scale harmonic potentials with phase shifts (modified coefficients)
        harmonic = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.5 * i + 0.7)
            harmonic += (x[i]**2) * np.cos(x[i] + phase_shift) * np.exp(-0.15 * x[i]**2)
        
        # Combined result with dynamic weighting
        result = 0.25 * periodic + 0.45 * decay_interaction + 0.25 * conditioning + 0.05 * harmonic
        
        # Add a global scaling factor that depends on the number of dimensions (modified)
        scaling = 1.0 + 0.15 * np.log(self.dim + 1)
        
        return result * scaling