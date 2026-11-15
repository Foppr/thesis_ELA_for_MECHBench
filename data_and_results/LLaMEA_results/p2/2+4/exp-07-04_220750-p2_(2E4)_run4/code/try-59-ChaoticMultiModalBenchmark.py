import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base radial component with chaotic polynomial growth
        r = np.sqrt(np.sum(x_norm**2))
        radial = r**4 + 0.3 * r**7 + 0.05 * np.sin(15 * r * np.pi) + 0.2 * np.cos(8 * r * np.pi)
        
        # Nested harmonic oscillations with varying frequencies and amplitudes
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 0.5 + 0.3 * np.sin(i * np.pi / 4)
            harmonic_sum += amp * np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi / 2)
        
        # Exponential decay barriers with random shifts
        barrier_term = 0.0
        for i in range(self.dim):
            shift = 0.5 * np.sin(i * np.pi / 3)
            barrier_term += np.exp(-5 * (x_norm[i] - shift)**2) + np.exp(-3 * (x_norm[i] + shift)**2)
        
        # Asymmetric cross-dimensional coupling with chaotic phase modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(i * j * np.pi / 4)
                coupling = (x_norm[i]**2 + x_norm[j]**2) * np.sin(4 * x_norm[i] * x_norm[j] * np.pi + phase)
                cross_coupling += coupling * np.exp(-0.1 * (i - j)**2)
        
        # Multi-scale chaotic modulation with fractal-like behavior
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(10 * x_norm[i] * np.pi + np.sin(5 * x_norm[i] * np.pi)) * np.cos(7 * x_norm[i] * np.pi)
        
        # Final fitness combining all components with adaptive weights
        return radial + 0.3 * harmonic_sum + 0.2 * barrier_term + 0.15 * cross_coupling + 0.05 * chaotic_mod