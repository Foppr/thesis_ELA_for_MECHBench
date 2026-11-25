import numpy as np

class SinusoidalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Periodic sinusoidal components with varying frequencies
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5 + np.sum(x) * 0.1)
            result += 2.0 * np.sin(freq * x[i])**2 + 1.5 * np.cos(freq * x[i])**2
            
        # Exponential barrier terms with position-dependent scaling
        for i in range(self.dim):
            # Create exponential barriers near boundaries
            barrier = 3.0 * (np.exp(2.0 * (x[i] - 5.0)) + np.exp(-2.0 * (x[i] + 5.0)))
            result += barrier
            
        # Cross-dimensional coupling with harmonic interference
        for i in range(self.dim):
            coupling = 0.0
            for j in range(i+1, min(i+3, self.dim)):
                coupling += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
            result += 0.8 * coupling
            
        # Multi-scale periodic modulation with dynamic phase shifts
        for i in range(self.dim):
            scale = 2**(i % 4 + 1)
            phase_shift = 0.3 * np.sin(i * 0.7 + np.sum(x) * 0.2)
            result += 1.2 * np.sin(scale * x[i] + phase_shift) * np.cos(scale * x[i] * 0.4 + phase_shift)
            
        # Saddle point structure with asymmetric harmonic components
        for i in range(self.dim):
            result += 0.5 * (x[i]**4 - 2.0 * x[i]**2) * np.sin(0.5 * np.sum(x))
            
        # Adaptive noise-like perturbations
        noise_amp = 0.1 + 0.05 * np.sin(np.sum(x) * 0.3)
        for i in range(self.dim):
            result += noise_amp * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        # Fractal-like energy wells with nested structures
        fractal = 0.0
        for i in range(self.dim):
            inner_term = np.sin(x[i] * 3.0) + 0.5 * np.sin(x[i] * 9.0)
            fractal += 1.8 * np.exp(-0.2 * (x[i] - inner_term)**2)
        result += fractal
        
        # Global conditioning term with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        cond_factor = 1.0 + 0.3 * np.sin(r * 0.5)
        result *= cond_factor
        
        return result