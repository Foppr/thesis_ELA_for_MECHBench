import numpy as np

class PeriodicMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal periodic components with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            periodic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Exponential decay interactions between dimensions
        decay_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                decay_interaction += np.exp(-dist * 0.5) * np.sin(dist * 2.0)
        
        # Adaptive conditioning based on dimension index
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.3 * i + 1.0)
            conditioning += cond_factor * x[i]**4
        
        # Multi-scale harmonic potentials with phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            phase_shift = 0.2 * np.sin(0.4 * i + 0.5)
            harmonic += (x[i]**2) * np.cos(x[i] + phase_shift) * np.exp(-0.1 * x[i]**2)
        
        # Combined result with dynamic weighting
        result = 0.3 * periodic + 0.4 * decay_interaction + 0.2 * conditioning + 0.1 * harmonic
        
        # Add a global scaling factor that depends on the number of dimensions
        scaling = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return result * scaling