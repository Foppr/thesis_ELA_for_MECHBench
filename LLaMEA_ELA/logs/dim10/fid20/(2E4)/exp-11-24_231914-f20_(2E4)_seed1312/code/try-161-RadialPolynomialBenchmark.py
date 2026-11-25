import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial symmetry parameters
        self.center = np.random.uniform(-2.0, 2.0, size=dim)
        self.radius_scale = np.random.uniform(0.5, 3.0)
        # Initialize polynomial exponents and coefficients
        self.exponents = np.random.uniform(2.0, 6.0, size=dim)
        self.coefficients = np.random.uniform(-1.0, 1.0, size=dim)
        # Initialize cross-dimensional interaction weights
        self.interaction_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        # Initialize adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.1, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial symmetry component
        radial_distance = np.sqrt(np.sum((x - self.center)**2))
        radial_component = np.exp(-self.radius_scale * radial_distance**2) * \
                          np.sin(radial_distance * 3.0) * np.cos(radial_distance * 2.0)
        
        # Polynomial conditioning component
        polynomial_component = 0.0
        for i in range(self.dim):
            polynomial_component += self.coefficients[i] * (x[i]**self.exponents[i])
            
        # Cross-dimensional interaction terms
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_weights[i, j] * x[i] * x[j]
                    
        # Adaptive scaling component
        scaling_component = 0.0
        for i in range(self.dim):
            scaling_component += self.scaling_factors[i] * np.sin(x[i] * (i + 1))
            
        # Multi-scale oscillatory pattern
        oscillatory_component = 0.0
        for i in range(self.dim):
            oscillatory_component += np.sin(2.5 * x[i]) * np.cos(1.5 * x[i]) * \
                                  np.exp(-0.1 * (x[i] - self.center[i])**2)
            
        # Combine all components with optimized weights
        return (1.5 * radial_component + 
                1.2 * polynomial_component + 
                1.3 * interaction_component + 
                1.1 * scaling_component + 
                0.9 * oscillatory_component)