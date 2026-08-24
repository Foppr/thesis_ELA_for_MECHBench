import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.global_min = np.array([2.5 * np.sin(i * 0.4 + self.t) for i in range(dim)])
        self.noise_scale = 0.05
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial coupling with dynamic exponents
        exponents = 2 + 2 * np.sin(self.t + np.arange(self.dim))
        f1 = np.sum(((x - self.global_min)**exponents) * np.log(1.0 + np.abs(x - self.global_min)))
        
        # Multi-scale exponential barrier terms with chaotic modulation
        f2 = np.sum(np.exp(-0.3 * (x - self.global_min)**2) * np.cos(3.0 * x + np.sin(self.t)))
        
        # Complex trigonometric interference with time-varying frequencies
        freqs = 2.0 + np.sin(self.t + np.arange(self.dim)) * 1.5
        f3 = np.sum(np.sin(freqs * x + np.cos(freqs * self.t)) * np.exp(-0.2 * np.abs(x)))
        
        # Adaptive noise with dynamic scaling factor
        self.noise_scale = 0.05 + 0.02 * np.sin(self.t * 0.5)
        noise = np.random.normal(0, self.noise_scale, self.dim)
        f4 = np.sum((x - self.global_min + noise)**2 * np.tanh(x))
        
        # Hyperbolic and logarithmic coupling with chaotic weights
        weights = 1.0 + 0.5 * np.sin(self.t + np.arange(self.dim))
        f5 = np.sum(weights * np.tanh(x) * np.log(1.0 + np.abs(x)) * np.cos(x))
        
        # Additional chaotic sinusoidal coupling between dimensions
        coupling = np.sum(np.sin(x[:-1] - x[1:]) * np.cos(self.t + np.arange(self.dim-1)))
        
        # Combine all components with optimized weights
        self.t += 0.02
        self.global_min = np.array([2.5 * np.sin(i * 0.4 + self.t) for i in range(self.dim)])
        
        return 0.25 * f1 + 0.2 * f2 + 0.25 * f3 + 0.2 * f4 + 0.1 * f5 + 0.05 * coupling