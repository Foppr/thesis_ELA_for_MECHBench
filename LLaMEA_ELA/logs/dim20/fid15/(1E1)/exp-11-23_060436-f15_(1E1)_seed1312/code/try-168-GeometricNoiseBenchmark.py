import numpy as np

class GeometricNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Geometric periodic components with varying frequencies and amplitudes
        periodic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.3 * np.cos(i * 0.4)
            periodic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive noise injection with dimension-dependent intensity
        noise = 0
        for i in range(self.dim):
            noise_intensity = 0.1 + 0.2 * np.sin(0.5 * i) * np.cos(0.3 * i)
            noise += noise_intensity * np.random.normal(0, 1) * np.exp(-0.5 * x[i]**2)
        
        # Constrained interaction terms based on geometric distances
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                interaction += np.sin(dist) * np.exp(-0.1 * dist**2)
        
        # Dynamic conditioning with chaotic modulation
        conditioning = 0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.4 * i) * np.cos(0.3 * x[i])
            conditioning += cond_factor * x[i]**2
        
        # Multi-scale fractal-like structure with recursive patterns
        fractal = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.2 * i)
            fractal += np.sin(scale * x[i]) * np.cos(scale * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Basin structure with varying depths and locations
        basins = 0
        for i in range(self.dim):
            basin_loc = 1.5 * np.sin(0.3 * i) * (1.0 + 0.2 * np.cos(i * 0.2))
            basin_depth = 0.8 + 0.4 * np.sin(0.4 * i)
            basins += basin_depth * np.exp(-0.3 * (x[i] - basin_loc)**2)
        
        # Asymmetric oscillatory component with chaotic phase shifts
        asym_osc = 0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.5 * i) * np.cos(0.2 * x[i])
            asym_osc += np.sin(x[i] + phase_shift) * np.exp(-0.1 * (x[i] - 1.0)**2)
        
        # Combined fitness with optimized weights
        return (quadratic * 0.6 +
                periodic * 0.4 +
                noise * 0.3 +
                interaction * 0.25 +
                conditioning * 0.35 +
                fractal * 0.2 +
                basins * 0.3 +
                asym_osc * 0.2)