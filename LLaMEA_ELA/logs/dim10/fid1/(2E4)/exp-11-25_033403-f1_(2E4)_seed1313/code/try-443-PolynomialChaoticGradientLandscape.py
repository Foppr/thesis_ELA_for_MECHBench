import numpy as np

class PolynomialChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial components with varying degrees
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(-1.0, 1.0, dim)
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize gradient modulation factors
        self.gradient_modulation = np.random.uniform(0.5, 2.0, dim)
        # Initialize hybrid coupling coefficients for inter-dimensional interactions
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Initialize dynamic weights for different components
        self.weights = np.random.dirichlet([1.0] * 5)
        
    def f(self, x):
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial components
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = self.poly_coefficients[j] * (x[j] ** self.poly_degrees[j])
            poly_terms += poly_term
        
        # Compute chaotic logistic map components
        logistic_terms = 0.0
        for j in range(self.dim):
            self.logistic_x[j] = self.logistic_r[j] * self.logistic_x[j] * (1 - self.logistic_x[j])
            logistic_terms += self.logistic_x[j]
        
        # Compute gradient modulation components
        grad_terms = 0.0
        for j in range(self.dim):
            grad_term = self.gradient_modulation[j] * np.sin(x[j])
            grad_terms += grad_term
        
        # Compute coupling terms between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_coeffs[i, j] * x[i] * x[j]
        
        # Compute additional nonlinear interaction terms
        interaction_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_terms += (x[i] - x[j])**2
        
        # Combine all components with dynamic weights
        total = (self.weights[0] * poly_terms + 
                 self.weights[1] * logistic_terms + 
                 self.weights[2] * grad_terms + 
                 self.weights[3] * coupling_terms + 
                 self.weights[4] * interaction_terms)
        
        return total