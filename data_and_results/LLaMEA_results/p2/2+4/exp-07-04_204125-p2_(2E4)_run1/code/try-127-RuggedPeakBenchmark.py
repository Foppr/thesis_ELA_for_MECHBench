import numpy as np

class RuggedPeakBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for performance
        self.peak_positions = np.random.uniform(-5.0, 5.0, (10, dim))
        self.peak_heights = np.random.uniform(1.0, 5.0, 10)
        self.ruggedness = 0.5 + 0.5 * np.random.rand()
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Multiple peak terms with varying heights and positions
        for i in range(10):
            peak_pos = self.peak_positions[i]
            height = self.peak_heights[i]
            distance = np.sum((x - peak_pos)**2)
            # Gaussian peak with adjustable ruggedness
            result += height * np.exp(-distance / (2.0 * (0.5 + self.ruggedness * np.random.rand())**2))
        
        # Add a smooth quadratic basin term to encourage convergence
        result += 0.1 * np.sum(x**2)
        
        # Introduce dimensionality-dependent complexity
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= dim_factor
        
        # Add a sinusoidal modulation to increase landscape complexity
        modulation = np.sin(0.5 * np.sum(x))
        result += 0.3 * modulation
        
        # Add a small noise term to make the function non-deterministic for different runs
        noise = 0.01 * np.random.rand()
        result += noise
        
        return result