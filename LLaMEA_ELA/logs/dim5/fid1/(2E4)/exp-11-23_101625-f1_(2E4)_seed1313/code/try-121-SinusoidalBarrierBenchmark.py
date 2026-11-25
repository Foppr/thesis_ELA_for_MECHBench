import numpy as np

class SinusoidalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.1 * np.sum(x**2)
        
        # Chaotic phase couplings with logistic map modulation
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.3 + np.sum(x) * 0.15)
            phase = 0.5 * np.sin(i * 0.8 + np.sum(x) * 0.2)
            result += 2.5 * np.sin(freq * x[i] + phase)**2 + 1.8 * np.cos(freq * x[i] + phase)**2
            
        # Hyperbolic tangent exponential barriers with adaptive scaling
        for i in range(self.dim):
            barrier = 2.0 * (np.tanh(3.0 * (x[i] - 5.0)) + 1.0) + 2.0 * (np.tanh(-3.0 * (x[i] + 5.0)) + 1.0)
            result += barrier
            
        # Cross-dimensional coupling with chaotic harmonic interference
        for i in range(self.dim):
            coupling = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                coupling += np.sin(x[i] * x[j]) * np.tanh(0.3 * (x[i] + x[j]))
            result += 1.0 * coupling
            
        # Quantum-inspired energy wells with superposition states
        for i in range(self.dim):
            scale = 2**(i % 5 + 1)
            phase_shift = 0.4 * np.sin(i * 0.6 + np.sum(x) * 0.25)
            result += 1.5 * np.sin(scale * x[i] + phase_shift) * np.cos(scale * x[i] * 0.3 + phase_shift) * np.exp(-0.1 * x[i]**2)
            
        # Saddle point structure with asymmetric harmonic components and fractal modulation
        for i in range(self.dim):
            result += 0.6 * (x[i]**4 - 2.5 * x[i]**2) * np.sin(0.6 * np.sum(x)) * np.cos(0.2 * x[i])
            
        # Adaptive noise-like perturbations with chaotic scaling
        noise_amp = 0.15 + 0.08 * np.sin(np.sum(x) * 0.4)
        for i in range(self.dim):
            result += noise_amp * np.sin(12.0 * x[i]) * np.cos(9.0 * x[i])
            
        # Fractal-like energy wells with nested structures and chaotic scaling
        fractal = 0.0
        for i in range(self.dim):
            inner_term = np.tanh(x[i] * 2.5) + 0.3 * np.sin(x[i] * 7.0)
            fractal += 2.0 * np.exp(-0.15 * (x[i] - inner_term)**2) * np.cos(0.5 * x[i])
        result += fractal
        
        # Global conditioning term with dynamic scaling and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        cond_factor = 1.0 + 0.4 * np.sin(r * 0.6) * np.cos(r * 0.3)
        result *= cond_factor
        
        # Add a complex multi-scale sinusoidal component
        for i in range(self.dim):
            result += 0.8 * np.sin(5.0 * x[i] + 0.2 * np.sum(x)) * np.cos(3.0 * x[i] + 0.1 * np.sum(x))
            
        return result