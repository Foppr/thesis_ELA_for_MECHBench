import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum perturbed with chaotic sequence
        self.global_min = np.array([2.5 * np.sin(i * np.pi / 3) for i in range(dim)])
    
    def f(self, x):
        # Clamp input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with dynamic scaling and chaotic modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(0.5 * x) + 0.1 * np.cos(0.3 * x)))
        
        # Sinusoidal interference with dynamic frequency and phase
        f2 = np.sum(np.sin(3.0 * x + np.cos(x)) * np.cos(2.0 * x + np.sin(x)) * (1 + 0.15 * np.sin(x**2)))
        
        # Polynomial coupling with chaotic interaction weights
        f3 = np.sum(x**4 - 10 * x**2 + 5 * x + 0.02 * np.sum(x**5 * np.cos(x)))
        
        # Exponential barrier with logarithmic scaling and chaotic perturbation
        f4 = np.sum(np.exp(0.2 * np.abs(x)) - 1 - 0.15 * np.log(1 + np.abs(x)) + 0.08 * np.cos(x**2))
        
        # Chaotic fractal component with nested sine-cosine structure
        f5 = np.sum(np.sin(np.cos(x)) + np.cos(np.sin(x)) + 0.04 * np.sin(x) * np.cos(x))
        
        # Cross-dimensional coupling with adaptive phase shifts
        f6 = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.exp(-0.05 * np.abs(x[:-1] - x[1:])) * (1 + 0.03 * np.cos(x[:-1] * x[1:])))
        
        # Fractal-like component with exponential decay and chaotic modulation
        fractal = np.sum(np.sin(2**np.arange(1, self.dim+1) * x) * (1 / (2**(np.arange(1, self.dim+1) * (1 + 0.1 * np.cos(x)))))
        
        # Nested chaotic coupling with dynamic modulation and fractional scaling
        nested_coupling = np.sum(np.sin(np.sin(x) * np.cos(x)) * np.cos(np.cos(x) * np.sin(x)) * (1 + 0.04 * np.sin(x)) * np.cos(0.4 * x))
        
        # Adaptive fractal modulation with time-varying scaling factors
        adaptive_fractal = np.sum(np.sin(np.power(3, np.arange(1, self.dim+1)) * x) * (1 / np.power(3, np.arange(1, self.dim+1) * (1 + 0.08 * np.cos(x)))))
        
        # Combine all components with varying weights and chaotic scaling
        return 0.12 * f1 + 0.18 * f2 + 0.16 * f3 + 0.14 * f4 + 0.10 * f5 + 0.09 * f6 + 0.08 * fractal + 0.06 * nested_coupling + 0.07 * adaptive_fractal