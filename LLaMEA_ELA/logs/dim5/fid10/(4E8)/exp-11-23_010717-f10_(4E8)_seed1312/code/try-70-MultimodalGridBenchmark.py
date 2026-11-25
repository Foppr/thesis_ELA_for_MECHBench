import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin term with chaotic scaling factors
        basin = 0.1 * np.sum(x**2) + 0.05 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Enhanced grid of global minima with fractal-like interactions
        grid_minima = 0.0
        for i in range(self.dim):
            # Fractal trigonometric pattern with varying frequencies and amplitudes
            grid_minima += 4.0 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + \
                          1.5 * np.sin(3.0 * x[i]) * np.cos(2.5 * x[i]) + \
                          0.8 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + \
                          0.3 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
            
        # Complex cross-terms with fractal-like coupling and chaotic interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic cross-interactions with fractal scaling
                cross_terms += 1.0 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[j]) + \
                              0.7 * np.cos(2.5 * x[i]) * np.sin(2.0 * x[j]) + \
                              0.5 * np.sin(1.8 * x[i]) * np.sin(1.8 * x[j]) + \
                              0.3 * np.cos(1.2 * x[i]) * np.cos(1.2 * x[j])
        
        # Fractal noise term with chaotic frequency components
        noise = 0.02 * np.sum(np.sin(9.0 * x) * np.cos(7.0 * x) + np.cos(5.0 * x) * np.sin(3.0 * x))
        
        # Cubic and quartic terms with fractal scaling
        cubic_term = 0.1 * np.sum(x**3)
        quartic_term = 0.05 * np.sum(x**4)
        
        # Add chaotic perturbation to increase algorithmic challenge
        chaotic_perturbation = 0.03 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) * np.sin(6.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + chaotic_perturbation