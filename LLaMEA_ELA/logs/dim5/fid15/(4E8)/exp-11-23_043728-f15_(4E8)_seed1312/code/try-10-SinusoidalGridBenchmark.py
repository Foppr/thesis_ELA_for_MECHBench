import numpy as np

class SinusoidalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        x_scaled = x * np.pi / 5.0
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add exponentially increasing sinusoidal grid components with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-term sinusoidal components with exponential weights
                weight = 2**(i + j)  # Increasing weights for higher dimensions
                result += weight * np.sin(x_scaled[i]) * np.sin(x_scaled[j])
                
        # Add periodic components that create multiple global minima with varying depths
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * x_scaled[i]) * np.cos(4 * x_scaled[i]) * np.exp(-0.1 * abs(x[i]))
            
        # Add saddle point components to increase complexity
        for i in range(self.dim):
            result += 0.2 * np.sin(x_scaled[i])**3 * np.cos(x_scaled[i])**3
            
        # Add a large penalty term that heavily penalizes being near the origin
        distance_from_origin = np.linalg.norm(x)
        if distance_from_origin < 1.0:
            result += 10.0 * (1.0 - distance_from_origin)**2
            
        # Add a small random component to make the function non-reproducible
        np.random.seed(42)  # For consistent testing but still random enough
        result += 0.05 * np.random.random()
        
        return result