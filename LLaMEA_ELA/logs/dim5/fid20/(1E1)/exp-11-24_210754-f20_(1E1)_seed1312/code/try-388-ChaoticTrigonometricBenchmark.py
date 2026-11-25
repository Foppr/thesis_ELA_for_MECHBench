import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Nested trigonometric terms with chaotic phase interactions
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive frequency based on dimension index and chaotic modulation
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.4))
            # Chaotic phase modulation using sine-cosine composition
            phase = np.sin(freq * xi) * np.cos(freq * xi**1.5)
            f2 += phase**2
        
        # Multi-scale sinusoidal interference with varying amplitudes
        f3 = 0.3 * np.sum(np.sin(15.0 * x) * np.cos(10.0 * x) * np.sin(5.0 * x))
        
        # Asymmetric polynomial corruption with mixed powers
        f4 = 0.05 * np.sum((x**6.2 + 0.7 * x**3.8 + 0.4 * x**1.9) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f5 = 0.2 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(8.0 * x) * np.cos(4.0 * x))
        
        # Fractal-like recursive interaction terms with varying coupling strengths
        f6 = 0.15 * np.sum(np.sin(30.0 * np.sin(5.0 * x)) * np.cos(20.0 * np.cos(3.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and dynamic weights
        f7 = 0.08 * np.sum(np.sin(0.8 * x[:-1] + 1.2 * x[1:]) * np.cos(1.5 * x[:-1] - 0.7 * x[1:]))
        
        # Fractional Brownian motion-like roughness with varying Hurst parameter effects
        f8 = 0.1 * np.sum(np.abs(x)**1.4 * np.sin(25.0 * x))
        
        # Asymmetric multimodal structure with varying curvature and enhanced nonlinearity
        f9 = 0.18 * np.sum((x**4.1 + 0.5 * x**3.2 - 0.3 * x**1.7) * np.exp(-0.15 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9