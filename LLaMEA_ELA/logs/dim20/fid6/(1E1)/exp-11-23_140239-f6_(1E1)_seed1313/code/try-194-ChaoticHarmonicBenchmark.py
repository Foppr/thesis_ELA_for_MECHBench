import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add exponentially decaying harmonic waves with adaptive frequencies
        for i in range(1, min(self.dim + 1, 25)):
            freq = i * 0.5 * np.exp(-i * 0.1)
            amp = 10.0 * np.exp(-i * 0.2)
            result += amp * np.sin(freq * x[i-1]) * np.cos(freq * x[i-1]**2)
        
        # Add cross-dimensional coupling with chaotic modulation
        for i in range(self.dim - 1):
            coupling = np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
            result += 5.0 * coupling * np.exp(-abs(x[i] - x[i+1]))
        
        # Add adaptive basin splitting with fractal-like scaling
        basin_split = 0.0
        for i in range(self.dim):
            basin_split += 3.0 * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2))
        result += basin_split * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Add multi-scale sinusoidal noise with varying amplitudes
        noise = 0.0
        for i in range(1, min(self.dim + 1, 30)):
            noise += 2.0 * np.sin(i * x[i-1] * 10) * np.cos(i * x[i-1] * 7)
        result += noise / self.dim
        
        # Add exponential decay term for increased ruggedness
        exp_decay = np.sum(np.exp(-np.abs(x)) * np.sin(x))
        result += 2.5 * exp_decay
        
        return result