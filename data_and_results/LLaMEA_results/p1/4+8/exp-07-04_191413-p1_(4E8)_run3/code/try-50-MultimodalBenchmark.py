import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.5, 2.5, 15)
        # Additional chaotic parameters
        self.chaos_params = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        # Enhanced radial basis function component with more centers
        rb_value = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            rb_value += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sine wave component with cross-dimensional coupling
        chaotic_wave = 0.0
        for i in range(self.dim):
            chaotic_wave += np.sin(self.chaos_params[i] * x[i]) * np.cos(self.chaos_params[i] * x[i] * 0.5)
        
        # Adaptive noise component with position-dependent frequency
        noise = np.sum(np.sin(2 * x) * np.cos(0.3 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Polynomial conditioning term with higher order terms
        poly_term = np.sum(x**5 + 0.15 * x**6 + 0.05 * x**7)
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.exp(0.1 * x[i] * x[i+1]) * (x[i]**2 + x[i+1]**2)
        
        # Additional harmonic component
        harmonic = np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        # Combine all terms with different scaling factors
        return rb_value + 0.7 * chaotic_wave + 0.6 * noise + 0.15 * poly_term + 0.1 * cross_term + 0.2 * harmonic