import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Exponential decay with sinusoidal modulation
        exp_decay = 1.5 * np.sum(np.exp(-0.5 * x**2) * np.sin(3.0 * x)**2)
        
        # Trigonometric wave interference with varying frequencies
        wave_interference = 1.2 * np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.sin(0.5 * x))
        
        # Adaptive ridge function with varying steepness
        ridge = 0.8 * np.sum((x[:-1] - x[1:])**2 * np.exp(-0.1 * np.abs(x[:-1] + x[1:])))
        
        # Multi-scale Gaussian peaks with varying widths
        peaks = 1.0 * np.sum(np.exp(-0.5 * (x**2 - 1.0)**2) + 0.5 * np.exp(-0.3 * (x**2 - 4.0)**2))
        
        # Sine-cosine coupled oscillators with phase shifts
        oscillators = 0.9 * np.sum(np.sin(x) * np.cos(2.0 * x) + np.cos(x) * np.sin(1.5 * x))
        
        # Polynomial coupling with exponential scaling
        coupling = 0.7 * np.sum((x**3 + 0.5 * x**5) * np.exp(-0.2 * np.abs(x)))
        
        # Hyperbolic tangent based ruggedness
        ruggedness = 0.6 * np.sum(np.tanh(x)**2 * np.sin(2.0 * x)**2)
        
        # Combined result
        result = result + exp_decay + wave_interference + ridge + peaks + oscillators + coupling + ruggedness
        
        return result