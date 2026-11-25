import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimension scaling and frequency modulations
        self.fractal_dims = np.linspace(0.3, 0.8, dim)
        self.freq_mods = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure and dynamic scaling
        fractal = 0.0
        for i in range(self.dim):
            # Use fractional Brownian motion-like scaling with dynamic exponent
            scale = self.fractal_dims[i]
            # Generate fractal-like pattern using sine wave with varying frequency
            freq = 2 ** (i + 1) * self.freq_mods[i]
            fractal += np.sin(freq * x_norm[i]) * (np.abs(x_norm[i]) ** scale)
        
        # Dynamic frequency modulation component with time-varying parameters
        mod_freq = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Hybrid gradient-flow chaos with adaptive damping
        grad_flow = 0.0
        for i in range(self.dim):
            # Simulate gradient descent with chaotic perturbations
            dx = np.sin(x_norm[i]) + 0.1 * np.cos(10 * x_norm[i])
            grad_flow += dx ** 2
        
        # Multi-scale sinusoidal coupling with phase-shifted harmonics
        coupling = 0.0
        for i in range(self.dim):
            # Combine multiple harmonic frequencies with varying amplitudes
            coupling += (np.sin(2 * np.pi * x_norm[i]) + 
                        0.5 * np.sin(4 * np.pi * x_norm[i]) + 
                        0.3 * np.sin(8 * np.pi * x_norm[i]))
        
        # Polynomial chaos with higher-order terms and cross-terms
        poly = np.sum(x_norm**6 + 0.7 * x_norm**5 + 0.4 * x_norm**4 + 0.2 * x_norm**3 + 0.1 * x_norm**2)
        
        # Cross-dimensional interaction with exponential decay and oscillatory terms
        cross_term = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(10 * x_norm) * np.sin(5 * x_norm))
        
        # Combine all components with optimized weights for complex landscape
        return 0.3 * fractal + 0.25 * mod_freq + 0.2 * grad_flow + 0.15 * coupling + 0.08 * poly + 0.02 * cross_term + 3.0