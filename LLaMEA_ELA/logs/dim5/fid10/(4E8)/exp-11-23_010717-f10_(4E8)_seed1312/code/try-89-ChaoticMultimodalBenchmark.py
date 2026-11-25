import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal basin term with chaotic scaling and additional polynomial
        basin = 0.15 * np.sum(x**2) + 0.08 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x)) + 0.02 * np.sum(x**4)
        
        # Modified grid of global minima with altered frequencies and amplitudes
        grid_minima = 0.0
        for i in range(self.dim):
            grid_minima += 5.1 * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i]) + \
                          2.3 * np.sin(3.7 * x[i]) * np.cos(3.1 * x[i]) + \
                          1.1 * np.sin(4.8 * x[i]) * np.cos(4.2 * x[i]) + \
                          0.4 * np.sin(5.9 * x[i]) * np.cos(5.1 * x[i])
            
        # Enhanced cross-terms with increased coupling strength and new interaction patterns
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 1.5 * np.sin(2.1 * x[i]) * np.cos(2.1 * x[j]) + \
                              1.1 * np.cos(2.7 * x[i]) * np.sin(2.7 * x[j]) + \
                              0.8 * np.sin(1.9 * x[i]) * np.sin(1.9 * x[j]) + \
                              0.5 * np.cos(2.3 * x[i]) * np.cos(2.3 * x[j])
        
        # Additional noise with different fractal characteristics and chaotic distribution
        noise = 0.03 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) + np.cos(12.0 * x) * np.sin(7.0 * x))
        
        # Higher-order polynomial terms with modified coefficients for increased complexity
        cubic_term = 0.1 * np.sum(x**3)
        quartic_term = 0.05 * np.sum(x**4)
        quintic_term = 0.025 * np.sum(x**5)
        
        # Chaotic sine-cosine combination with altered frequencies for additional landscape complexity
        chaotic_component = 0.06 * np.sum(np.sin(13.0 * x) + np.cos(14.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + quintic_term + chaotic_component