import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced chaotic interactions with recursive trigonometric components
        f2 = 0.8 * np.sum(np.sin(12.0 * np.sin(7.0 * x)) * np.cos(9.0 * np.cos(4.0 * x)))
        
        # Novel radial basis components with Gaussian and exponential scaling
        f3 = 0.4 * np.sum(np.exp(-0.5 * np.sum((x[:, np.newaxis] - x[np.newaxis, :])**2, axis=0)) * np.sin(3.0 * x))
        
        # Increased polynomial coupling with higher-order terms
        f4 = 0.3 * np.sum((x**4 + 0.3 * x**5 + 0.05 * x**6) * np.sin(2.5 * x) * np.cos(2.0 * x))
        
        # Adaptive scaling with dynamic frequency modulation
        f5 = 0.25 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Multi-scale interaction terms with fractional powers and logarithmic scaling
        f6 = 0.2 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.log(1.0 + np.abs(x)))
        
        # Saddle point generator with hyperbolic tangent and polynomial coupling
        f7 = 0.18 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.sin(8.0 * x))
        
        # Novel adaptive scaling with exponential decay and sinusoidal perturbations
        f8 = 0.15 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(25.0 * x) * np.cos(20.0 * x))
        
        # Nested chaotic modulation with recursive trigonometric components
        f9 = 0.12 * np.sum(np.sin(np.sin(np.sin(5.0 * x))) * np.cos(np.cos(np.cos(4.0 * x))))
        
        # Additional chaotic modulation with fractional Brownian motion inspired terms
        f10 = 0.1 * np.sum(np.sin(15.0 * np.abs(x)**0.7) * np.cos(10.0 * np.abs(x)**0.5))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10