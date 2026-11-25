import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic basin
        f1 = 0.1 * np.sum(x**2)
        
        # Multiple sinusoidal wells with adaptive frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)  # Adaptive frequency
            f2 += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Overlapping periodic modulations with varying amplitudes
        f3 = 0.0
        for i in range(self.dim):
            amp = 0.5 + 0.5 * np.cos(0.3 * i)  # Varying amplitude
            f3 += amp * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Add a small cubic term to increase landscape complexity
        f4 = 0.01 * np.sum(x**3)
        
        # Add a global scaling factor to make the function more challenging
        f5 = 0.05 * np.sum(np.sin(0.5 * x) * np.cos(0.2 * x))
        
        return f1 + f2 + f3 + f4 + f5