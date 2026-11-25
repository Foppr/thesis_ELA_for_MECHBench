import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal basin term with chaotic scaling and additional polynomial
        basin = 0.2 * np.sum(x**2) + 0.1 * np.sum(np.sin(15.0 * x) * np.cos(10.0 * x)) + 0.03 * np.sum(x**4)
        
        # Modified grid of global minima with altered frequencies and amplitudes
        grid_minima = 0.0
        for i in range(self.dim):
            grid_minima += 6.5 * np.sin(3.2 * x[i]) * np.cos(2.7 * x[i]) + \
                          3.3 * np.sin(4.4 * x[i]) * np.cos(3.9 * x[i]) + \
                          1.9 * np.sin(5.7 * x[i]) * np.cos(5.1 * x[i]) + \
                          0.65 * np.sin(7.0 * x[i]) * np.cos(6.0 * x[i])
            
        # Enhanced cross-terms with increased coupling strength and new interaction patterns
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 2.3 * np.sin(3.2 * x[i]) * np.cos(3.2 * x[j]) + \
                              2.0 * np.cos(3.7 * x[i]) * np.sin(3.7 * x[j]) + \
                              1.6 * np.sin(2.9 * x[i]) * np.sin(2.9 * x[j]) + \
                              1.2 * np.cos(3.4 * x[i]) * np.cos(3.4 * x[j])
        
        # Additional noise with different fractal characteristics and chaotic distribution
        noise = 0.06 * np.sum(np.sin(16.0 * x) * np.cos(13.0 * x) + np.cos(19.0 * x) * np.sin(11.0 * x))
        
        # Higher-order polynomial terms with modified coefficients for increased complexity
        cubic_term = 0.20 * np.sum(x**3)
        quartic_term = 0.14 * np.sum(x**4)
        quintic_term = 0.09 * np.sum(x**5)
        sextic_term = 0.05 * np.sum(x**6)
        
        # Chaotic sine-cosine combination with altered frequencies for additional landscape complexity
        chaotic_component = 0.13 * np.sum(np.sin(19.0 * x) + np.cos(20.0 * x))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + quintic_term + sextic_term + chaotic_component