import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Fractal-like structure using nested trigonometric functions
        f2 = 0.5 * np.sum(np.sin(10.0 * np.sin(5.0 * x)) * np.cos(8.0 * np.cos(3.0 * x)))
        
        # Polynomial chaos expansion with mixed monomials
        f3 = 0.3 * np.sum((x**2 + x**3 + x**4) * np.sin(7.0 * x) * np.cos(4.0 * x))
        
        # Adaptive gradient modulation with exponential scaling
        f4 = 0.25 * np.sum(np.exp(-0.2 * np.sum(x**2)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Saddle point enhancement through coupled sine and cosine waves
        f5 = 0.2 * np.sum(np.sin(6.0 * x) * np.cos(9.0 * x) * np.sin(3.0 * x))
        
        # Non-separable interaction using higher-order polynomial coupling
        f6 = 0.15 * np.sum((x**5) * np.sin(5.0 * x) * np.cos(7.0 * x))
        
        # Multi-scale fractal modulation with Gaussian-like decay
        f7 = 0.1 * np.sum(np.exp(-0.1 * np.sum(x**2)) * np.sin(20.0 * x) * np.cos(12.0 * x))
        
        # Enhanced multimodality with nested exponential and trigonometric terms
        f8 = 0.12 * np.sum(np.exp(-0.3 * np.sum(x**2)) * np.sin(18.0 * x) * np.cos(14.0 * x) * (1.0 + 0.3 * np.sin(8.0 * x)))
        
        # Additional coupling term for increased complexity
        f9 = 0.08 * np.sum(np.sin(11.0 * x) * np.cos(13.0 * x) * np.exp(-0.15 * np.sum(x**2)) * x**3)
        
        # Final term to ensure landscape is highly non-convex and challenging
        f10 = 0.06 * np.sum(np.sin(25.0 * x) * np.cos(20.0 * x) * np.exp(-0.25 * np.sum(x**2)) * x**4)
        
        # Combine all terms with adjusted weights for better balance
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10