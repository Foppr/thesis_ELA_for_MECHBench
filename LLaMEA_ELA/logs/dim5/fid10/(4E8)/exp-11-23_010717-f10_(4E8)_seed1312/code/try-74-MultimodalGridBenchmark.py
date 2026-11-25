import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin term with chaotic scaling
        basin = 0.1 * np.sum(x**2) + 0.05 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x))
        
        # Enhanced grid of global minima with fractal-like frequencies and amplitudes
        grid_minima = 0.0
        for i in range(self.dim):
            grid_minima += 4.2 * np.sin(2.1 * x[i]) * np.cos(1.7 * x[i]) + \
                          1.8 * np.sin(3.2 * x[i]) * np.cos(2.4 * x[i]) + \
                          0.9 * np.sin(4.1 * x[i]) * np.cos(3.3 * x[i]) + \
                          0.3 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
            
        # Complex cross-terms with chaotic interaction patterns and fractal coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 1.2 * np.sin(1.8 * x[i]) * np.cos(1.8 * x[j]) + \
                              0.9 * np.cos(2.2 * x[i]) * np.sin(2.2 * x[j]) + \
                              0.6 * np.sin(1.4 * x[i]) * np.sin(1.4 * x[j]) + \
                              0.3 * np.cos(1.6 * x[i]) * np.cos(1.6 * x[j])
        
        # Enhanced noise with fractal characteristics and chaotic distribution
        noise = 0.025 * np.sum(np.sin(9.0 * x) * np.cos(7.0 * x) + np.cos(11.0 * x) * np.sin(6.0 * x))
        
        # Higher-order polynomial terms for increased complexity and nonlinearity
        cubic_term = 0.08 * np.sum(x**3)
        quartic_term = 0.03 * np.sum(x**4)
        quintic_term = 0.015 * np.sum(x**5)
        
        # Add a chaotic sine-cosine combination for additional landscape complexity
        chaotic_component = 0.04 * np.sum(np.sin(12.0 * x) + np.cos(13.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + quintic_term + chaotic_component