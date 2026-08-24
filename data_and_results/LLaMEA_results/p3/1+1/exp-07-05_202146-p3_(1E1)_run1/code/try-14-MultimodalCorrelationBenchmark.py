import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying correlation terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.1 * (i + j))
                result += decay * np.sin(x[i]) * np.cos(x[j])
                
        # Add multimodal sinusoidal components with varying amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.3 * np.sin(5 * x[i])
            
        # Include interaction terms with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(-0.5 * (x[i]**2 + x[j]**2))
                result += 0.2 * interaction * np.sin(x[i] * x[j])
                
        # Add a saddle-point structure
        sum_x_sq = np.sum(x**2)
        result += 0.1 * sum_x_sq * np.cos(0.5 * sum_x_sq)
        
        # Add a complex multi-modal component
        product_x = np.prod(x)
        result += 0.4 * np.sin(4 * product_x) * np.cos(3 * product_x)
        
        # Add a global shaping term
        result += 0.05 * np.sum(np.abs(x)**3) + 0.01 * np.sum(x**6)
        
        return result