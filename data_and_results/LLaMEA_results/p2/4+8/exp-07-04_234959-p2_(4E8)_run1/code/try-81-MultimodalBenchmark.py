import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamically shifted global minimum with chaotic progression
        self.global_min = np.array([(-1)**i * 2.5 + 0.3 * np.sin(i * np.pi / 3 + np.sqrt(i + 1)) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling and chaotic modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(x * np.cos(x))))
        
        # Enhanced sinusoidal modulations with multi-frequency coupling
        f2 = np.sum(np.sin(7.0 * x + np.cos(2.0 * x)) * np.cos(4.0 * x + np.sin(1.5 * x)))
        
        # Higher-order polynomial interactions with chaotic cross-terms
        f3 = np.sum(x**6 - 20 * x**4 + 100 * x**2 - 50)
        
        # Exponential penalty with logarithmic and hyperbolic scaling
        f4 = np.sum(np.exp(0.4 * np.abs(x)) - 1 - 0.3 * np.log(1 + np.abs(x)) - 0.1 * np.tanh(x))
        
        # Chaotic component using nested sine and cosine with time-varying coefficients
        f5 = np.sum(np.sin(np.cos(x * np.sin(x))) + np.cos(np.sin(x * np.cos(x))))
        
        # Additional chaotic coupling term with variable phase shift
        f6 = np.sum(np.sin(x * np.cos(x * np.sin(x))) * np.cos(x * np.sin(x * np.cos(x))))
        
        # Logarithmic barrier terms to increase difficulty near boundaries
        f7 = np.sum(10 * np.log(1 + np.abs(x - 5)) + 10 * np.log(1 + np.abs(x + 5)))
        
        # Combine all components with varying weights and chaotic scaling
        return 0.1 * f1 + 0.2 * f2 + 0.15 * f3 + 0.2 * f4 + 0.15 * f5 + 0.1 * f6 + 0.1 * f7