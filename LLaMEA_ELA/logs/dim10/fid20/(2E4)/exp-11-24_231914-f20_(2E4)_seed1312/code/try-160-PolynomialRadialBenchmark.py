import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial degree and coefficients for each dimension
        self.degrees = np.random.randint(3, 7, size=dim)
        self.coefficients = np.random.uniform(-2.0, 2.0, size=(dim, 4))
        # Initialize radial symmetry parameters
        self.radial_centers = np.random.uniform(-3.0, 3.0, size=dim)
        self.radial_weights = np.random.uniform(0.5, 2.0, size=dim)
        # Initialize conditioning factors for each dimension
        self.conditioning_factors = np.random.uniform(0.1, 10.0, size=dim)
        # Initialize local minima positions and strengths
        self.local_minima = np.random.uniform(-4.0, 4.0, size=(5, dim))
        self.minima_strengths = np.random.uniform(1.0, 5.0, size=5)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley component
        polynomial_valley = 0.0
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(4):
                poly_term += self.coefficients[i, j] * (x[i] ** (j + 1))
            polynomial_valley += poly_term * self.conditioning_factors[i]
            
        # Radial symmetry component with adaptive weights
        radial_component = 0.0
        for i in range(self.dim):
            distance_from_center = np.abs(x[i] - self.radial_centers[i])
            radial_component += self.radial_weights[i] * np.exp(-0.5 * (distance_from_center**2))
            
        # Adaptive conditioning component with varying curvature
        conditioning_component = 0.0
        for i in range(self.dim):
            conditioning_component += self.conditioning_factors[i] * (x[i]**2)
            
        # Local minima attraction component
        local_attraction = 0.0
        for k in range(5):
            distance = np.sum((x - self.local_minima[k])**2)
            local_attraction += self.minima_strengths[k] / (1.0 + distance)
            
        # Cross-dimensional interaction with polynomial coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x[i]**2) * (x[j]**self.degrees[i]) * np.sin(x[i] * x[j])
                
        # Combine all components with optimized weights
        return (1.5 * polynomial_valley + 
                1.3 * radial_component + 
                1.2 * conditioning_component + 
                1.4 * local_attraction + 
                0.9 * cross_interaction)