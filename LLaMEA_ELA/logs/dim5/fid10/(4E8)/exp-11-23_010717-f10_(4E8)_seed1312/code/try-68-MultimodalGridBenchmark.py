import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal basin term with chaotic scaling
        basin = 0.15 * np.sum(x**2) + 0.05 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Complex grid of global minima terms with fractal-like frequency patterns
        grid_minima = 0.0
        for i in range(self.dim):
            # Fractal-inspired trigonometric pattern with varying coefficients
            grid_minima += 4.0 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + \
                          1.5 * np.sin(3.0 * x[i]) * np.cos(2.5 * x[i]) + \
                          0.8 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + \
                          0.3 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
            
        # Enhanced cross-terms with fractal coupling and nonlinear interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like cross-interactions with chaotic coupling strength
                cross_terms += 1.0 * np.sin(1.5 * x[i]) * np.cos(1.8 * x[j]) + \
                              0.6 * np.cos(2.0 * x[i]) * np.sin(2.2 * x[j]) + \
                              0.4 * np.sin(1.2 * x[i]) * np.sin(1.7 * x[j]) + \
                              0.3 * np.cos(1.8 * x[i]) * np.cos(1.3 * x[j])
        
        # Adaptive noise term with fractal characteristics
        noise = 0.02 * np.sum(np.sin(8.0 * x) * np.cos(6.0 * x) * np.sin(4.0 * x))
        
        # Cubic and quartic terms with enhanced nonlinearity
        cubic_term = 0.1 * np.sum(x**3)
        quartic_term = 0.03 * np.sum(x**4)
        
        # Add chaotic perturbation term for increased landscape complexity
        chaotic_perturbation = 0.05 * np.sum(np.sin(7.0 * x) * np.cos(9.0 * x) * np.sin(5.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + chaotic_perturbation