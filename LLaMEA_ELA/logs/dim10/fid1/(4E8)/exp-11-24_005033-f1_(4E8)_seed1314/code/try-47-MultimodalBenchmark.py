import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Core multimodal component with enhanced chaotic interactions
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 3.0 * np.sum(np.cos(15 * x) * np.sin(20 * x)) + 0.02 * np.sum(x**4)
        
        # Enhanced polynomial conditioning with adaptive penalties
        result += 0.2 * np.sum((x**2 + x**3 + x**4) / (1.0 + np.abs(x)) * np.log(1.0 + np.abs(x)))
        
        # Stronger cross-dimensional couplings with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(10 * x[i]) * np.cos(10 * x[j]) * (x[i]**2 + x[j]**2 + x[i]*x[j])
        
        # Additional high-frequency chaotic component
        result += 0.1 * np.sum(np.sin(25 * x) * np.cos(30 * x))
        
        # Modified barrier term for better conditioning
        result += 0.01 * np.sum(np.exp(x**2 / 50.0) - 1.0)
        
        return result