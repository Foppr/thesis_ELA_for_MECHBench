import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - pulls towards origin
        basin = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms with modified frequencies
        grid_minima = 0.0
        for i in range(self.dim):
            # Create periodic pattern with multiple local minima using altered coefficients
            grid_minima += 1.5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            
        # Add interactive cross-terms to increase landscape complexity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.3 * np.sin(0.5 * x[i]) * np.cos(0.5 * x[j])
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(10 * x))
        
        return basin + grid_minima + cross_terms + noise