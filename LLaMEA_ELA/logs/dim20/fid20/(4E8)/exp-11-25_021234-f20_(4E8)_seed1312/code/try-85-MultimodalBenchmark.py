import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic basin
        f1 = 0.1 * np.sum(x**2)
        
        # Multiple sinusoidal wells with adaptive frequencies and logarithmic barriers
        f2 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 5.0 * np.sin(0.4 * i)  # Enhanced frequency modulation
            barrier = np.log(1.0 + 0.5 * np.abs(x[i]))  # Logarithmic barrier
            f2 += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2) * barrier
        
        # Overlapping periodic modulations with varying amplitudes, phases, and saddle points
        f3 = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.4 * np.cos(0.5 * i)  # Varying amplitude
            phase = 0.3 * np.sin(0.6 * i)  # Phase shift
            saddle = np.sin(2.0 * x[i]) * np.cos(2.0 * x[i])  # Saddle point structure
            f3 += amp * np.sin(6.0 * x[i] + phase) * np.cos(4.0 * x[i]) * (1.0 + 0.2 * saddle)
        
        # Add a strong cubic term with chaotic scaling
        f4 = 0.03 * np.sum(x**3)
        
        # Add a global scaling factor with enhanced fractal-like behavior and chaotic modulation
        f5 = 0.15 * np.sum(np.sin(0.8 * x) * np.cos(0.4 * x) * np.exp(-0.03 * np.sum(x**2)))
        
        # Add chaotic modulation with modified adaptive scaling factor and multi-scale interactions
        scale_factor = 1.2 + 0.6 * np.sin(np.sum(x**2) / (self.dim * 15.0)) * np.cos(np.sum(x) / self.dim)
        f6 = scale_factor * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Introduce chaotic sinusoidal perturbations with multi-scale frequency components
        f7 = 0.08 * np.sum(np.sin(12.0 * np.sin(x)) * np.cos(9.0 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Add a complex interaction term between dimensions to increase non-separability
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(2.0 * (x[i] + x[j])) * np.cos(3.0 * (x[i] - x[j]))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + 0.02 * interaction