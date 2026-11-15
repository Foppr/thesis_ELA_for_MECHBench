import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple Gaussian peaks
        radial = 0.0
        for i in range(self.dim):
            radial += np.exp(-0.5 * (x_norm[i] - 0.3)**2) + np.exp(-0.5 * (x_norm[i] + 0.3)**2)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sine_wave = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)
            amp = 1.0 + 0.5 * np.sin(i * np.pi / 4)
            sine_wave += amp * np.sin(freq * x_norm[i] * np.pi)
        
        # Cross-dimensional coupling with radial basis functions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.1)
                cross_coupling += np.exp(-dist**2) * np.sin(2 * x_norm[i] * x_norm[j])
        
        # Adaptive conditioning component
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.5 * i * np.pi)
            conditioning += cond_factor * x_norm[i]**4
        
        # Chaotic modulation using logistic map
        chaotic_mod = 0.0
        for i in range(self.dim):
            logistic_input = 3.9 * (x_norm[i] % 1.0)
            chaotic_mod += np.sin(logistic_input * 8 * np.pi) * np.cos(x_norm[i] * 3 * np.pi)
        
        # Polynomial interaction with exponential decay
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Trigonometric coupling with varying phase shifts
        trig_coupling = 0.0
        for i in range(self.dim):
            phase = 0.25 * i * np.pi
            trig_coupling += np.sin(x_norm[i] * np.pi + phase) * np.cos(x_norm[i] * 2 * np.pi + phase)
        
        # Combined fitness function with adaptive weights
        return 0.3 * radial + 0.25 * sine_wave + 0.2 * cross_coupling + 0.15 * conditioning + 0.05 * chaotic_mod + 0.03 * poly_interaction + 0.02 * trig_coupling