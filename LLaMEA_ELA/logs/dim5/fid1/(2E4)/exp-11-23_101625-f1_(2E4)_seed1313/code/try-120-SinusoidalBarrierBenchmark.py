import numpy as np

class SinusoidalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with dynamic frequencies
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(i * 0.6 + np.sum(x) * 0.15)
            result += 2.5 * np.sin(freq * x[i])**2 + 1.8 * np.cos(freq * x[i])**2
            
        # Improved exponential barrier terms with sharper gradients
        for i in range(self.dim):
            # Create sharper exponential barriers near boundaries
            barrier = 4.0 * (np.exp(3.0 * (x[i] - 5.0)) + np.exp(-3.0 * (x[i] + 5.0)))
            result += barrier
            
        # Enhanced cross-dimensional coupling with stronger interference
        for i in range(self.dim):
            coupling = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                coupling += np.sin(x[i] * x[j]) * np.cos(0.7 * (x[i] + x[j]))
            result += 1.2 * coupling
            
        # Refined multi-scale periodic modulation with phase locking
        for i in range(self.dim):
            scale = 2**(i % 5 + 1)
            phase_shift = 0.4 * np.sin(i * 0.8 + np.sum(x) * 0.25)
            result += 1.5 * np.sin(scale * x[i] + phase_shift) * np.cos(scale * x[i] * 0.3 + phase_shift)
            
        # Strengthened saddle point structure with asymmetric components
        for i in range(self.dim):
            result += 0.7 * (x[i]**4 - 2.5 * x[i]**2) * np.sin(0.6 * np.sum(x))
            
        # Modified noise-like perturbations with spatial correlation
        noise_amp = 0.15 + 0.08 * np.sin(np.sum(x) * 0.35)
        for i in range(self.dim):
            result += noise_amp * np.sin(12.0 * x[i]) * np.cos(8.0 * x[i])
            
        # Enhanced fractal-like energy wells with more complex nested structures
        fractal = 0.0
        for i in range(self.dim):
            inner_term = np.sin(x[i] * 3.5) + 0.6 * np.sin(x[i] * 10.0)
            fractal += 2.2 * np.exp(-0.25 * (x[i] - inner_term)**2)
        result += fractal
        
        # Refined global conditioning term with more dynamic scaling
        r = np.sqrt(np.sum(x**2))
        cond_factor = 1.0 + 0.4 * np.sin(r * 0.6)
        result *= cond_factor
        
        return result