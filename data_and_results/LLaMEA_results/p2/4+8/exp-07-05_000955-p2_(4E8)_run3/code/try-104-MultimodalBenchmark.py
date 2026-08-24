import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2)
        
        # Logarithmic modulation with trigonometric coupling for multi-scale structure
        f2 = 0.3 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Adaptive radial basis with exponential decay and sine modulation
        f3 = 0.25 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(8.0 * np.sum(x**2)))
        
        # Coupled sine-cosine waves with polynomial scaling for increased complexity
        f4 = 0.2 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * (1.0 + 0.3 * x**2))
        
        # Multi-dimensional Gaussian interaction with dynamic amplitude
        f5 = 0.15 * np.sum(np.exp(-0.1 * np.sum((x - 0.5)**2)) * np.sin(20.0 * x))
        
        # Nested logarithmic and polynomial terms for fine-scale structure
        f6 = 0.1 * np.sum(np.log(1.0 + np.abs(x)) * x**4)
        
        # Asymmetric polynomial coupling with trigonometric modulation
        f7 = 0.12 * np.sum((x**3) * np.sin(7.0 * x) * np.cos(9.0 * x))
        
        # Adaptive multi-modal sine-wave interaction with dynamic frequency
        f8 = 0.08 * np.sum(np.sin(25.0 * x) * np.cos(18.0 * x) * np.exp(-0.2 * np.sum(x**2)))
        
        # Hybrid radial and trigonometric term for enhanced nonlinearity
        f9 = 0.1 * np.sum(np.exp(-0.3 * np.sum(x**2)) * np.sin(12.0 * x) * np.cos(6.0 * x))
        
        # Cross-dimensional interaction with logarithmic scaling
        f10 = 0.09 * np.sum(np.log(1.0 + np.abs(np.sum(x))) * np.sin(14.0 * x))
        
        # Novel term: Combines polynomial, logarithmic, and trigonometric components for high complexity
        f11 = 0.07 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(22.0 * x) * (x**5))
        
        # Additional interaction term with dynamic Gaussian modulation
        f12 = 0.06 * np.sum(np.exp(-0.4 * np.sum(x**2)) * np.cos(16.0 * x) * np.sin(11.0 * x))
        
        # Final combined term with weighted sum for balanced multimodality
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12