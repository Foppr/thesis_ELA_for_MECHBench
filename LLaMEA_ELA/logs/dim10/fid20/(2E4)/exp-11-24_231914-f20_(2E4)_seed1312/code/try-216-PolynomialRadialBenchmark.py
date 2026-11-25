import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters
        self.poly_degrees = np.random.randint(2, 6, size=dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=dim)
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=dim)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, size=dim)
        # Adaptive gradient modulation parameters
        self.grad_modulation = np.random.uniform(0.1, 2.0, size=dim)
        self.adaptive_scale = np.random.uniform(0.5, 3.0, size=dim)
        # Dynamic curvature parameters
        self.curvature_params = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Multi-scale interaction weights
        self.interaction_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        # Time-varying fitness landscape components
        self.time_varying = np.random.uniform(0.1, 1.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            term = 0.0
            for d in range(1, self.poly_degrees[i] + 1):
                term += self.poly_coeffs[i] * (x[i] ** d)
            poly_component += term
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = np.sum((x - self.rbf_centers[i, :]) ** 2)
                rbf_sum += self.rbf_weights[i] * np.exp(-distance / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_sum
        
        # Adaptive gradient modulation
        grad_modulation = 0.0
        for i in range(self.dim):
            grad_modulation += self.grad_modulation[i] * np.sin(x[i]) * np.cos(self.adaptive_scale[i] * x[i])
        
        # Dynamic curvature effects
        curvature_effect = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    curvature_effect += self.curvature_params[i, j] * x[i] * x[j]
        
        # Multi-scale interaction terms
        interaction_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_terms += self.interaction_weights[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Time-varying fitness component
        time_component = 0.0
        for i in range(self.dim):
            time_component += self.time_varying[i] * np.sin(0.5 * x[i] + np.pi * (i+1) / self.dim)
        
        # Combine all components with dynamic weighting
        total_fitness = (0.8 * poly_component + 
                        1.2 * rbf_component + 
                        0.6 * grad_modulation + 
                        0.4 * curvature_effect + 
                        0.3 * interaction_terms + 
                        0.5 * time_component)
        
        return total_fitness