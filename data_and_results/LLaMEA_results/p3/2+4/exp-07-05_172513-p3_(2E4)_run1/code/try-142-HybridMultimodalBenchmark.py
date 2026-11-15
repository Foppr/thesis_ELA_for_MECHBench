import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for efficiency
        self.constants = np.arange(1, dim + 1) * np.pi / dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian radial basis components with varying centers and variances
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(self.constants[i])
            variance = 0.1 + 0.2 * np.cos(self.constants[i])
            gaussian += np.exp(-0.5 * ((x_scaled[i] - center) / variance)**2)
        
        # Trigonometric oscillation components with varying frequencies and amplitudes
        trig = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(self.constants[i])
            amp = 1.0 + 0.5 * np.cos(self.constants[i])
            trig += amp * np.sin(freq * x_scaled[i])
        
        # Cross-dimensional interaction terms with exponential decay
        cross = 0.0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                cross += np.exp(-0.1 * (x_scaled[i]**2 + x_scaled[j]**2)) * np.sin(5 * (x_scaled[i] - x_scaled[j]))
        
        # Non-separable cubic polynomial terms
        cubic = np.sum(x_scaled**3 * np.sin(3 * x_scaled))
        
        # Sine-modulated quadratic terms for additional complexity
        sine_quad = np.sum(np.sin(2 * x_scaled)**2 * x_scaled**2)
        
        # Combine all components with carefully tuned weights
        return 2.0 * gaussian + 1.5 * trig + 0.8 * cross + 0.5 * cubic + 0.3 * sine_quad