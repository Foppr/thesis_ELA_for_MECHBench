import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal basin term with chaotic scaling and multiple frequencies
        basin = 0.15 * np.sum(x**2) + 0.08 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x)) + \
                0.03 * np.sum(np.sin(7.0 * x) * np.cos(5.0 * x)) + \
                0.02 * np.sum(np.sin(15.0 * x) * np.cos(13.0 * x))
        
        # Modified grid of global minima with higher frequency interactions
        grid_minima = 0.0
        for i in range(self.dim):
            grid_minima += 5.0 * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i]) + \
                          2.5 * np.sin(3.8 * x[i]) * np.cos(3.1 * x[i]) + \
                          1.2 * np.sin(4.7 * x[i]) * np.cos(4.2 * x[i]) + \
                          0.5 * np.sin(6.0 * x[i]) * np.cos(5.5 * x[i])
            
        # Increased cross-terms with enhanced chaotic interaction patterns and fractal coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 1.5 * np.sin(2.0 * x[i]) * np.cos(2.0 * x[j]) + \
                              1.1 * np.cos(2.5 * x[i]) * np.sin(2.5 * x[j]) + \
                              0.8 * np.sin(1.5 * x[i]) * np.sin(1.5 * x[j]) + \
                              0.5 * np.cos(1.8 * x[i]) * np.cos(1.8 * x[j]) + \
                              0.3 * np.sin(3.0 * x[i]) * np.cos(3.0 * x[j])
        
        # Enhanced noise with fractal characteristics and chaotic distribution
        noise = 0.03 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) + np.cos(12.0 * x) * np.sin(7.0 * x))
        
        # Higher-order polynomial terms for increased complexity and nonlinearity
        cubic_term = 0.1 * np.sum(x**3)
        quartic_term = 0.04 * np.sum(x**4)
        quintic_term = 0.02 * np.sum(x**5)
        sextic_term = 0.01 * np.sum(x**6)
        
        # Additional chaotic sine-cosine combination for enhanced landscape complexity
        chaotic_component = 0.05 * np.sum(np.sin(14.0 * x) + np.cos(15.0 * x) + np.sin(16.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + quintic_term + sextic_term + chaotic_component