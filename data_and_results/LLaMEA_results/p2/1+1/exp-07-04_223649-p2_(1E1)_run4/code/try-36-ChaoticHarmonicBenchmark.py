import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for added complexity
        self.chaotic_sequence = np.array([np.sin(2 ** i * np.pi / 100) for i in range(dim)])
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        base = np.sum(x ** 2)
        
        # Chaotic sine-cosine interaction terms
        chaotic = 0.5 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(self.chaotic_sequence * x))
        
        # Harmonic polynomial coupling with dynamic frequencies
        harmonic = 0.3 * np.sum(np.sin(3.0 * x) + np.cos(2.0 * x) + 0.5 * np.sin(5.0 * x) ** 2)
        
        # Non-separable interaction using exponential decay
        sep_interaction = 0.4 * np.sum(np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * (x[:-1] + x[1:]) ** 2)
        
        # Multi-modal peaks with dynamic centers and amplitudes
        peaks = 0.6 * np.sum(np.exp(-0.5 * (x - np.sin(x)) ** 2) * np.cos(2.0 * x) ** 2)
        
        # Saddle point perturbation using hyperbolic functions
        saddle = 0.2 * np.sum(np.tanh(x) * np.sinh(x) * np.cos(x))
        
        # Dynamic coupling with time-varying weights
        dynamic_coupling = 0.3 * np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)))
        
        # Combine all components
        result = base + chaotic + harmonic + sep_interaction + peaks + saddle + dynamic_coupling
        
        return result