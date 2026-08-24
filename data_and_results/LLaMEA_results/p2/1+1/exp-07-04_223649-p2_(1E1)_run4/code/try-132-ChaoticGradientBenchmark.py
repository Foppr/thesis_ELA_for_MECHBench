import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for dynamic phase shifts
        self.phases = np.linspace(0, 2 * np.pi, dim, endpoint=False)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with quadratic and logarithmic terms
        r = np.sqrt(np.sum(x**2))
        radial = 0.5 * r**2 + 0.1 * np.log(1.0 + r**2)
        
        # Dynamic phase-shifted sine-cosine interactions
        phase_shifted = np.sum(np.sin(self.phases + x) * np.cos(self.phases - x))
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.sum(np.sin(10.0 * np.tanh(x)) * np.cos(5.0 * np.exp(-x**2)))
        
        # Adaptive noise term that scales with dimensionality
        noise = 0.05 * np.sum(np.random.randn(self.dim) * (1.0 + 0.1 * np.abs(x)))
        
        # Multi-scale radial peaks with varying amplitudes
        peaks = 0.0
        for i in range(1, 6):
            peaks += i * np.exp(-0.5 * ((r - i) / (0.5 * i))**2) * np.cos(i * r)
        
        # Gradient-based curvature modulation
        grad_mod = np.sum((x**2 + 1.0)**(-1.5) * np.sin(x))
        
        # Combine all components
        result = radial + phase_shifted + chaotic + noise + peaks + grad_mod
        
        return result