import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(2 * np.pi * x * np.exp(-0.1 * x**2)) * np.cos(3 * np.pi * x * np.exp(-0.05 * x**2)))
        
        # Polynomial interaction terms with mixed coupling
        poly_interaction = np.sum(0.5 * x**8 - 6.0 * x**6 + 15.0 * x**4 - 12.0 * x**2 + 2.0)
        
        # Cross-dimensional coupling with phase-shifted interactions
        cross_coupling = np.sum(np.sin(4 * np.pi * (x[:-1] + 0.5 * x[1:])) * np.cos(2 * np.pi * (x[:-1] - 0.3 * x[1:])))
        
        # Resonance-based correlation terms with dynamic phase shifts
        resonance = np.sum(np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x) * np.sin(2 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Asymmetric polynomial with mixed nonlinearities
        asym_poly = np.sum(0.2 * x**10 - 3.0 * x**8 + 8.0 * x**6 - 8.0 * x**4 + 3.0 * x**2 - 0.5 * x)
        
        # Combine all terms with optimized weights
        return 0.3 * chaotic_wave + 0.15 * poly_interaction + 0.2 * cross_coupling + 0.1 * resonance + 0.25 * asym_poly + 1.5