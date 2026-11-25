import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic basin
        f1 = 0.1 * np.sum(x**2)
        
        # Multiple sinusoidal wells with adaptive frequencies and exponential decay
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 4.0 * np.sin(0.3 * i)  # Adaptive frequency
            decay = np.exp(-0.2 * np.abs(x[i]))  # Exponential decay
            f2 += decay * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Overlapping periodic modulations with varying amplitudes and phases
        f3 = 0.0
        for i in range(self.dim):
            amp = 0.7 + 0.3 * np.cos(0.4 * i)  # Varying amplitude
            phase = 0.2 * np.sin(0.5 * i)  # Phase shift
            f3 += amp * np.sin(5.0 * x[i] + phase) * np.cos(3.0 * x[i])
        
        # Add a strong cubic term to increase landscape complexity
        f4 = 0.02 * np.sum(x**3)
        
        # Add a global scaling factor with enhanced fractal-like behavior
        f5 = 0.1 * np.sum(np.sin(0.7 * x) * np.cos(0.3 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Add chaotic modulation with modified adaptive scaling factor
        scale_factor = 1.0 + 0.8 * np.sin(np.sum(x**2) / (self.dim * 20.0)) * np.cos(np.sum(x) / self.dim)
        f6 = scale_factor * np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Introduce chaotic sinusoidal perturbations
        f7 = 0.05 * np.sum(np.sin(10.0 * np.sin(x)) * np.cos(7.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7