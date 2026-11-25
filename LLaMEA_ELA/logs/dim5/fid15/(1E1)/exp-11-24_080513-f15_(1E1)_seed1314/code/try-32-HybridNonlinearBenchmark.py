import numpy as np

class HybridNonlinearBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Spherical component with variable radius
        sphere = np.sum(x_normalized**2)
        
        # Exponential decay terms with random offsets
        exp_decay = 0.0
        for i in range(self.dim):
            offset = 0.3 * np.sin(i * 0.7)
            exp_decay += np.exp(-5.0 * (x_normalized[i] - offset)**2)
        
        # Trigonometric wave interference with varying frequencies and amplitudes
        waves = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.5)
            amp = 0.5 + 0.5 * np.cos(i * 0.3)
            waves += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Cross-dimensional coupling with exponential interaction
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.exp(-2.0 * (x_normalized[i] - x_normalized[j])**2)
                cross += coupling * (x_normalized[i]**2 + x_normalized[j]**2)
        
        # Polynomial distortion with mixed degrees
        poly_distort = 0.0
        for i in range(self.dim):
            poly_distort += x_normalized[i]**3 + 0.5 * x_normalized[i]**4
        
        # Add a global sinusoidal modulation
        modulation = np.sin(2.0 * np.sum(x_normalized))
        
        # Combine all components with carefully tuned weights
        return 0.3 * sphere + 0.25 * exp_decay + 0.2 * waves + 0.15 * cross + 0.08 * poly_distort + 0.02 * modulation