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
                # Cross-term sinusoidal components with varying frequencies
                result += 0.3 * np.sin(1.5 * x_scaled[i]) * np.cos(2.0 * x_scaled[j])
                
        # Add periodic components that create multiple global minima with varying amplitudes
        for i in range(self.dim):
            result += 0.4 * np.sin(3 * x_scaled[i]) * np.sin(4 * x_scaled[i]) * np.cos(x_scaled[i])
            
        # Add exponential modulation to increase landscape complexity
        exp_modulation = 1.0 + 0.2 * np.exp(-0.5 * np.sum(x**2))
        result *= exp_modulation
        
        # Add a small random component to make the function non-reproducible
        np.random.seed(hash(str(x)) % (2**32))  # Unique seed per input for consistency in testing
        result += 0.05 * np.random.random()
        
        return result