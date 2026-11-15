import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Enhanced exponential decay with sinusoidal modulation and altered decay rate
        f2 = np.sum(np.exp(-0.4 * x**2) * np.sin(4.0 * x) * np.cos(2.0 * x))
        
        # Chaotic component using a modified logistic map with piecewise behavior
        chaotic_term = np.zeros_like(x)
        for i in range(len(x)):
            if x[i] < 0:
                chaotic_term[i] = np.sin(x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
            else:
                chaotic_term[i] = np.sin(x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        f3 = np.sum(chaotic_term)
        
        # High-frequency oscillation term to increase ruggedness
        f4 = 0.6 * np.sum(np.sin(25.0 * x) * np.exp(-0.03 * x**2))
        
        # Additional cosine modulation to create more complex landscape
        f5 = 0.2 * np.sum(np.cos(10.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all components with adjusted weights
        return f1 + 0.4 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5