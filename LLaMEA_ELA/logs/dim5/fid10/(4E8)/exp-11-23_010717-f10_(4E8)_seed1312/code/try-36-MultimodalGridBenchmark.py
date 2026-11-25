import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - pulls towards origin with stronger influence
        basin = 0.2 * np.sum(x**2)
        
        # Grid of global minima terms with enhanced frequencies and amplitudes
        grid_minima = 0.0
        for i in range(self.dim):
            # Enhanced trigonometric pattern with varied coefficients
            grid_minima += 2.5 * np.sin(1.3 * x[i]) * np.cos(0.9 * x[i]) + \
                          0.6 * np.sin(2.2 * x[i]) * np.cos(1.6 * x[i])
            
        # Add interactive cross-terms with higher interaction strength
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased complexity through nonlinear cross-interactions
                cross_terms += 0.6 * np.sin(0.9 * x[i]) * np.sin(0.9 * x[j]) + \
                              0.25 * np.cos(1.1 * x[i]) * np.cos(1.1 * x[j])
        
        # Add a small noise term to increase challenge
        noise = 0.025 * np.sum(np.sin(5.5 * x) * np.cos(3.5 * x))
        
        return basin + grid_minima + cross_terms + noise