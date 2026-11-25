import numpy as np

class ChaoticOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute phase shifts and frequencies for dynamic oscillation
        self.phases = np.linspace(0, 2*np.pi, min(dim, 10), endpoint=False)
        self.frequencies = np.logspace(0.5, 2.0, min(dim, 10))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Chaotic oscillator component with dynamic phase shifts and varying frequencies
        oscillator = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            phase = self.phases[i % len(self.phases)]
            oscillator += np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase) * np.exp(-0.1 * np.abs(x[i]))
        
        # Non-separable high-order interaction terms
        high_order = 0.0
        for i in range(self.dim - 1):
            high_order += (x[i]**4 + x[i+1]**4) * np.sin(2.5 * (x[i] + x[i+1])) * np.exp(-0.2 * (x[i] - x[i+1])**2)
        
        # Exponentially decaying coupling between dimensions
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += np.exp(-0.3 * i) * np.sin(3.0 * x[i]) * np.cos(4.0 * x[i+1]) * np.sin(2.5 * x[i+2])
        
        # Multi-scale chaotic modulation with adaptive amplitude
        modulated = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(5.0 * x[i])
            modulated += amp * np.sin(7.0 * x[i]) * np.cos(6.0 * x[i]**2) * np.exp(-0.15 * x[i]**2)
        
        # Asymmetric oscillatory field with piecewise nonlinearity
        asymmetric = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asymmetric += np.sin(9.0 * x[i]) * np.exp(-0.5 * x[i]**2)
            else:
                asymmetric += np.cos(8.0 * x[i]) * np.exp(-0.4 * x[i]**2)
        
        # Combined chaotic landscape with weighted components
        return base + 1.8 * oscillator + 1.2 * high_order + 0.9 * coupling + 0.7 * modulated + 0.6 * asymmetric