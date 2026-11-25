import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-like interference patterns with phase modulation
        quantum_terms = np.sum(np.sin(3 * np.pi * x + np.sin(2 * x)) * np.cos(5 * np.pi * x + np.cos(1.5 * x)))
        
        # Saddle-point attractors with dynamic positioning
        saddle_terms = 0.0
        for i in range(min(4, self.dim)):
            saddle_center = 2.5 * np.sin(i * np.pi / 3)
            saddle_width = 0.5 + 0.3 * np.cos(i * 0.7)
            saddle_terms += (x[i] - saddle_center)**2 * np.exp(-0.5 * ((x[i] - saddle_center) / saddle_width)**2)
        
        # Adaptive penalty landscapes with dimensionality-dependent scaling
        penalty = 0.0
        for i in range(self.dim):
            penalty += 10 * (1 + 0.5 * np.sin(i * 0.3)) * np.exp(-0.1 * np.abs(x[i]))
        
        # Rugged terrain with fractal-like characteristics and multi-scale peaks
        rugged = 0.0
        for i in range(min(6, self.dim)):
            scale = 2**(i % 3)
            rugged += scale * np.sin(scale * x[i]) * np.cos(scale * x[i] / 2)
        
        # Enhanced cross-term interactions with non-linear coupling and memory effects
        cross_terms = 0.0
        for i in range(self.dim - 1):
            cross_terms += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1]) * np.exp(-0.1 * np.abs(x[i] - x[i+1]))
        
        # Novel hyperbolic tangent coupling mechanisms for sharp transitions
        tanh_coupling = 0.0
        for i in range(min(5, self.dim)):
            tanh_coupling += np.tanh(3 * x[i]) * np.sin(2 * x[i]) * np.cos(x[i]**2)
        
        # Multi-scale harmonic components with varying frequencies and amplitudes
        harmonic = 0.0
        for i in range(min(8, self.dim)):
            freq = 1 + 0.5 * np.sin(i * 0.4)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3)
        
        # Fractional Brownian motion component with varying Hurst parameter
        fbm = 0.0
        hurst = 0.2 + 0.6 * np.sin(self.dim * 0.15)
        for i in range(1, min(7, self.dim)):
            fbm += (x[i] - x[i-1])**2 * np.sin(i * hurst * np.pi / 3)
        
        # Add noise term with directional bias and temporal correlation
        noise = 0.1 * np.random.rand() * np.sum(np.sin(15 * x) * np.cos(10 * x))
        
        # Combined function value
        return quantum_terms + saddle_terms + penalty + rugged + cross_terms + tanh_coupling + harmonic + fbm + noise