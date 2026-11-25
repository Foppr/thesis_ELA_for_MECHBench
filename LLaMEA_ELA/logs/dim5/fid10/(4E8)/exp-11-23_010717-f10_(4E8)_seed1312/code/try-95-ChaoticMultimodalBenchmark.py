import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal basin term with chaotic scaling and multiple frequencies
        basin = 0.18 * np.sum(x**2) + 0.09 * np.sum(np.sin(13.0 * x) * np.cos(10.0 * x)) + \
                0.04 * np.sum(np.sin(8.0 * x) * np.cos(6.0 * x)) + \
                0.025 * np.sum(np.sin(16.0 * x) * np.cos(14.0 * x))
        
        # Modified grid of global minima with higher frequency interactions
        grid_minima = 0.0
        for i in range(self.dim):
            grid_minima += 5.5 * np.sin(2.7 * x[i]) * np.cos(2.2 * x[i]) + \
                          2.8 * np.sin(4.0 * x[i]) * np.cos(3.3 * x[i]) + \
                          1.4 * np.sin(5.0 * x[i]) * np.cos(4.5 * x[i]) + \
                          0.6 * np.sin(6.5 * x[i]) * np.cos(6.0 * x[i])
            
        # Increased cross-terms with enhanced chaotic interaction patterns and fractal coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 1.7 * np.sin(2.2 * x[i]) * np.cos(2.2 * x[j]) + \
                              1.3 * np.cos(2.7 * x[i]) * np.sin(2.7 * x[j]) + \
                              0.9 * np.sin(1.7 * x[i]) * np.sin(1.7 * x[j]) + \
                              0.6 * np.cos(2.0 * x[i]) * np.cos(2.0 * x[j]) + \
                              0.4 * np.sin(3.2 * x[i]) * np.cos(3.2 * x[j])
        
        # Enhanced noise with fractal characteristics and chaotic distribution
        noise = 0.035 * np.sum(np.sin(11.0 * x) * np.cos(9.0 * x) + np.cos(13.0 * x) * np.sin(8.0 * x))
        
        # Higher-order polynomial terms for increased complexity and nonlinearity
        cubic_term = 0.12 * np.sum(x**3)
        quartic_term = 0.05 * np.sum(x**4)
        quintic_term = 0.025 * np.sum(x**5)
        sextic_term = 0.015 * np.sum(x**6)
        
        # Additional chaotic sine-cosine combination for enhanced landscape complexity
        chaotic_component = 0.06 * np.sum(np.sin(15.0 * x) + np.cos(16.0 * x) + np.sin(17.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + quintic_term + sextic_term + chaotic_component