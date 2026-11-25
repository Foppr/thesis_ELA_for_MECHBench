import numpy as np

class SinusoidalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        x_scaled = x * np.pi / 5.0
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add sinusoidal grid components with multiple local minima
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-term sinusoidal components
                result += 0.5 * np.sin(x_scaled[i]) * np.sin(x_scaled[j])
                
        # Add periodic components that create multiple global minima
        for i in range(self.dim):
            result += 0.3 * np.sin(2 * x_scaled[i]) * np.cos(3 * x_scaled[i])
            
        # Add a small random component to make the function non-reproducible
        np.random.seed(42)  # For consistent testing but still random enough
        result += 0.1 * np.random.random()
        
        return result