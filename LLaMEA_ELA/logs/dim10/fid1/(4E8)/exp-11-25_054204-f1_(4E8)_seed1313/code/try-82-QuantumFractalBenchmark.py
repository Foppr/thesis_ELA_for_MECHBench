import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum harmonic oscillator frequencies
        self.frequencies = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic potential component
        f1 = 0.5 * np.sum(self.frequencies * x**2)
        
        # Fractal-like self-similarity pattern with multiple scales
        f2 = 0.0
        for i in range(1, 6):
            scale = 2**i
            f2 += 0.3 / scale * np.sum(np.sin(scale * x) * np.cos(scale * x))
        
        # Adaptive noise injection based on gradient magnitude
        grad_magnitude = np.sqrt(np.sum(np.gradient(x)**2))
        noise_amp = 0.1 * (1.0 + 0.5 * np.tanh(grad_magnitude))
        f3 = noise_amp * np.sum(np.random.normal(0, 1, self.dim) * x)
        
        # Cross-dimensional coupling with quantum entanglement-inspired terms
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += 0.25 * (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Multi-scale periodic modulation with varying amplitudes
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.4 * np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
        
        # Exponential decay with fractal dimension scaling
        f6 = 0.15 * np.sum(np.exp(-0.5 * x**2) * np.sin(x))
        
        # Sigmoidal basin structure with multiple local minima
        f7 = 0.0
        for i in range(self.dim):
            f7 += 1.0 / (1.0 + np.exp(-x[i])) * np.cos(2.0 * x[i])
        
        # Coupled harmonic oscillators with time-delayed feedback
        f8 = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                f8 += 0.3 * (x[i] - x[i+1])**2 * np.sin(0.5 * (x[i] + x[i+1]))
        
        # Fractional power scaling with non-integer exponents
        f9 = 0.2 * np.sum(np.abs(x)**1.7)
        
        # Complex amplitude modulation with phase coupling
        f10 = 0.25 * np.sum(np.sin(x) * np.cos(2.0 * x) + np.cos(x) * np.sin(2.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10