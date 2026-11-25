import numpy as np

class LogisticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component with varying r values for complexity
        logistic_term = 0.0
        r_values = np.linspace(3.5, 4.0, self.dim)
        x_log = np.random.rand()
        for i in range(self.dim):
            x_log = r_values[i] * x_log * (1 - x_log)
            logistic_term += np.sin(x_log * np.pi) ** 2
        
        # Radial basis function component with adaptive widths
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / (0.3**2))
        
        # Polynomial chaos expansion with Hermite polynomials
        poly_term = np.sum(x**3 + 0.5 * x**2 - 0.3 * x + 1.0)
        
        # Sine wave interference with variable frequencies and amplitudes
        sine_term = np.sum(np.sin(2.0 * x) + 0.7 * np.sin(5.0 * x) + 0.4 * np.sin(9.0 * x))
        
        # Gaussian radial basis with varying scales to create multi-scale features
        gauss_rbf_term = 0.0
        scales = np.logspace(-1, 1, 8)
        for scale in scales:
            gauss_rbf_term += np.sum(np.exp(-0.5 * (x**2) / scale**2))
        
        # Cross-term interaction with exponential decay
        cross_term = np.sum(np.exp(-np.abs(x[:-1] - x[1:])) * (x[:-1] + x[1:]))
        
        # Hyperbolic tangent distortion for non-linearity
        tanh_term = np.sum(np.tanh(2.0 * x) ** 2)
        
        # Quadratic and cubic polynomial with mixed coefficients
        quad_cubic_term = np.sum(0.5 * x**2 + 0.3 * x**3 - 0.1 * x**4)
        
        # Add global scaling and offset for balanced contribution
        return 0.25 * logistic_term + 0.20 * rbf_term + 0.15 * poly_term + 0.12 * sine_term + 0.10 * gauss_rbf_term + 0.08 * cross_term + 0.07 * tanh_term + 0.03 * quad_cubic_term + 1.5