import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.scale_factor = 1.0
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Fractal-like recursive sine-cosine interactions
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            if i < self.dim:
                fractal += np.sum(np.sin(2**i * x[:-i]) * np.cos(2**i * x[i:]) * np.sin(0.5 * x[:-i] + 0.3 * x[i:]))
        
        # Dynamic phase-shifted chaotic components
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x[i] + self.phase_shifts[i]) * np.cos(x[i] * np.exp(-0.1 * x[i]**2))
        
        # Multi-scale interference pattern with varying amplitudes
        interference = 0.0
        for scale in [0.5, 1.0, 2.0, 4.0]:
            interference += scale * np.sum(np.sin(scale * x) * np.cos(scale * x * 0.7) * np.exp(-0.05 * x**2))
        
        # Self-similar cubic coupling with recursive structure
        cubic_coupling = 0.0
        for i in range(1, min(4, self.dim)):
            if i < self.dim:
                cubic_coupling += np.sum((x[:-i]**3 - x[i:]**3) * np.sin(x[:-i] * x[i:]))
        
        # Asymmetric exponential decay with oscillatory modulation
        exponential = 0.0
        for i in range(self.dim):
            exponential += np.exp(-0.1 * np.abs(x[i])) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Multi-modal peak with varying heights and widths
        peaks = 0.0
        for i in range(self.dim):
            peaks += 2.0 * np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2)) * np.sin(0.5 * x[i])**2
        
        # Combined result
        result = result + 0.5 * fractal + 0.3 * chaotic + 0.4 * interference + 0.2 * cubic_coupling + 0.3 * exponential + 0.25 * peaks
        
        return result